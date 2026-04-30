# sd-combinator-ext

A1111 SD WebUI extension that adds a **LoRA Combinator** tab — zone-based LoRA management and combinatorial batch generation.

---

## Installation

Install via the A1111 WebUI **Extensions → Install from URL** tab:

```
https://github.com/Graceus777/sd-combinator-ext
```

---

## Zones

| Zone | Behavior |
|------|----------|
| **Always Use** | Included in every generation |
| **Loop Through** | One image per LoRA, cycling through each |
| **Random Pool** | Pick N random per image (frequency-weighted toward less-used) |

Activation/trigger text per LoRA is resolved from `lora_texts/{name}.json` or `.txt` first, then falls back to LoRA metadata.

Zone configurations and base prompts can be saved/loaded by name. Generation history is tracked in `generation_history.jsonl` for skip-exists deduplication and least-used random weighting.
