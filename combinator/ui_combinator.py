"""
Gradio UI for the LoRA Combinator tab.

Provides zone-based LoRA management (Always/Loop/Random),
generation settings, and batch image generation.
"""
import os
import random
import time
from datetime import datetime

import gradio as gr

from combinator.shared import config, save_config, DEFAULT_CONFIG
from combinator.lora_utils import LoRA, get_activation_text, discover_loras, refresh_lora_registry
from combinator.zone_manager import (
    state, LoRAEntry,
    format_zone, get_zone_dict, get_zone_lora_choices,
    add_to_zone, remove_from_zone, clear_zone, clear_all_zones,
    update_zone_weight,
    save_zone_config, load_zone_config, list_saved_configs,
    save_prompt_config, load_prompt_config, list_prompt_configs,
    weighted_sample,
)
from combinator.history import (
    load_history, append_history_record,
    compute_generation_hash, build_frequency_map,
)
from combinator import generation_engine


# --- Helper functions ---

def _refresh_loras():
    """Discover LoRAs and update state."""
    refresh_lora_registry()
    state.all_loras = discover_loras()
    state.bank_loras = [lora.name for lora in state.all_loras]
    state.always_loras.clear()
    state.loop_loras.clear()
    state.random_loras.clear()
    count = len(state.all_loras)
    return (
        f"Found {count} LoRAs",
        gr.update(choices=state.bank_loras, value=[]),
    )


def _sort_bank(sort_method):
    if not state.bank_loras:
        return gr.update()
    if sort_method == "A-Z":
        state.bank_loras = sorted(state.bank_loras, key=lambda x: x.lower())
    elif sort_method == "Z-A":
        state.bank_loras = sorted(state.bank_loras, key=lambda x: x.lower(), reverse=True)
    return gr.update(choices=state.bank_loras, value=[])


def _zone_outputs():
    """Return the standard 8-tuple of zone UI updates."""
    return (
        gr.update(choices=state.bank_loras, value=[]),
        format_zone(state.always_loras),
        format_zone(state.loop_loras),
        format_zone(state.random_loras),
        gr.update(choices=get_zone_lora_choices("always")),
        gr.update(choices=get_zone_lora_choices("loop")),
        gr.update(choices=get_zone_lora_choices("random")),
    )


def _do_add_to_zone(selected, zone, default_weight):
    count = add_to_zone(selected, zone, default_weight)
    return (*_zone_outputs(), f"Added {count} LoRA(s) to {zone}")


def _do_remove_from_zone(zone, lora_name):
    remove_from_zone(zone, lora_name)
    return (*_zone_outputs(), f"Removed {lora_name}")


def _do_clear_zone(zone):
    count = clear_zone(zone)
    return (*_zone_outputs(), f"Cleared {count} LoRA(s) from {zone}")


def _do_clear_all():
    count = clear_all_zones()
    return (*_zone_outputs(), f"Cleared {count} LoRA(s) from all zones")


def _get_weight_in_zone(zone, lora_name):
    if not lora_name:
        return gr.update()
    zone_dict = get_zone_dict(zone)
    if zone_dict and lora_name in zone_dict:
        return gr.update(value=zone_dict[lora_name].weight)
    return gr.update(value=0.8)


def _do_update_weight(zone, lora_name, weight):
    update_zone_weight(zone, lora_name, weight)
    zone_dict = get_zone_dict(zone)
    return format_zone(zone_dict) if zone_dict else "(empty)"


