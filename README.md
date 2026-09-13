# sd-combinator-ext

Adds a **LoRA Combinator** tab to Automatic1111 WebUI: zone-based LoRA selection, prompt combinations, txt2img/img2img batches, optional hires, ADetailer and ControlNet.

## Install

In A1111, open **Extensions → Install from URL**, enter the URL below, install, and restart WebUI:

```text
https://github.com/Graceus777/sd-combinator-ext
```

Or clone into `stable-diffusion-webui/extensions/`. This extension uses A1111's Python runtime and internal processing API; it needs no `--api` flag or separate Gradio installation. Choose a checkpoint in A1111 before generating. Install ADetailer/ControlNet and their models separately if using those options.

## First batch

1. Open **LoRA Combinator** and refresh the LoRA bank. Refresh clears the current zone selections; save a configuration first if needed.
2. Assign LoRAs to zones and set weights/activation text.
3. Enter a base positive/negative prompt and any prompt-slot alternatives.
4. Select steps, sampler, CFG, dimensions, seed and batch settings in this tab.
5. Click **Refresh Preview** after editing settings to inspect the resolved prompt combinations. Run a small batch, inspect its PNG Info, then scale up.

| Zone | Behavior |
| --- | --- |
| Always Use | Included in every generation |
| Loop Through | Cycles through individual LoRAs |
| Random Pool | Picks the requested number, weighted toward less-used entries |

The bank supports alphabetical and newest-modified ordering. Activation text resolves from `lora_texts/NAME.json` or `.txt` before the model metadata fallback. Named zone and prompt configurations can be saved and reloaded. Generation history supports skip-exists deduplication and least-used weighting.

## Output and generation settings

Images use A1111's configured txt2img/img2img sample output paths and sample format. They pass through its metadata-aware saver, retaining prompts, seeds and generation infotext. Configure output locations in A1111 Settings. There is no separate Combinator output-directory setting.

The tab reapplies its sampling settings after always-on script setup, so ADetailer/ControlNet initialization does not silently restore the main UI's sampler, steps or seed. Check the effective parameters printed in the console and the generated image's PNG Info.

For img2img, supply an initial image and choose denoising strength. Hires adds a second generation pass. For ControlNet, supply the control image, preprocessor, model, weight and guidance range. **Low VRAM** passes through to the ControlNet unit; availability and memory behavior depend on the installed extension and model.

## Fill missing activation text

The optional helper reads model JSON/TXT sidecars and patches saved zone configurations. It preserves existing activation text unless `--overwrite` is given and backs up each changed JSON file.

From the extension directory:

```powershell
python patch_lora_activations.py --config-dir configs --lora-dir ../../models/Lora --dry-run
python patch_lora_activations.py --config-dir configs --lora-dir ../../models/Lora
```

Inspect the dry-run output first. Use explicit paths when the repository is outside A1111's extensions directory.

## Runtime files and recovery

`config.json`, `configs/`, `lora_texts/` and `generation_history.jsonl` are local runtime data. Preserve them when updating; keep generated images, model files and backups out of Git.

- Missing tab: restart WebUI and inspect its console for import errors. Do not run the extension as a standalone app.
- No images: check A1111's interrupt/skip state and the console's failure reason. The generation path clears stale interrupt flags before a new call.
- Unexpected sampler/steps: inspect the tab's effective parameter log and PNG Info, then check installed always-on script versions.
- Missing triggers: verify filename matching and sidecar content; use the helper's dry run.
- Jobs skipped: inspect skip-exists and history settings before deleting anything. Clearing history also resets frequency weighting.
- GPU failure: stop the batch, preserve completed images and history, and recover A1111 before starting another run.

Offline regression tests use stubs for A1111: install `pytest` and `Pillow` in a separate environment and run `python -m pytest -q`. Live WebUI/GPU checks remain separate.

## Related tools

[combinatorSD](https://github.com/Graceus777/combinatorSD) is the standalone A1111 HTTP client. [comfyui_wrapper](https://github.com/Graceus777/comfyui_wrapper) runs API workflow graphs and editable batches through ComfyUI. [sd-comic-ext](https://github.com/Graceus777/sd-comic-ext) adds scripted comic and movie production.
