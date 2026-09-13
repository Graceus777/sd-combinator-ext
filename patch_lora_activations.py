"""Patch Combinator configs from matching models/Lora JSON or TXT sidecars."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

EXT_DIR = Path(__file__).resolve().parent
ZONES = ("always", "loop", "random")
KEYS = (
    "activation text", "activation_text", "activation", "trigger words",
    "trigger_words", "trigger", "triggers", "trainedwords", "trained_words",
    "ss_trigger_words",
)


def as_text(value: Any) -> str:
    if isinstance(value, str):
        return value.strip(" ,\r\n\t")
    if isinstance(value, list):
        return ", ".join(str(x).strip() for x in value if str(x).strip())
    return ""


def extract_activation(value: Any) -> str:
    """Find common activation fields, including in nested metadata."""
    if isinstance(value, dict):
        folded = {str(k).casefold(): v for k, v in value.items()}
        for key in KEYS:
            text = as_text(folded.get(key.casefold()))
            if text:
                return text
        for child in value.values():
            text = extract_activation(child)
            if text:
                return text
    elif isinstance(value, list):
        for child in value:
            text = extract_activation(child)
            if text:
                return text
    return ""


def read_sidecar(path: Path) -> str:
    try:
        raw = path.read_text(encoding="utf-8-sig")
        return raw.strip(" ,\r\n\t") if path.suffix.casefold() == ".txt" else extract_activation(json.loads(raw))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"WARNING: cannot read {path}: {error}")
        return ""


def index_sidecars(root: Path) -> dict[str, list[Path]]:
    found: dict[str, list[Path]] = {}
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.casefold() in {".json", ".txt"}:
            found.setdefault(path.stem.casefold(), []).append(path)
    for paths in found.values():
        # Prefer a file beside the model, then JSON over TXT.
        paths.sort(key=lambda p: (len(p.relative_to(root).parts), p.suffix.casefold() != ".json"))
    return found


def patch(path: Path, sidecars: dict[str, list[Path]], overwrite: bool, dry_run: bool) -> tuple[int, int]:
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"WARNING: skipping {path}: {error}")
        return 0, 0
    if not isinstance(data, dict) or not any(isinstance(data.get(z), dict) for z in ZONES):
        return 0, 0

    changed = missing = 0
    for zone in ZONES:
        for name, entry in data.get(zone, {}).items():
            if not isinstance(entry, dict) or (entry.get("activation") and not overwrite):
                continue
            activation = ""
            source = None
            for candidate in sidecars.get(str(name).casefold(), []):
                activation = read_sidecar(candidate)
                if activation:
                    source = candidate
                    break
            if activation:
                entry["activation"] = activation
                changed += 1
                print(f"  PATCHED [{zone}] {name} <- {source}")
            else:
                missing += 1
                print(f"  MISSING [{zone}] {name}")

    if changed and not dry_run:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        backup = path.with_name(f"{path.name}.{stamp}.bak")
        shutil.copy2(path, backup)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  BACKUP {backup}")
    return changed, missing


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config-dir", type=Path, default=EXT_DIR / "configs")
    parser.add_argument("--lora-dir", type=Path, default=EXT_DIR.parent.parent / "models" / "Lora")
    parser.add_argument("--overwrite", action="store_true", help="replace existing activation text")
    parser.add_argument("--dry-run", action="store_true", help="show changes without writing")
    args = parser.parse_args()
    if not args.config_dir.is_dir():
        parser.error(f"config directory not found: {args.config_dir}")
    if not args.lora_dir.is_dir():
        parser.error(f"LoRA directory not found: {args.lora_dir}")

    sidecars = index_sidecars(args.lora_dir)
    print(f"Indexed {sum(map(len, sidecars.values()))} sidecars in {args.lora_dir}")
    changed = missing = 0
    for path in sorted(args.config_dir.glob("*.json")):
        file_changed, file_missing = patch(path, sidecars, args.overwrite, args.dry_run)
        if file_changed or file_missing:
            print(f"{path.name}: {file_changed} patched, {file_missing} missing")
        changed += file_changed
        missing += file_missing
    verb = "would patch" if args.dry_run else "patched"
    print(f"Done: {changed} {verb}, {missing} missing sidecars/activation values")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