def _build_preview(base_prompt, negative_prompt, random_count, batch_size, batch_count):
    if not state.always_loras and not state.loop_loras and not state.random_loras:
        return f"Prompt: {base_prompt}" if base_prompt else "(no LoRAs selected)"

    previews = []
    loop_count = max(1, len(state.loop_loras))
    total = loop_count * int(batch_count) * int(batch_size)
    previews.append(f"=== Will generate {total} image(s) ===")
    previews.append(f"    ({loop_count} variants x {int(batch_count)} batches x {int(batch_size)} per batch)\n")

    if state.always_loras:
        parts = [f"<lora:{n}:{e.weight}>" for n, e in state.always_loras.items()]
        previews.append(f"ALWAYS: {', '.join(parts)}")

    if state.loop_loras:
        previews.append(f"\nLOOP ({len(state.loop_loras)} variants):")
        for name, entry in state.loop_loras.items():
            line = f"  - <lora:{name}:{entry.weight}>"
            if entry.activation:
                act = entry.activation[:40] + "..." if len(entry.activation) > 40 else entry.activation
                line += f" [{act}]"
            previews.append(line)

    if state.random_loras:
        previews.append(f"\nRANDOM (pick {random_count} from {len(state.random_loras)}):")
        for name, entry in state.random_loras.items():
            previews.append(f"  - {name} (w={entry.weight})")

    if base_prompt:
        previews.append(f"\nBASE PROMPT: {base_prompt}")
    if negative_prompt:
        previews.append(f"NEGATIVE: {negative_prompt}")

    return "\n".join(previews)


def _save_session(
    positive_prompt, negative_prompt, steps, sampler, cfg, width, height,
    enable_hr, hr_scale, hr_upscaler, denoising, enable_adetailer,
    random_count, batch_size, batch_count, cooldown, skip_exists,
):
    config["defaults"] = {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "steps": int(steps),
        "sampler": sampler,
        "cfg_scale": float(cfg),
        "width": int(width),
        "height": int(height),
        "batch_size": int(batch_size),
        "batch_count": int(batch_count),
        "random_count": int(random_count),
        "cooldown": int(cooldown),
        "enable_hr": bool(enable_hr),
        "hr_scale": float(hr_scale),
        "hr_upscaler": hr_upscaler,
        "denoising_strength": float(denoising),
        "enable_adetailer": bool(enable_adetailer),
        "skip_exists": bool(skip_exists),
    }
    save_config(config)


def _stop_generation():
    state.should_stop = True
    try:
        from modules import shared
        shared.state.interrupt()
    except Exception:
        pass
    return "Stop signal sent..."


# --- Main generation loop ---

