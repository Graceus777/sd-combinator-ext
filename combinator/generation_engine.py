"""
Generation engine using A1111's internal processing.

Replaces the HTTP API client — calls modules.processing directly
for txt2img and img2img, returning PIL Images with no base64 overhead.
"""
import os
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image


def _get_sd_model():
    """Get the currently loaded SD model."""
    from modules import shared
    return shared.sd_model


def _check_interrupted():
    """Check if the user has requested an interrupt."""
    from modules import shared
    return shared.state.interrupted


def _set_job(job_name: str):
    """Set the current job name for A1111's progress display."""
    try:
        from modules import shared
        shared.state.job = job_name
    except Exception:
        pass


def _ensure_scripts_runner(p, is_img2img: bool):
    """
    Wire up A1111's scripts runner on a fresh processing object so alwayson
    scripts (ADetailer, ControlNet, etc.) actually fire. Initializes
    p.script_args to a fully-sized list of per-script defaults — without this,
    enabling one script causes every other alwayson script to read None args
    from its slot and crash.
    """
    from modules import scripts as scripts_module

    runner = scripts_module.scripts_img2img if is_img2img else scripts_module.scripts_txt2img
    p.scripts = runner

    if not runner.alwayson_scripts:
        p.script_args = []
        return

    total = max(s.args_to for s in runner.alwayson_scripts)
    args = [None] * total
    for s in runner.alwayson_scripts:
        # Try a few places the script may have stashed default values.
        defaults = None
        if hasattr(s, "default_args"):
            try:
                defaults = list(s.default_args)
            except Exception:
                defaults = None
        if defaults is None and hasattr(s, "controls") and s.controls:
            defaults = [getattr(c, "value", None) for c in s.controls]
        if defaults is None:
            defaults = [None] * (s.args_to - s.args_from)
        # Ensure correct length
        slot_size = s.args_to - s.args_from
        if len(defaults) < slot_size:
            defaults = defaults + [None] * (slot_size - len(defaults))
        elif len(defaults) > slot_size:
            defaults = defaults[:slot_size]
        args[s.args_from:s.args_to] = defaults

    p.script_args = args


def _find_alwayson_script(p, name_substring: str):
    """Find an alwayson script by case-insensitive title substring."""
    if not getattr(p, "scripts", None):
        return None
    needle = name_substring.lower()
    for s in p.scripts.alwayson_scripts:
        if needle in s.title().lower():
            return s
    return None


def _reset_interrupt_state():
    """Clear A1111 interrupt/skip flags so process_images() doesn't bail."""
    try:
        from modules import shared
        was_interrupted = shared.state.interrupted
        shared.state.interrupted = False
        shared.state.skipped = False
        if hasattr(shared.state, "stopping_generation"):
            shared.state.stopping_generation = False
        if was_interrupted:
            print("[combinator] cleared stale interrupt flag before generation")
    except Exception as e:
        print(f"[combinator] failed to reset interrupt state: {e}")


