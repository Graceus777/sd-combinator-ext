"""
Gradio UI for the Comic Generator tab.

Three sub-tabs:
  1. Comic — JSON editor for authored scripts, generate panels, assemble pages
  2. Strip — scenario selection (file or procedural), character pick, batch gen
  3. Assembly — standalone re-assembly from existing images, export PDF/CBZ
"""
import json
import os
import threading
from typing import List, Optional

import gradio as gr

from combinator.shared import EXT_DIR, STRIPS_DIR, LORA_TEXTS_DIR
from combinator import comic_engine
from combinator import strip_engine
from combinator import assembler
from combinator.prompt_builder import validate_camera_continuity


# -- shared state -----------------------------------------------------------

_log_lines: List[str] = []
_generating = False
_lock = threading.Lock()


def _log(msg: str):
    """Thread-safe log append."""
    with _lock:
        _log_lines.append(msg)


def _get_log() -> str:
    with _lock:
        return "\n".join(_log_lines)


def _clear_log():
    with _lock:
        _log_lines.clear()


def _stop():
    """Request interrupt via A1111's shared state."""
    try:
        from modules import shared
        shared.state.interrupted = True
        return "Interrupt requested..."
    except Exception:
        return "Could not send interrupt signal"


# ═══════════════════════════════════════════════════════════════════════════
# COMIC SUB-TAB
# ═══════════════════════════════════════════════════════════════════════════

def _list_script_files() -> List[str]:
    """Find all .json script files in comics/ and configs/ dirs."""
    found = []
    for search_dir in [str(EXT_DIR / "configs"), str(EXT_DIR.parent / "comics")]:
        if not os.path.isdir(search_dir):
            continue
        for root, dirs, files in os.walk(search_dir):
            for f in files:
                if f.endswith(".json") and "script" in f.lower():
                    found.append(os.path.join(root, f))
    return sorted(found)


