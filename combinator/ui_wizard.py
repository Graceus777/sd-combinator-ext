"""
Script Template Wizard — Comic Generator sub-tab.

Workflow:
  1. Pick a primary (and optional secondary) character from lora_texts/
  2. Choose a format: Strip, Short Story, or Chapter
  3. Optionally tune generation params
  4. Click "Generate Template" → get a valid JSON scaffold with placeholders
  5. Copy the auto-assembled LLM prompt → paste into ChatGPT / Claude / Gemini
  6. Paste the filled script back into the Comic sub-tab's Script Editor

No A1111 imports — safe to unit-test standalone.
"""
import json
from typing import Optional

import gradio as gr

from combinator.shared import DEFAULT_CONFIG
from combinator import strip_engine


# ---------------------------------------------------------------------------
# Format definitions
# ---------------------------------------------------------------------------
# Each entry maps to a list of (layout_name, panel_count) pairs — one per page.
# panel_count must match the number of slots returned by assembler.compute_layout.
#
#  splash    → 1 panel  (full-page)
#  two_row   → 2 panels (2 full-width rows)
#  three_row → 3 panels (3 columns, 1 row)
#  l_right   → 3 panels (1 large left + 2 small right)
#  l_left    → 3 panels (2 small left + 1 large right)
#  grid_2x2  → 4 panels (2×2 grid)
#  t_top     → 4 panels (1 wide top + 3 bottom)
#  t_bottom  → 4 panels (3 top + 1 wide bottom)
#  wide_focus→ 1 panel  (full-width square)
# ---------------------------------------------------------------------------

FORMATS = {
    "strip": {
        "label": "Strip  (3 panels · 1 page)",
        "pages": [
            ("three_row", 3),
        ],
    },
    "short": {
        "label": "Short Story  (7 panels · 2 pages)",
        "pages": [
            ("t_top",     4),   # wide establishing shot + 3 panels
            ("three_row", 3),   # 3 panels
        ],
    },
    "chapter": {
        "label": "Chapter  (15 panels · 5 pages)",
        "pages": [
            ("splash",    1),   # full-page opener
            ("l_right",   3),   # big left + 2 small right
            ("grid_2x2",  4),   # 2×2 action grid
            ("t_bottom",  4),   # 3 panels + wide closer
            ("three_row", 3),   # 3-panel finale row
        ],
    },
}

FORMAT_LABELS = {v["label"]: k for k, v in FORMATS.items()}

SAMPLER_CHOICES = ["Euler a", "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM", "UniPC"]

_DEFAULTS = DEFAULT_CONFIG.get("defaults", {})


# ---------------------------------------------------------------------------
# Pure logic helpers (no Gradio imports needed to test these)
# ---------------------------------------------------------------------------

def _list_characters() -> list:
    """Return sorted character key list from lora_texts/."""
    try:
        chars = strip_engine.load_lora_characters()
        return sorted(chars.keys()) if chars else []
    except Exception:
        return []


def _char_activation(char_key: str) -> str:
    """Return activation text string for a character key, or empty string."""
    if not char_key:
        return ""
    try:
        chars = strip_engine.load_lora_characters()
        data = chars.get(char_key, {})
        return data.get("activation", "") or data.get("activation text", "")
    except Exception:
        return ""


def _char_weight(char_key: str) -> float:
    """Return preferred weight for a character key."""
    if not char_key:
        return 0.8
    try:
        chars = strip_engine.load_lora_characters()
        data = chars.get(char_key, {})
        return float(data.get("weight", data.get("preferred weight", 0.8)))
    except Exception:
        return 0.8


def _build_character_block(char_key: str) -> dict:
    return {
        "lora": char_key,
        "activation": _char_activation(char_key),
        "weight": _char_weight(char_key),
    }


def _panel_placeholder(panel_num: int, page_num: int) -> dict:
    pid = f"p{page_num:02d}{panel_num:02d}"
    return {
        "id": pid,
        "scene": f"PANEL {panel_num} — [describe what the camera sees: setting, character action, lighting]",
        "dialogue": "",
        "caption": "",
        "shot": "medium",
    }