def generate_txt2img(
    prompt: str,
    negative_prompt: str = "",
    steps: int = 27,
    sampler_name: str = "Euler a",
    cfg_scale: float = 6.0,
    width: int = 1024,
    height: int = 1280,
    seed: int = -1,
    batch_size: int = 1,
    enable_hr: bool = False,
    hr_scale: float = 1.5,
    hr_upscaler: str = "Latent",
    denoising_strength: float = 0.5,
    enable_adetailer: bool = False,
    controlnet_args: Optional[Dict] = None,
    output_dir: str = "generated_images",
    custom_filename: str = "image",
) -> Tuple[bool, str, List[str], List[Image.Image]]:
    """
    Generate images via txt2img using A1111's internal processing.

    Returns:
        (success, message, list_of_saved_filepaths, list_of_pil_images)
    """
    from modules import processing, shared

    _reset_interrupt_state()

    p = processing.StableDiffusionProcessingTxt2Img(
        sd_model=shared.sd_model,
        outpath_samples=shared.opts.outdir_txt2img_samples,
        outpath_grids=shared.opts.outdir_txt2img_grids,
        prompt=prompt,
        negative_prompt=negative_prompt,
        steps=steps,
        sampler_name=sampler_name,
        cfg_scale=cfg_scale,
        width=width,
        height=height,
        seed=seed,
        batch_size=batch_size,
    )

    if enable_hr:
        p.enable_hr = True
        p.hr_scale = hr_scale
        p.hr_upscaler_name = hr_upscaler
        p.denoising_strength = denoising_strength

    if enable_adetailer or controlnet_args:
        _ensure_scripts_runner(p, is_img2img=False)
        if enable_adetailer:
            _attach_adetailer(p)
        if controlnet_args:
            _attach_controlnet(p, controlnet_args)

    try:
        result = processing.process_images(p)
    except Exception as e:
        return False, f"Generation error: {e}", [], []

    if not result.images:
        from modules import shared as _s
        reason = "interrupted" if _s.state.interrupted else ("skipped" if _s.state.skipped else "empty result")
        return False, f"No images generated ({reason})", [], []

    # Save images to disk
    saved_files = _save_images(
        result.images[:batch_size], output_dir, custom_filename
    )

    return (
        True,
        f"Generated {len(saved_files)} image(s)",
        saved_files,
        list(result.images[:batch_size]),
    )


def generate_img2img(
    init_image: Image.Image,
    prompt: str,
    negative_prompt: str = "",
    steps: int = 27,
    sampler_name: str = "Euler a",
    cfg_scale: float = 6.0,
    width: int = 1024,
    height: int = 1280,
    seed: int = -1,
    batch_size: int = 1,
    denoising_strength: float = 0.75,
    resize_mode: int = 0,
    enable_adetailer: bool = False,
    controlnet_args: Optional[Dict] = None,
    output_dir: str = "generated_images",
    custom_filename: str = "img2img",
) -> Tuple[bool, str, List[str], List[Image.Image]]:
    """
    Generate images via img2img using A1111's internal processing.

    Returns:
        (success, message, list_of_saved_filepaths, list_of_pil_images)
    """
    from modules import processing, shared

    _reset_interrupt_state()

    p = processing.StableDiffusionProcessingImg2Img(
        sd_model=shared.sd_model,
        outpath_samples=shared.opts.outdir_img2img_samples,
        outpath_grids=shared.opts.outdir_img2img_grids,
        init_images=[init_image],
        prompt=prompt,
        negative_prompt=negative_prompt,
        steps=steps,
        sampler_name=sampler_name,
        cfg_scale=cfg_scale,
        width=width,
        height=height,
        seed=seed,
        batch_size=batch_size,
        denoising_strength=denoising_strength,
        resize_mode=resize_mode,
    )

    if enable_adetailer or controlnet_args:
        _ensure_scripts_runner(p, is_img2img=True)
        if enable_adetailer:
            _attach_adetailer(p)
        if controlnet_args:
            _attach_controlnet(p, controlnet_args)

    try:
        result = processing.process_images(p)
    except Exception as e:
        return False, f"Generation error: {e}", [], []

    if not result.images:
        from modules import shared as _s
        reason = "interrupted" if _s.state.interrupted else ("skipped" if _s.state.skipped else "empty result")
        return False, f"No images generated ({reason})", [], []

    saved_files = _save_images(
        result.images[:batch_size], output_dir, custom_filename
    )

    return (
        True,
        f"Generated {len(saved_files)} image(s)",
        saved_files,
        list(result.images[:batch_size]),
    )


def interrogate_clip(image: Image.Image) -> Optional[str]:
    """Get CLIP tags for an image using A1111's built-in interrogator."""
    try:
        from modules import shared
        interrogator = shared.interrogator
        caption = interrogator.interrogate(image.convert("RGB"))
        return caption
    except Exception:
        return None