def _load_script_file(path: str) -> str:
    """Load a script JSON file and return its contents."""
    if not path or not os.path.isfile(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _validate_script(json_str: str) -> str:
    """Validate a comic script JSON and return preview or error."""
    if not json_str.strip():
        return "No script content"
    try:
        script = comic_engine.load_script_from_json(json_str)
    except (json.JSONDecodeError, ValueError) as e:
        return f"**Error:** {e}"
    return comic_engine.preview_script(script, source_label="Editor")


def _generate_comic_panels(
    json_str, output_dir, candidates, cooldown, skip_existing, composite,
    only_panels_str,
):
    """Generate panels from a comic script. Returns (log, gallery)."""
    global _generating
    _clear_log()

    if not json_str.strip():
        return "No script loaded", []

    try:
        script = comic_engine.load_script_from_json(json_str)
    except (json.JSONDecodeError, ValueError) as e:
        return f"Script error: {e}", []

    if not output_dir.strip():
        title = script.get("title", "untitled")
        tag = comic_engine.make_title_tag(title)
        output_dir = os.path.join("comics", tag, "pages")

    only_panels = None
    if only_panels_str and only_panels_str.strip():
        only_panels = set(only_panels_str.strip().split())

    _generating = True
    try:
        result = comic_engine.run_comic_script(
            script=script,
            output_dir=output_dir,
            cooldown=float(cooldown),
            only_panels=only_panels,
            skip_existing=bool(skip_existing),
            composite=bool(composite),
            num_candidates=int(candidates),
            log=_log,
        )
    except Exception as e:
        _log(f"Error: {e}")
        result = {}
    finally:
        _generating = False

    # Collect output images for gallery
    images = []
    if output_dir and os.path.isdir(output_dir):
        for f in sorted(os.listdir(output_dir)):
            if f.lower().endswith(".png") and not f.endswith(("_bg.png", "_char.png", "_mask.png")):
                images.append(os.path.join(output_dir, f))

    return _get_log(), images


def _assemble_comic_pages(json_str, image_dir, page_width):
    """Assemble pages from a comic script + generated images."""
    if not json_str.strip():
        return "No script loaded", []

    try:
        script = comic_engine.load_script_from_json(json_str)
    except (json.JSONDecodeError, ValueError) as e:
        return f"Script error: {e}", []

    title = script.get("title", "untitled")
    tag = comic_engine.make_title_tag(title)

    if not image_dir.strip():
        image_dir = os.path.join("comics", tag, "pages")

    output_dir = os.path.join("comics", tag, "assembled")

    try:
        pages = assembler.assemble_from_script_data(
            script=script,
            image_dirs=[image_dir],
            output_dir=output_dir,
            page_width=int(page_width),
        )
    except Exception as e:
        return f"Assembly error: {e}", []

    return f"Assembled {len(pages)} pages to {output_dir}", pages


# ═══════════════════════════════════════════════════════════════════════════
# STRIP SUB-TAB
# ═══════════════════════════════════════════════════════════════════════════

def _get_scenario_choices():
    """Return combined list of file + procedural scenario names."""
    file_scens = strip_engine.list_file_scenarios()
    proc_settings = strip_engine.list_procedural_settings()
    choices = []
    for s in file_scens:
        choices.append(f"[file] {s}")
    for s in proc_settings:
        choices.append(f"[proc] {s}")
    if not choices:
        choices = ["(none available)"]
    return choices


def _get_character_choices():
    """Return list of available character keys."""
    chars = strip_engine.load_lora_characters()
    return sorted(chars.keys()) if chars else ["(none)"]


def _preview_strip(scenario_choice, char_key):
    """Build a strip script and return preview."""
    if not scenario_choice or scenario_choice.startswith("("):
        return "No scenario selected"

    chars = strip_engine.load_lora_characters()
    if not chars:
        return "No characters found"

    phase1, phase2 = strip_engine.load_scene_loras()

    # Pick character
    if char_key and char_key in chars:
        ck, cd = char_key, chars[char_key]
    else:
        ck, cd = strip_engine.pick_character(chars)

    # Load scenario
    if scenario_choice.startswith("[file] "):
        name = scenario_choice[7:]
        scenario = strip_engine.load_file_scenario(name)
    elif scenario_choice.startswith("[proc] "):
        name = scenario_choice[7:]
        scenario, _ = strip_engine.generate_procedural_scenario(name)
    else:
        return "Invalid scenario selection"

    script = strip_engine.build_strip_script(scenario, ck, cd, phase1, phase2)
    return strip_engine.preview_strip(script)


def _generate_strip(
    scenario_choice, char_key, skip_existing, candidates, cooldown,
):
    """Generate a strip. Returns (log, panel_gallery, page_gallery)."""
    global _generating
    _clear_log()

    if not scenario_choice or scenario_choice.startswith("("):
        return "No scenario selected", [], []

    chars = strip_engine.load_lora_characters()
    if not chars:
        return "No characters found", [], []

    phase1, phase2 = strip_engine.load_scene_loras()

    if char_key and char_key in chars:
        ck, cd = char_key, chars[char_key]
    else:
        ck, cd = strip_engine.pick_character(chars)

    if scenario_choice.startswith("[file] "):
        sname = scenario_choice[7:]
        scenario = strip_engine.load_file_scenario(sname)
    elif scenario_choice.startswith("[proc] "):
        sname = scenario_choice[7:]
        scenario, _ = strip_engine.generate_procedural_scenario(sname)
    else:
        return "Invalid scenario", [], []

    _generating = True
    try:
        result = strip_engine.run_strip(
            scenario_name=sname,
            scenario=scenario,
            char_key=ck,
            char_data=cd,
            phase1=phase1,
            phase2=phase2,
            skip_existing=bool(skip_existing),
            num_candidates=int(candidates),
            cooldown=float(cooldown),
            log=_log,
        )
    except Exception as e:
        _log(f"Error: {e}")
        return _get_log(), [], []
    finally:
        _generating = False

    # Collect panels
    panels = []
    panels_dir = result.get("panels_dir", "")
    if panels_dir and os.path.isdir(panels_dir):
        for f in sorted(os.listdir(panels_dir)):
            if f.lower().endswith(".png") and not f.endswith(("_bg.png", "_char.png", "_mask.png")):
                panels.append(os.path.join(panels_dir, f))

    pages = result.get("pages", [])

    return _get_log(), panels, pages


def _batch_generate_strips(
    count, char_key, setting_choice, skip_existing, candidates, cooldown,
):
    """Generate multiple strips. Returns (log, page_gallery)."""
    global _generating
    _clear_log()

    setting_key = None
    if setting_choice and setting_choice.startswith("[proc] "):
        setting_key = setting_choice[7:]

    char_keys = [char_key] if char_key and char_key != "(none)" else None

    _generating = True
    try:
        results = strip_engine.run_batch_strips(
            count=int(count),
            char_keys=char_keys,
            setting_key=setting_key,
            skip_existing=bool(skip_existing),
            num_candidates=int(candidates),
            cooldown=float(cooldown),
            log=_log,
        )
    except Exception as e:
        _log(f"Error: {e}")
        results = []
    finally:
        _generating = False

    all_pages = []
    for r in results:
        all_pages.extend(r.get("pages", []))

    return _get_log(), all_pages


# ═══════════════════════════════════════════════════════════════════════════
# ASSEMBLY SUB-TAB
# ═══════════════════════════════════════════════════════════════════════════

def _assemble_standalone(script_path, image_dir, output_dir, page_width):
    """Standalone assembly from existing files."""
    if not script_path or not os.path.isfile(script_path):
        return "Script file not found", []

    if not image_dir.strip():
        image_dir = os.path.dirname(script_path)
    if not output_dir.strip():
        output_dir = os.path.join(os.path.dirname(script_path), "assembled")

    try:
        pages = assembler.assemble_from_script(
            script_path=script_path,
            image_dirs=[image_dir],
            output_dir=output_dir,
            page_width=int(page_width),
        )
    except Exception as e:
        return f"Assembly error: {e}", []

    return f"Assembled {len(pages)} pages to {output_dir}", pages


def _export_pdf(page_gallery):
    """Export gallery pages as PDF."""
    if not page_gallery:
        return "No pages to export"
    # page_gallery is list of file paths
    paths = [p if isinstance(p, str) else p["name"] for p in page_gallery]
    if not paths:
        return "No page images found"
    output_dir = os.path.dirname(paths[0])
    tag = "comic_export"
    result = assembler.export_pdf(paths, output_dir, tag)
    return f"PDF exported: {result}" if result else "Export failed"


def _export_cbz(page_gallery):
    """Export gallery pages as CBZ."""
    if not page_gallery:
        return "No pages to export"
    paths = [p if isinstance(p, str) else p["name"] for p in page_gallery]
    if not paths:
        return "No page images found"
    output_dir = os.path.dirname(paths[0])
    tag = "comic_export"
    result = assembler.export_cbz(paths, output_dir, tag)
    return f"CBZ exported: {result}" if result else "Export failed"


# ═══════════════════════════════════════════════════════════════════════════
# MAIN TAB BUILDER
# ═══════════════════════════════════════════════════════════════════════════

def create_comic_tab():
    """Create the Comic Generator tab with Comic/Strip/Assembly sub-tabs."""

    with gr.Blocks(analytics_enabled=False) as tab:
        gr.Markdown("## Comic Generator")

        with gr.Tabs():
            # ── Comic sub-tab ─────────────────────────────────────────
            with gr.Tab("Comic"):
                with gr.Row():
                    with gr.Column(scale=2):
                        gr.Markdown("### Script Editor")
                        script_dd = gr.Dropdown(
                            label="Load script file",
                            choices=_list_script_files(),
                            interactive=True,
                        )
                        refresh_scripts_btn = gr.Button("Refresh", size="sm")
                        script_editor = gr.Code(
                            label="Comic Script JSON",
                            language="json",
                            lines=25,
                        )
                        with gr.Row():
                            validate_btn = gr.Button("Validate & Preview")
                            load_file_btn = gr.Button("Load Selected")
                        preview_md = gr.Markdown(label="Preview", value="")

                    with gr.Column(scale=1):
                        gr.Markdown("### Generation Settings")
                        comic_output_dir = gr.Textbox(
                            label="Output directory",
                            placeholder="Auto from title if empty",
                        )
                        comic_candidates = gr.Slider(
                            label="Candidates per panel", minimum=1, maximum=5,
                            step=1, value=1,
                        )
                        comic_cooldown = gr.Slider(
                            label="Cooldown (sec)", minimum=0, maximum=10,
                            step=0.5, value=2.0,
                        )
                        comic_skip = gr.Checkbox(label="Skip existing panels", value=True)
                        comic_composite = gr.Checkbox(label="Composite mode", value=False)
                        comic_only = gr.Textbox(
                            label="Only panels (space-separated IDs)",
                            placeholder="e.g. p001 p002 p003",
                        )
                        with gr.Row():
                            gen_panels_btn = gr.Button("Generate Panels", variant="primary")
                            assemble_btn = gr.Button("Assemble Pages")
                            stop_comic_btn = gr.Button("Stop", variant="stop")

                        comic_page_width = gr.Slider(
                            label="Page width (px)", minimum=1200, maximum=4800,
                            step=100, value=2400,
                        )

                comic_log = gr.Textbox(label="Log", lines=12, interactive=False)
                with gr.Row():
                    comic_panel_gallery = gr.Gallery(label="Generated Panels", columns=4, height=400)
                    comic_page_gallery = gr.Gallery(label="Assembled Pages", columns=2, height=400)

                # Wiring
                refresh_scripts_btn.click(
                    fn=lambda: gr.update(choices=_list_script_files()),
                    outputs=[script_dd],
                )
                load_file_btn.click(
                    fn=_load_script_file,
                    inputs=[script_dd],
                    outputs=[script_editor],
                )
                script_dd.change(
                    fn=_load_script_file,
                    inputs=[script_dd],
                    outputs=[script_editor],
                )
                validate_btn.click(
                    fn=_validate_script,
                    inputs=[script_editor],
                    outputs=[preview_md],
                )
                gen_panels_btn.click(
                    fn=_generate_comic_panels,
                    inputs=[
                        script_editor, comic_output_dir, comic_candidates,
                        comic_cooldown, comic_skip, comic_composite, comic_only,
                    ],
                    outputs=[comic_log, comic_panel_gallery],
                )
                assemble_btn.click(
                    fn=_assemble_comic_pages,
                    inputs=[script_editor, comic_output_dir, comic_page_width],
                    outputs=[comic_log, comic_page_gallery],
                )
                stop_comic_btn.click(fn=_stop, outputs=[comic_log])

            # ── Strip sub-tab ─────────────────────────────────────────
            with gr.Tab("Strip"):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### Scenario")
                        scenario_dd = gr.Dropdown(
                            label="Scenario",
                            choices=_get_scenario_choices(),
                            interactive=True,
                        )
                        refresh_scenarios_btn = gr.Button("Refresh", size="sm")
                        char_dd = gr.Dropdown(
                            label="Character",
                            choices=_get_character_choices(),
                            interactive=True,
                        )
                        refresh_chars_btn = gr.Button("Refresh Characters", size="sm")

                        gr.Markdown("### Settings")
                        strip_skip = gr.Checkbox(label="Skip existing", value=True)
                        strip_candidates = gr.Slider(
                            label="Candidates", minimum=1, maximum=5,
                            step=1, value=1,
                        )
                        strip_cooldown = gr.Slider(
                            label="Cooldown (sec)", minimum=0, maximum=10,
                            step=0.5, value=2.0,
                        )

                        with gr.Row():
                            preview_strip_btn = gr.Button("Preview")
                            gen_strip_btn = gr.Button("Generate", variant="primary")
                            stop_strip_btn = gr.Button("Stop", variant="stop")

                        gr.Markdown("### Batch")
                        batch_count = gr.Slider(
                            label="Strip count", minimum=1, maximum=20,
                            step=1, value=3,
                        )
                        batch_gen_btn = gr.Button("Batch Generate")

                    with gr.Column(scale=2):
                        strip_preview_md = gr.Markdown(label="Preview", value="")
                        strip_log = gr.Textbox(label="Log", lines=12, interactive=False)
                        with gr.Row():
                            strip_panel_gallery = gr.Gallery(label="Panels", columns=4, height=350)
                            strip_page_gallery = gr.Gallery(label="Pages", columns=2, height=350)

                # Wiring
                refresh_scenarios_btn.click(
                    fn=lambda: gr.update(choices=_get_scenario_choices()),
                    outputs=[scenario_dd],
                )
                refresh_chars_btn.click(
                    fn=lambda: gr.update(choices=_get_character_choices()),
                    outputs=[char_dd],
                )
                preview_strip_btn.click(
                    fn=_preview_strip,
                    inputs=[scenario_dd, char_dd],
                    outputs=[strip_preview_md],
                )
                gen_strip_btn.click(
                    fn=_generate_strip,
                    inputs=[
                        scenario_dd, char_dd, strip_skip,
                        strip_candidates, strip_cooldown,
                    ],
                    outputs=[strip_log, strip_panel_gallery, strip_page_gallery],
                )
                stop_strip_btn.click(fn=_stop, outputs=[strip_log])
                batch_gen_btn.click(
                    fn=_batch_generate_strips,
                    inputs=[
                        batch_count, char_dd, scenario_dd,
                        strip_skip, strip_candidates, strip_cooldown,
                    ],
                    outputs=[strip_log, strip_page_gallery],
                )

            # ── Wizard sub-tab ────────────────────────────────────────
            with gr.Tab("Wizard"):
                from combinator.ui_wizard import create_wizard_tab_content
                create_wizard_tab_content(script_editor_target=script_editor)

            # ── Assembly sub-tab ──────────────────────────────────────
            with gr.Tab("Assembly"):
                with gr.Row():
                    with gr.Column():
                        gr.Markdown("### Standalone Assembly")
                        gr.Markdown("Re-assemble pages from existing script + images without regenerating.")
                        asm_script = gr.Textbox(
                            label="Script JSON path",
                            placeholder="path/to/script.json",
                        )
                        asm_images = gr.Textbox(
                            label="Image directory",
                            placeholder="Auto from script dir if empty",
                        )
                        asm_output = gr.Textbox(
                            label="Output directory",
                            placeholder="Auto: {script_dir}/assembled/",
                        )
                        asm_width = gr.Slider(
                            label="Page width (px)", minimum=1200, maximum=4800,
                            step=100, value=2400,
                        )
                        with gr.Row():
                            asm_btn = gr.Button("Assemble", variant="primary")
                            pdf_btn = gr.Button("Export PDF")
                            cbz_btn = gr.Button("Export CBZ")

                    with gr.Column():
                        asm_log = gr.Textbox(label="Status", lines=4, interactive=False)
                        asm_gallery = gr.Gallery(label="Assembled Pages", columns=2, height=500)

                # Wiring
                asm_btn.click(
                    fn=_assemble_standalone,
                    inputs=[asm_script, asm_images, asm_output, asm_width],
                    outputs=[asm_log, asm_gallery],
                )
                pdf_btn.click(fn=_export_pdf, inputs=[asm_gallery], outputs=[asm_log])
                cbz_btn.click(fn=_export_cbz, inputs=[asm_gallery], outputs=[asm_log])

    return (tab, "Comic Generator", "comic_generator")