def _build_template(
    char1_key: str,
    char2_key: Optional[str],
    format_label: str,
    steps: int,
    cfg: float,
    width: int,
    height: int,
    sampler: str,
    base_positive: str,
    base_negative: str,
) -> str:
    """Return a JSON string of a script template with placeholders."""
    fmt_key = FORMAT_LABELS.get(format_label, "strip")
    fmt = FORMATS[fmt_key]

    # Character block
    if char1_key:
        if char2_key and char2_key != char1_key:
            character = {
                "char1": _build_character_block(char1_key),
                "char2": _build_character_block(char2_key),
            }
            char_field = "characters"
        else:
            character = _build_character_block(char1_key)
            char_field = "character"
    else:
        character = {"lora": "YOUR_LORA_NAME", "activation": "YOUR ACTIVATION TEXT", "weight": 0.8}
        char_field = "character"

    # Generation block
    generation = {
        "steps": int(steps),
        "cfg": float(cfg),
        "width": int(width),
        "height": int(height),
        "sampler": sampler,
        "base_positive": base_positive.strip() or _DEFAULTS.get("positive_prompt", "masterpiece, best quality"),
        "base_negative": base_negative.strip() or _DEFAULTS.get("negative_prompt", "(low quality, worst quality:1.4)"),
    }

    # Pages block
    pages = []
    for page_idx, (layout, panel_count) in enumerate(fmt["pages"], start=1):
        panels = [_panel_placeholder(i + 1, page_idx) for i in range(panel_count)]
        pages.append({"layout": layout, "panels": panels})

    script = {
        "title": "YOUR TITLE HERE",
        char_field: character,
        "generation": generation,
        "pages": pages,
    }
    return json.dumps(script, indent=2, ensure_ascii=False)


def _build_llm_prompt(template_json: str, story_idea: str, char1_key: str) -> str:
    """Return a self-contained copy-paste prompt for any LLM chatbot."""
    activation = _char_activation(char1_key) if char1_key else "your character"
    idea = story_idea.strip() or "[describe your story idea and genre here]"

    header = (
        "You are writing a comic script. Fill in ONLY the scene, dialogue, and caption fields.\n"
        "\n"
        f"CHARACTER: {activation}\n"
        "\n"
        "RULES:\n"
        "• Scenes are visual — describe exactly what the camera sees (pose, location, mood, lighting)\n"
        "• Dialogue goes in speech bubbles — keep each line under 80 characters\n"
        "• Captions are narrator text — short and punchy (under 60 characters)\n"
        "• Set \"dialogue\" or \"caption\" to \"\" for panels that don't need them\n"
        "• Do NOT change any other field (id, shot, layout, lora, generation, etc.)\n"
        "• Return ONLY the completed JSON — no explanations, no markdown fences\n"
        "\n"
        "TEMPLATE:\n"
        f"{template_json}\n"
        "\n"
        f"STORY PROMPT: {idea}"
    )
    return header


# ---------------------------------------------------------------------------
# Gradio UI builder
# ---------------------------------------------------------------------------