def _attach_adetailer(p):
    """
    Enable ADetailer on the processing object. Assumes _ensure_scripts_runner
    has been called so p.script_args is already a properly sized list with
    sane defaults for every alwayson script.
    """
    script = _find_alwayson_script(p, "adetailer")
    if script is None:
        print("[combinator] ADetailer: not installed; skipping")
        return

    if not isinstance(p.script_args, list):
        # Defensive — caller forgot _ensure_scripts_runner
        p.script_args = list(p.script_args)

    ad_args = {
        "ad_model": "face_yolov8n.pt",
        "ad_mask_k_largest": 1,
        "ad_confidence": 0.3,
        "ad_dilate_erode": 4,
        "ad_mask_blur": 4,
        "ad_denoising_strength": 0.4,
        "ad_inpaint_only_masked": True,
        "ad_inpaint_only_masked_padding": 32,
    }

    args_from = script.args_from
    try:
        # ADetailer arg layout: [enabled, skip_img2img, model_dict_1, model_dict_2, ...]
        p.script_args[args_from] = True       # ad_enable
        p.script_args[args_from + 1] = False  # skip_img2img
        p.script_args[args_from + 2] = ad_args
        print(f"[combinator] ADetailer attached: model={ad_args['ad_model']}")
    except Exception as e:
        print(f"[combinator] ADetailer attach failed: {e}")
        import traceback
        traceback.print_exc()


def _attach_controlnet(p, cn_args: Dict):
    """
    Attach a ControlNet unit to a processing object using sd-webui-controlnet's
    official external_code API. This handles the script_args wiring across
    versions and works for both txt2img and img2img.
    """
    import numpy as np
    from PIL import Image as PILImage

    # Locate sd-webui-controlnet's external_code module. It registers itself
    # under multiple possible names depending on install path.
    external_code = None
    for mod_name in (
        "scripts.external_code",
        "extensions.sd-webui-controlnet.scripts.external_code",
        "extensions-builtin.sd-webui-controlnet.scripts.external_code",
    ):
        try:
            external_code = __import__(mod_name, fromlist=["external_code"])
            break
        except Exception:
            continue
    if external_code is None:
        print("[combinator] ControlNet: sd-webui-controlnet not installed or external_code not importable; skipping")
        return

    image = cn_args.get("image")
    if image is None:
        print("[combinator] ControlNet: no control image provided; skipping")
        return

    # ControlNet expects numpy uint8 RGB.
    if isinstance(image, PILImage.Image):
        image = np.array(image.convert("RGB"))
    elif isinstance(image, dict) and "image" in image:
        # Gradio image-with-mask payload
        img = image["image"]
        if isinstance(img, PILImage.Image):
            img = np.array(img.convert("RGB"))
        image = img

    try:
        unit = external_code.ControlNetUnit(
            enabled=True,
            image=image,
            module=cn_args.get("preprocessor", "none"),
            model=cn_args.get("model", ""),
            weight=float(cn_args.get("weight", 1.0)),
            guidance_start=float(cn_args.get("guidance_start", 0.0)),
            guidance_end=float(cn_args.get("guidance_end", 1.0)),
            pixel_perfect=True,
            control_mode=cn_args.get("control_mode", "Balanced"),
            resize_mode="Crop and Resize",
        )
        external_code.update_cn_script_in_processing(p, [unit])
        print(f"[combinator] ControlNet attached: model={unit.model} module={unit.module} weight={unit.weight}")
    except Exception as e:
        print(f"[combinator] ControlNet attach failed: {e}")
        import traceback
        traceback.print_exc()


def _save_images(
    images: List[Image.Image],
    output_dir: str,
    custom_filename: str,
) -> List[str]:
    """Save PIL images to disk, return list of file paths."""
    os.makedirs(output_dir, exist_ok=True)
    saved = []
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    for idx, img in enumerate(images):
        if len(images) > 1:
            filename = f"{timestamp}_{custom_filename}_{idx + 1}.png"
        else:
            filename = f"{timestamp}_{custom_filename}.png"

        filepath = os.path.abspath(os.path.join(output_dir, filename))
        filepath = filepath.replace("\\", "/")  # Normalize for Gradio
        try:
            img.save(filepath, format="PNG")
            saved.append(filepath)
        except Exception as e:
            print(f"[CombinatorSD] Failed to save image {idx}: {e}")

    return saved
