# sd-combinator-ext

SD WebUI extension with two independent tabs:

- **LoRA Combinator** — zone-based LoRA management and combinatorial batch generation
- **Comic Generator** — script authoring, panel generation, page assembly, and PDF/CBZ export

---

## Installation

Install via the A1111 WebUI **Extensions → Install from URL** tab:

```
https://github.com/Graceus777/sd-combinator-ext
```

Both tabs are enabled by default after install.

---

## Installing only one tab

Create (or edit) `config.json` in the extension root directory to disable a tab:

```json
{
  "enabled_tabs": {
    "combinator": true,
    "comic_generator": false
  }
}
```

Reload the WebUI after saving. The disabled tab will not appear.

---

## Comic Generator — Script Template Wizard

The **Wizard** sub-tab lets you build a ready-to-fill comic script template without writing any JSON.

**Workflow:**

1. Select a character from your `lora_texts/` LoRAs — activation text is pulled automatically
2. Choose a format: **Strip** (3 panels), **Short Story** (7 panels, 2 pages), or **Chapter** (15 panels, 5 pages)
3. Optionally adjust generation params (steps, CFG, size, sampler)
4. Click **Generate Template** — a valid JSON scaffold appears with `[placeholder]` scenes
5. Type your story idea in the **Story idea** box
6. Click **Copy** on the LLM Prompt box → paste it into ChatGPT, Claude, Gemini, or any LLM
7. Paste the LLM's filled JSON back using **Send to Script Editor** (or copy manually into the Comic tab)
8. Click **Generate Panels** in the Comic tab

Free-tier LLMs (ChatGPT 3.5, Claude.ai free) can typically fill 3–5 scripts per session window.

---

## Available page layouts

| Layout | Panels | Description |
|--------|--------|-------------|
| `splash` | 1 | Full-page single panel |
| `two_row` | 2 | Two full-width rows |
| `three_row` | 3 | Three columns in one row |
| `l_right` | 3 | One large left + two small right |
| `l_left` | 3 | Two small left + one large right |
| `grid_2x2` | 4 | 2×2 grid |
| `t_top` | 4 | One wide top + three bottom |
| `t_bottom` | 4 | Three top + one wide bottom |
| `wide_focus` | 1 | Full-width square panel |
| `tall_split` | 2 | Two tall side-by-side columns |
| `staircase` | 3 | Staggered diagonal layout |
| `strip` | n | n panels in a horizontal row |