def create_wizard_tab_content(script_editor_target):
    """
    Build the Wizard sub-tab UI inside an already-open gr.Tab() context.

    Parameters
    ----------
    script_editor_target : gr.Code
        The script_editor Code component from the Comic sub-tab.
        Used to wire the "Send to Script Editor" button.
    """
    gr.Markdown(
        "Build a template → paste the LLM prompt into ChatGPT or Claude → "
        "paste the filled script back into the **Comic** tab's Script Editor."
    )

    with gr.Row():
        # ── Left column: inputs ────────────────────────────────────────────
        with gr.Column(scale=2):

            gr.Markdown("### Characters")
            with gr.Row():
                refresh_chars_btn = gr.Button("Refresh", size="sm")
            char1_dd = gr.Dropdown(
                label="Primary character",
                choices=_list_characters(),
                interactive=True,
            )
            char1_preview = gr.Markdown(value="", label="Activation text")

            multi_char_cb = gr.Checkbox(label="Add a second character", value=False)
            char2_dd = gr.Dropdown(
                label="Second character",
                choices=_list_characters(),
                interactive=True,
                visible=False,
            )

            gr.Markdown("### Format")
            format_radio = gr.Radio(
                label="Script length",
                choices=[v["label"] for v in FORMATS.values()],
                value=list(FORMATS.values())[0]["label"],
            )

            gr.Markdown("### Generation Settings")
            with gr.Accordion("Params (uses extension defaults if blank)", open=False):
                with gr.Row():
                    steps_sl = gr.Slider(
                        label="Steps", minimum=1, maximum=60, step=1,
                        value=_DEFAULTS.get("steps", 28),
                    )
                    cfg_sl = gr.Slider(
                        label="CFG scale", minimum=1.0, maximum=20.0, step=0.5,
                        value=_DEFAULTS.get("cfg_scale", 7.0),
                    )
                with gr.Row():
                    width_sl = gr.Slider(
                        label="Width", minimum=512, maximum=2048, step=64,
                        value=_DEFAULTS.get("width", 768),
                    )
                    height_sl = gr.Slider(
                        label="Height", minimum=512, maximum=2048, step=64,
                        value=_DEFAULTS.get("height", 1024),
                    )
                sampler_dd = gr.Dropdown(
                    label="Sampler",
                    choices=SAMPLER_CHOICES,
                    value=_DEFAULTS.get("sampler", "Euler a"),
                    interactive=True,
                )
                base_pos = gr.Textbox(
                    label="Base positive prompt",
                    placeholder=_DEFAULTS.get("positive_prompt", "masterpiece, best quality"),
                    lines=2,
                )
                base_neg = gr.Textbox(
                    label="Base negative prompt",
                    placeholder=_DEFAULTS.get("negative_prompt", "(low quality, worst quality:1.4)"),
                    lines=2,
                )
                reset_defaults_btn = gr.Button("Reset to extension defaults", size="sm")

            generate_btn = gr.Button("Generate Template", variant="primary")

        # ── Right column: outputs ──────────────────────────────────────────
        with gr.Column(scale=3):

            gr.Markdown("### Generated Template")
            template_code = gr.Code(
                label="Comic Script JSON",
                language="json",
                lines=22,
                interactive=True,
            )
            with gr.Row():
                send_to_editor_btn = gr.Button("Send to Script Editor", variant="secondary")
                clear_btn = gr.Button("Clear", size="sm")

            gr.Markdown(
                "### LLM Prompt\n"
                "Paste the block below into ChatGPT, Claude, or any LLM. "
                "Free tiers can handle 3–5 scripts per session."
            )
            story_idea = gr.Textbox(
                label="Your story idea / genre",
                placeholder="e.g. a rainy afternoon slice-of-life with some playful banter",
                lines=2,
            )
            llm_prompt_box = gr.Textbox(
                label="LLM Prompt  (copy and paste this entire block)",
                lines=14,
                interactive=False,
                show_copy_button=True,
            )

    # ── Wiring ──────────────────────────────────────────────────────────────

    refresh_chars_btn.click(
        fn=lambda: (gr.update(choices=_list_characters()), gr.update(choices=_list_characters())),
        outputs=[char1_dd, char2_dd],
    )

    char1_dd.change(
        fn=lambda k: f"*{_char_activation(k)}*" if _char_activation(k) else "",
        inputs=[char1_dd],
        outputs=[char1_preview],
    )

    multi_char_cb.change(
        fn=lambda v: gr.update(visible=v),
        inputs=[multi_char_cb],
        outputs=[char2_dd],
    )

    def _reset_defaults():
        return (
            _DEFAULTS.get("steps", 28),
            _DEFAULTS.get("cfg_scale", 7.0),
            _DEFAULTS.get("width", 768),
            _DEFAULTS.get("height", 1024),
            _DEFAULTS.get("sampler", "Euler a"),
            "",  # clear base_pos so placeholder shows
            "",  # clear base_neg so placeholder shows
        )

    reset_defaults_btn.click(
        fn=_reset_defaults,
        outputs=[steps_sl, cfg_sl, width_sl, height_sl, sampler_dd, base_pos, base_neg],
    )

    def _on_generate(char1, char2, fmt, steps, cfg, w, h, sampler, bpos, bneg, idea):
        tmpl = _build_template(char1, char2, fmt, steps, cfg, w, h, sampler, bpos, bneg)
        prompt = _build_llm_prompt(tmpl, idea, char1)
        return tmpl, prompt

    generate_btn.click(
        fn=_on_generate,
        inputs=[
            char1_dd, char2_dd, format_radio,
            steps_sl, cfg_sl, width_sl, height_sl,
            sampler_dd, base_pos, base_neg,
            story_idea,
        ],
        outputs=[template_code, llm_prompt_box],
    )

    # Regenerate LLM prompt live when story_idea changes (template already built)
    story_idea.change(
        fn=lambda tmpl, idea, c1: _build_llm_prompt(tmpl, idea, c1) if tmpl else "",
        inputs=[template_code, story_idea, char1_dd],
        outputs=[llm_prompt_box],
    )

    send_to_editor_btn.click(
        fn=lambda t: t,
        inputs=[template_code],
        outputs=[script_editor_target],
    )

    clear_btn.click(
        fn=lambda: ("", ""),
        outputs=[template_code, llm_prompt_box],
    )