def _run_generation(
    positive_prompt, negative_prompt,
    steps, sampler, cfg, width, height,
    enable_hr, hr_scale, hr_upscaler, denoising,
    enable_adetailer, random_count, batch_size, batch_count,
    cooldown_seconds, skip_exists,
    gen_mode_val="txt2img",
    img2img_image_val=None, img2img_denoising_val=0.75, img2img_resize_mode_val="Just resize",
    enable_controlnet_val=False, control_image_val=None,
    control_preprocessor_val="none", control_model_val="",
    control_weight_val=1.0, control_guidance_start_val=0.0,
    control_guidance_end_val=1.0, control_mode_val="Balanced",
    progress=gr.Progress(),
):
    """Run the generation queue, yielding (log, gallery) after each image."""
    if state.is_running:
        yield "Generation already in progress!", []
        return

    _save_session(
        positive_prompt, negative_prompt, steps, sampler, cfg, width, height,
        enable_hr, hr_scale, hr_upscaler, denoising, enable_adetailer,
        random_count, batch_size, batch_count, cooldown_seconds, skip_exists,
    )

    is_img2img = gen_mode_val == "img2img"
    if is_img2img and img2img_image_val is None:
        yield "img2img mode requires an input image.", []
        return

    resize_mode_map = {"Just resize": 0, "Crop and resize": 1, "Resize and fill": 2}
    resize_mode_int = resize_mode_map.get(img2img_resize_mode_val, 0)

    # ControlNet args
    cn_args = None
    if enable_controlnet_val and control_image_val is not None:
        cn_args = {
            "image": control_image_val,
            "preprocessor": control_preprocessor_val,
            "model": control_model_val,
            "weight": control_weight_val,
            "guidance_start": control_guidance_start_val,
            "guidance_end": control_guidance_end_val,
            "control_mode": control_mode_val,
        }

    # History for frequency weighting and skip-exists
    history = load_history()
    existing_hashes = {r["gen_hash"] for r in history if "gen_hash" in r}
    freq = build_frequency_map(history)

    # Loop items sorted by frequency (least generated first)
    if state.loop_loras:
        loop_items = sorted(state.loop_loras.items(), key=lambda x: freq.get(x[0], 0))
    else:
        loop_items = [(None, None)]

    if not loop_items and not state.always_loras and not state.random_loras:
        yield "No LoRAs configured. Add some to zones first.", []
        return

    num_variants = len(loop_items)
    total_jobs = num_variants * int(batch_count)

    state.is_running = True
    state.should_stop = False
    state.total_jobs = total_jobs
    state.current_job = 0

    output_dir = config.get("output_dir", "generated_images")
    mode_str = "img2img" if is_img2img else "txt2img"
    log_lines = [
        f"Starting {mode_str}: {num_variants} variants x {int(batch_count)} batches "
        f"x {int(batch_size)} per batch = {total_jobs * int(batch_size)} images..."
    ]
    if freq:
        log_lines.append(f"History: {len(history)} previous generations tracked")
    if skip_exists:
        log_lines.append(f"Skip Exists: ON ({len(existing_hashes)} unique combos)")

    if state.loop_loras:
        order_info = [f"{name}({freq.get(name, 0)})" for name, _ in loop_items]
        log_lines.append(f"Loop order (uses): {', '.join(order_info)}")

    generated_images = []
    skipped = 0

    yield "\n".join(log_lines), []

    job_num = 0
    for i, (loop_name, loop_entry) in enumerate(loop_items):
        for batch_idx in range(int(batch_count)):
            if state.should_stop:
                log_lines.append("Generation stopped by user.")
                yield "\n".join(log_lines), list(generated_images)
                break

            job_num += 1
            state.current_job = job_num
            progress(job_num / total_jobs, desc=f"Generating {job_num}/{total_jobs}")

            # Build prompt
            lora_tags = []
            activation_texts = []
            used_lora_names = []

            for name, entry in state.always_loras.items():
                lora_tags.append(f"<lora:{name}:{entry.weight}>")
                used_lora_names.append(name)
                act = get_activation_text(name) or entry.activation
                if act:
                    activation_texts.append(act)

            if loop_name and loop_entry:
                lora_tags.append(f"<lora:{loop_name}:{loop_entry.weight}>")
                used_lora_names.append(loop_name)
                act = get_activation_text(loop_name) or loop_entry.activation
                if act:
                    activation_texts.append(act)

            random_picks_info = []
            if state.random_loras and random_count > 0:
                pool = list(state.random_loras.items())
                pick_count = min(int(random_count), len(pool))
                if freq:
                    max_f = max((freq.get(n, 0) for n, _ in pool), default=0) + 1
                    weights = [max_f - freq.get(n, 0) + 1 for n, _ in pool]
                    picks = weighted_sample(pool, weights, pick_count)
                else:
                    picks = random.sample(pool, pick_count)
                for name, entry in picks:
                    lora_tags.append(f"<lora:{name}:{entry.weight}>")
                    used_lora_names.append(name)
                    act = get_activation_text(name) or entry.activation
                    if act:
                        activation_texts.append(act)
                    random_picks_info.append(f"{name}({freq.get(name, 0)})")

            prompt_parts = lora_tags + activation_texts
            if positive_prompt:
                prompt_parts.append(positive_prompt)
            final_prompt = ", ".join(prompt_parts)

            # Dedup check
            gen_hash = compute_generation_hash(
                final_prompt, negative_prompt, steps, sampler, cfg,
                width, height, enable_hr, hr_scale, hr_upscaler,
                denoising, enable_adetailer, int(batch_size),
            )
            if skip_exists and gen_hash in existing_hashes:
                variant = loop_name or "base"
                log_lines.append(f"\n--- '{variant}' Batch {batch_idx+1} SKIPPED (already generated) ---")
                skipped += 1
                yield "\n".join(log_lines), list(generated_images)
                continue

            # Filename
            name_parts = []
            if loop_name:
                name_parts.append(loop_name)
            if state.always_loras:
                name_parts.append(f"always{len(state.always_loras)}")
            name_parts.append(f"b{batch_idx+1}")
            if not name_parts:
                name_parts.append("image")
            custom_fn = "_".join(name_parts)

            variant = loop_name or "base"
            log_lines.append(f"\n--- [{mode_str}] '{variant}' Batch {batch_idx+1}/{int(batch_count)} ---")
            if random_picks_info:
                log_lines.append(f"Random picks: {', '.join(random_picks_info)}")
            log_lines.append(f"Prompt: {final_prompt[:100]}...")
            yield "\n".join(log_lines), list(generated_images)

            # Generate
            if is_img2img:
                success, msg, filepaths, _ = generation_engine.generate_img2img(
                    init_image=img2img_image_val,
                    prompt=final_prompt,
                    negative_prompt=negative_prompt,
                    steps=int(steps),
                    sampler_name=sampler,
                    cfg_scale=float(cfg),
                    width=int(width),
                    height=int(height),
                    batch_size=int(batch_size),
                    denoising_strength=float(img2img_denoising_val),
                    resize_mode=resize_mode_int,
                    enable_adetailer=bool(enable_adetailer),
                    controlnet_args=cn_args,
                    output_dir=output_dir,
                    custom_filename=custom_fn,
                )
            else:
                success, msg, filepaths, _ = generation_engine.generate_txt2img(
                    prompt=final_prompt,
                    negative_prompt=negative_prompt,
                    steps=int(steps),
                    sampler_name=sampler,
                    cfg_scale=float(cfg),
                    width=int(width),
                    height=int(height),
                    batch_size=int(batch_size),
                    enable_hr=bool(enable_hr),
                    hr_scale=float(hr_scale),
                    hr_upscaler=hr_upscaler,
                    denoising_strength=float(denoising),
                    enable_adetailer=bool(enable_adetailer),
                    controlnet_args=cn_args,
                    output_dir=output_dir,
                    custom_filename=custom_fn,
                )

            log_lines.append(msg)
            if success and filepaths:
                generated_images.extend(filepaths)
                append_history_record({
                    "timestamp": datetime.now().isoformat(),
                    "loras": sorted(used_lora_names),
                    "gen_hash": gen_hash,
                    "prompt_preview": final_prompt[:200],
                    "files": [os.path.basename(f) for f in filepaths],
                })

            yield "\n".join(log_lines), list(generated_images)

            if cooldown_seconds > 0 and job_num < total_jobs and not state.should_stop:
                log_lines.append(f"Cooling down for {cooldown_seconds}s...")
                yield "\n".join(log_lines), list(generated_images)
                time.sleep(int(cooldown_seconds))

        if state.should_stop:
            break

    state.is_running = False
    summary = f"\n=== Complete: {len(generated_images)} images generated"
    if skipped:
        summary += f", {skipped} skipped"
    summary += " ==="
    log_lines.append(summary)
    yield "\n".join(log_lines), list(generated_images)


# --- Build Gradio tab ---

def create_combinator_tab():
    """Create the LoRA Combinator Gradio tab. Returns (tab, title, id)."""
    defaults = config.get("defaults", DEFAULT_CONFIG["defaults"])

    custom_css = """
    .lora-bank-grid { max-height: 400px; overflow-y: auto; }
    .lora-bank-grid > div {
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 4px !important;
    }
    .lora-bank-grid label {
        font-size: 0.85em !important;
        padding: 4px 8px !important;
        white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }
    """

    with gr.Blocks(css=custom_css, analytics_enabled=False) as tab:
        gr.Markdown("## LoRA Combinator")
        gr.Markdown("Zone-based LoRA management for batch generation")

        # --- LoRA Bank ---
        with gr.Accordion("LoRA Bank", open=True):
            with gr.Row():
                refresh_btn = gr.Button("Refresh LoRAs", variant="primary", scale=1)
                scan_status = gr.Textbox(label="Status", interactive=False, scale=2)

            with gr.Row():
                lora_sort = gr.Dropdown(label="Sort", choices=["A-Z", "Z-A"], value="A-Z", scale=1)

            lora_bank = gr.CheckboxGroup(
                label="Available LoRAs",
                choices=[],
                interactive=True,
                elem_classes=["lora-bank-grid"],
            )

            with gr.Row():
                default_weight = gr.Slider(
                    label="Default Weight", minimum=0.1, maximum=2.0, value=0.8, step=0.1, scale=1,
                )
                add_always_btn = gr.Button("Add to Always", variant="secondary")
                add_loop_btn = gr.Button("Add to Loop", variant="secondary")
                add_random_btn = gr.Button("Add to Random", variant="secondary")
                clear_all_btn = gr.Button("Clear All Zones", variant="stop")

        # --- Save/Load Config ---
        with gr.Accordion("Save/Load Zone Config", open=False):
            with gr.Row():
                config_name = gr.Textbox(
                    label="Config Name",
                    value=config.get("last_zone_config", ""),
                    placeholder="my_config",
                    scale=2,
                )
                save_cfg_btn = gr.Button("Save", variant="primary", scale=1)
                load_cfg_btn = gr.Button("Load", variant="secondary", scale=1)
            with gr.Row():
                config_dd = gr.Dropdown(label="Saved Configs", choices=list_saved_configs(), scale=2)
                refresh_cfgs_btn = gr.Button("Refresh List", scale=1)

        # --- Zones ---
        with gr.Row():
            # ALWAYS column
            with gr.Column():
                gr.Markdown("### Always Use")
                gr.Markdown("*Included in every generation*")
                always_display = gr.Textbox(value="(empty)", interactive=False, lines=4, show_label=False)
                with gr.Row():
                    always_dd = gr.Dropdown(label="Adjust weight", choices=[], scale=2)
                    always_slider = gr.Slider(minimum=0.1, maximum=2.0, value=0.8, step=0.1, show_label=False, scale=1)
                with gr.Row():
                    always_rm_name = gr.Textbox(placeholder="LoRA name to remove", show_label=False, scale=2)
                    always_rm_btn = gr.Button("Remove", scale=1)
                clear_always_btn = gr.Button("Clear Always", variant="stop", size="sm")

            # LOOP column
            with gr.Column():
                gr.Markdown("### Loop Through")
                gr.Markdown("*One image per LoRA*")
                loop_display = gr.Textbox(value="(empty)", interactive=False, lines=4, show_label=False)
                with gr.Row():
                    loop_dd = gr.Dropdown(label="Adjust weight", choices=[], scale=2)
                    loop_slider = gr.Slider(minimum=0.1, maximum=2.0, value=0.8, step=0.1, show_label=False, scale=1)
                with gr.Row():
                    loop_rm_name = gr.Textbox(placeholder="LoRA name to remove", show_label=False, scale=2)
                    loop_rm_btn = gr.Button("Remove", scale=1)
                clear_loop_btn = gr.Button("Clear Loop", variant="stop", size="sm")

            # RANDOM column
            with gr.Column():
                gr.Markdown("### Random Pool")
                gr.Markdown("*Pick N random per image*")
                random_display = gr.Textbox(value="(empty)", interactive=False, lines=4, show_label=False)
                random_count = gr.Slider(
                    label="Pick N random", minimum=0, maximum=5,
                    value=defaults.get("random_count", 1), step=1,
                )
                with gr.Row():
                    random_dd = gr.Dropdown(label="Adjust weight", choices=[], scale=2)
                    random_slider = gr.Slider(minimum=0.1, maximum=2.0, value=0.8, step=0.1, show_label=False, scale=1)
                with gr.Row():
                    random_rm_name = gr.Textbox(placeholder="LoRA name to remove", show_label=False, scale=2)
                    random_rm_btn = gr.Button("Remove", scale=1)
                clear_random_btn = gr.Button("Clear Random", variant="stop", size="sm")

        # --- Generation Settings ---
        with gr.Accordion("Generation Settings", open=True):
            gen_mode = gr.Radio(label="Mode", choices=["txt2img", "img2img"], value="txt2img")

            with gr.Group(visible=False) as img2img_controls:
                with gr.Row():
                    img2img_image = gr.Image(label="Input Image", type="pil", scale=2)
                    with gr.Column(scale=1):
                        img2img_denoising = gr.Slider(
                            label="img2img Denoising", minimum=0.0, maximum=1.0, value=0.75, step=0.05,
                        )
                        img2img_resize = gr.Dropdown(
                            label="Resize Mode",
                            choices=["Just resize", "Crop and resize", "Resize and fill"],
                            value="Just resize",
                        )

            with gr.Group() as controlnet_controls:
                enable_controlnet = gr.Checkbox(label="Enable ControlNet", value=False)
                with gr.Row():
                    control_image = gr.Image(label="Control Image", type="pil")
                    control_preprocessor = gr.Dropdown(
                        label="Preprocessor",
                        choices=["none", "canny", "depth", "openpose", "tile", "lineart_anime"],
                        value="lineart_anime",
                    )
                    control_model = gr.Textbox(label="ControlNet Model", placeholder="controlnet-lineart-anime-sdxl-fp16")
                with gr.Row():
                    control_weight = gr.Slider(0.0, 2.0, value=1.0, step=0.05, label="Weight")
                    control_start = gr.Slider(0.0, 1.0, value=0.0, step=0.05, label="Start")
                    control_end = gr.Slider(0.0, 1.0, value=1.0, step=0.05, label="End")
                    control_mode = gr.Dropdown(
                        label="Control Mode",
                        choices=["Balanced", "My prompt is more important", "ControlNet is more important"],
                        value="Balanced",
                    )

            with gr.Row():
                sampler_input = gr.Dropdown(
                    label="Sampler",
                    choices=["Euler a", "Euler", "DPM++ 2M Karras", "DPM++ SDE Karras"],
                    value=defaults.get("sampler", "Euler a"),
                    allow_custom_value=True,
                )
                steps_input = gr.Slider(label="Steps", minimum=1, maximum=150, value=defaults.get("steps", 27), step=1)
                cfg_input = gr.Slider(label="CFG Scale", minimum=1, maximum=30, value=defaults.get("cfg_scale", 6.0), step=0.5)

            with gr.Row():
                batch_size = gr.Slider(
                    label="Batch Size", minimum=1, maximum=8,
                    value=defaults.get("batch_size", 1), step=1, info="Images per batch",
                )
                batch_count = gr.Slider(
                    label="Batch Count", minimum=1, maximum=10,
                    value=defaults.get("batch_count", 1), step=1, info="Batches per variant",
                )

            with gr.Row():
                width_input = gr.Slider(label="Width", minimum=512, maximum=2048, value=defaults.get("width", 1024), step=64)
                swap_btn = gr.Button("Swap", scale=0, min_width=80)
                height_input = gr.Slider(label="Height", minimum=512, maximum=2048, value=defaults.get("height", 1280), step=64)

            with gr.Row():
                gr.Markdown("**Presets:**")
                p1_1 = gr.Button("1:1", scale=0, min_width=60)
                p4_3 = gr.Button("4:3", scale=0, min_width=60)
                p3_4 = gr.Button("3:4", scale=0, min_width=60)
                p5_4 = gr.Button("5:4", scale=0, min_width=60)
                p4_5 = gr.Button("4:5", scale=0, min_width=60)
                p16_9 = gr.Button("16:9", scale=0, min_width=60)
                p9_16 = gr.Button("9:16", scale=0, min_width=60)
                p3_2 = gr.Button("3:2", scale=0, min_width=60)
                p2_3 = gr.Button("2:3", scale=0, min_width=60)

            with gr.Row():
                enable_hr = gr.Checkbox(label="Hires Fix", value=defaults.get("enable_hr", False))
                hr_scale = gr.Slider(label="HR Scale", minimum=1.0, maximum=4.0, value=defaults.get("hr_scale", 1.5), step=0.1)
                hr_upscaler = gr.Dropdown(
                    label="HR Upscaler",
                    choices=["Latent", "Latent (nearest)", "ESRGAN_4x", "R-ESRGAN 4x+"],
                    value=defaults.get("hr_upscaler", "Latent"),
                )
                denoising = gr.Slider(
                    label="Denoising", minimum=0.0, maximum=1.0,
                    value=defaults.get("denoising_strength", 0.5), step=0.05,
                )

            with gr.Row():
                enable_adetailer = gr.Checkbox(label="ADetailer", value=defaults.get("enable_adetailer", False))
                skip_exists = gr.Checkbox(label="Skip Exists", value=defaults.get("skip_exists", False))

            positive_prompt = gr.Textbox(
                label="Base Positive Prompt", value=defaults.get("positive_prompt", ""), lines=2,
            )
            negative_prompt = gr.Textbox(
                label="Negative Prompt", value=defaults.get("negative_prompt", ""), lines=2,
            )

            with gr.Row():
                prompt_cfg_name = gr.Textbox(
                    label="Prompt Config", value=config.get("last_prompt_config", ""),
                    placeholder="my_prompts", scale=2,
                )
                save_prompt_btn = gr.Button("Save Prompts", scale=1)
                load_prompt_btn = gr.Button("Load Prompts", scale=1)
            with gr.Row():
                prompt_cfg_dd = gr.Dropdown(label="Saved Prompt Configs", choices=list_prompt_configs(), scale=2)
                refresh_prompts_btn = gr.Button("Refresh", scale=1)

        # --- Preview ---
        with gr.Accordion("Generation Preview", open=True):
            preview = gr.Textbox(label="What will be generated", interactive=False, lines=8)
            refresh_preview_btn = gr.Button("Refresh Preview")

        # --- Generate ---
        with gr.Row():
            cooldown = gr.Slider(
                label="Cooldown (s)", minimum=0, maximum=120,
                value=defaults.get("cooldown", 0), step=1, scale=2,
            )
            generate_btn = gr.Button("Generate Images", variant="primary", scale=2)
            stop_btn = gr.Button("Stop", variant="stop", scale=1)

        # --- Output ---
        with gr.Row():
            log_output = gr.Textbox(label="Generation Log", interactive=False, lines=12, scale=1)
            gallery = gr.Gallery(
                label="Generated Images", columns=3, height="auto",
                object_fit="contain", allow_preview=True, scale=1,
            )

        # === Wire events ===

        zone_outputs = [
            lora_bank, always_display, loop_display, random_display,
            always_dd, loop_dd, random_dd, scan_status,
        ]

        refresh_btn.click(fn=_refresh_loras, outputs=[scan_status, lora_bank])
        lora_sort.change(fn=_sort_bank, inputs=[lora_sort], outputs=[lora_bank])

        add_always_btn.click(
            fn=lambda s, w: _do_add_to_zone(s, "always", w),
            inputs=[lora_bank, default_weight], outputs=zone_outputs,
        )
        add_loop_btn.click(
            fn=lambda s, w: _do_add_to_zone(s, "loop", w),
            inputs=[lora_bank, default_weight], outputs=zone_outputs,
        )
        add_random_btn.click(
            fn=lambda s, w: _do_add_to_zone(s, "random", w),
            inputs=[lora_bank, default_weight], outputs=zone_outputs,
        )
        clear_all_btn.click(fn=_do_clear_all, outputs=zone_outputs)
        clear_always_btn.click(fn=lambda: _do_clear_zone("always"), outputs=zone_outputs)
        clear_loop_btn.click(fn=lambda: _do_clear_zone("loop"), outputs=zone_outputs)
        clear_random_btn.click(fn=lambda: _do_clear_zone("random"), outputs=zone_outputs)

        always_rm_btn.click(
            fn=lambda n: _do_remove_from_zone("always", n),
            inputs=[always_rm_name], outputs=zone_outputs,
        )
        loop_rm_btn.click(
            fn=lambda n: _do_remove_from_zone("loop", n),
            inputs=[loop_rm_name], outputs=zone_outputs,
        )
        random_rm_btn.click(
            fn=lambda n: _do_remove_from_zone("random", n),
            inputs=[random_rm_name], outputs=zone_outputs,
        )

        # Weight adjustment
        always_dd.change(fn=lambda n: _get_weight_in_zone("always", n), inputs=[always_dd], outputs=[always_slider])
        loop_dd.change(fn=lambda n: _get_weight_in_zone("loop", n), inputs=[loop_dd], outputs=[loop_slider])
        random_dd.change(fn=lambda n: _get_weight_in_zone("random", n), inputs=[random_dd], outputs=[random_slider])

        always_slider.change(fn=lambda n, w: _do_update_weight("always", n, w), inputs=[always_dd, always_slider], outputs=[always_display])
        loop_slider.change(fn=lambda n, w: _do_update_weight("loop", n, w), inputs=[loop_dd, loop_slider], outputs=[loop_display])
        random_slider.change(fn=lambda n, w: _do_update_weight("random", n, w), inputs=[random_dd, random_slider], outputs=[random_display])

        # Config save/load
        save_cfg_btn.click(fn=save_zone_config, inputs=[config_name], outputs=[scan_status])
        load_cfg_btn.click(
            fn=lambda n: load_zone_config(n or ""),
            inputs=[config_name], outputs=[always_display, loop_display, random_display, scan_status],
        )
        config_dd.change(fn=lambda n: n, inputs=[config_dd], outputs=[config_name])
        refresh_cfgs_btn.click(fn=lambda: gr.update(choices=list_saved_configs()), outputs=[config_dd])

        # Prompt config
        save_prompt_btn.click(fn=save_prompt_config, inputs=[prompt_cfg_name, positive_prompt, negative_prompt], outputs=[scan_status])
        load_prompt_btn.click(
            fn=lambda n: load_prompt_config(n or ""),
            inputs=[prompt_cfg_name], outputs=[positive_prompt, negative_prompt, scan_status],
        )
        prompt_cfg_dd.change(fn=lambda n: n, inputs=[prompt_cfg_dd], outputs=[prompt_cfg_name])
        refresh_prompts_btn.click(fn=lambda: gr.update(choices=list_prompt_configs()), outputs=[prompt_cfg_dd])

        # Dimension presets
        swap_btn.click(fn=lambda w, h: (h, w), inputs=[width_input, height_input], outputs=[width_input, height_input])
        p1_1.click(fn=lambda: (1024, 1024), outputs=[width_input, height_input])
        p4_3.click(fn=lambda: (1152, 896), outputs=[width_input, height_input])
        p3_4.click(fn=lambda: (896, 1152), outputs=[width_input, height_input])
        p5_4.click(fn=lambda: (1280, 1024), outputs=[width_input, height_input])
        p4_5.click(fn=lambda: (1024, 1280), outputs=[width_input, height_input])
        p16_9.click(fn=lambda: (1344, 768), outputs=[width_input, height_input])
        p9_16.click(fn=lambda: (768, 1344), outputs=[width_input, height_input])
        p3_2.click(fn=lambda: (1216, 832), outputs=[width_input, height_input])
        p2_3.click(fn=lambda: (832, 1216), outputs=[width_input, height_input])

        # Mode toggle
        gen_mode.change(fn=lambda m: gr.update(visible=(m == "img2img")), inputs=[gen_mode], outputs=[img2img_controls])

        # Preview
        refresh_preview_btn.click(
            fn=_build_preview,
            inputs=[positive_prompt, negative_prompt, random_count, batch_size, batch_count],
            outputs=[preview],
        )

        # Generate
        generate_btn.click(
            fn=_run_generation,
            inputs=[
                positive_prompt, negative_prompt,
                steps_input, sampler_input, cfg_input, width_input, height_input,
                enable_hr, hr_scale, hr_upscaler, denoising,
                enable_adetailer, random_count, batch_size, batch_count,
                cooldown, skip_exists,
                gen_mode, img2img_image, img2img_denoising, img2img_resize,
                enable_controlnet, control_image, control_preprocessor, control_model,
                control_weight, control_start, control_end, control_mode,
            ],
            outputs=[log_output, gallery],
        )

        stop_btn.click(fn=_stop_generation, outputs=[log_output])

    return (tab, "LoRA Combinator", "combinator")
