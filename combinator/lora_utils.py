"""
LoRA discovery and activation text management.

Inside A1111, LoRAs are discovered via the internal registry.
Activation text is resolved from lora_texts/ JSON/TXT files first,
then falls back to LoRA metadata.
"""
import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from combinator.shared import LORA_TEXTS_DIR


@dataclass
class LoRA:
    """Represents a LoRA file."""
    name: str
    filepath: str
    weight: float = 1.0
    prompt: str = ""  # Activation / trigger text

    def to_tag(self) -> str:
        return f"<lora:{self.name}:{self.weight}>"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "filepath": self.filepath,
            "weight": self.weight,
            "prompt": self.prompt,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "LoRA":
        return cls(
            name=data["name"],
            filepath=data.get("filepath", ""),
            weight=data.get("weight", 1.0),
            prompt=data.get("prompt", ""),
        )


def get_activation_text(lora_name: str) -> str:
    """
    Read activation/trigger text from local file.
    Checks lora_texts/{lora_name}.json first, then .txt fallback.
    """
    json_path = LORA_TEXTS_DIR / f"{lora_name}.json"
    if json_path.exists():
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data.get("activation text", "").strip()
        except Exception:
            pass

    txt_path = LORA_TEXTS_DIR / f"{lora_name}.txt"
    if txt_path.exists():
        try:
            return txt_path.read_text(encoding="utf-8").strip()
        except Exception:
            pass
    return ""


def extract_activation_from_metadata(metadata: dict) -> str:
    """Extract activation/trigger words from LoRA metadata dict."""
    if not metadata:
        return ""

    trigger_keys = [
        "ss_trigger_words",
        "trigger",
        "triggers",
        "activation text",
        "activation_text",
    ]
    for key in trigger_keys:
        if key in metadata and metadata[key]:
            val = metadata[key]
            if isinstance(val, list):
                return ", ".join(val)
            return str(val)

    # Fallback: extract from ss_tag_frequency (training tags)
    tag_freq = metadata.get("ss_tag_frequency", {})
    if tag_freq:
        generic_tags = {
            "masterpiece", "best quality", "high quality", "highres",
            "1girl", "1boy", "solo", "looking at viewer", "smile",
            "long hair", "short hair", "breasts", "blush", "simple background",
            "white background", "nude", "nipples", "pussy", "penis",
        }
        all_tags = {}
        for folder, tags in tag_freq.items():
            if isinstance(tags, dict):
                for tag, count in tags.items():
                    if tag.lower() not in generic_tags:
                        all_tags[tag] = all_tags.get(tag, 0) + count
        if all_tags:
            sorted_tags = sorted(all_tags.items(), key=lambda x: x[1], reverse=True)
            top_tags = [t[0] for t in sorted_tags[:7] if t[1] > 6]
            if top_tags:
                return ", ".join(top_tags)
    return ""


def _lora_from_registry_entry(name: str, entry) -> LoRA:
    activation = get_activation_text(name)
    if not activation:
        meta = getattr(entry, "metadata", {}) or {}
        activation = extract_activation_from_metadata(meta)
    return LoRA(
        name=name,
        filepath=getattr(entry, "filename", ""),
        weight=1.0,
        prompt=activation,
    )


def _lora_dir() -> Optional[Path]:
    """Resolve A1111's LoRA directory."""
    try:
        from modules import shared as a1111_shared
        path = getattr(a1111_shared.cmd_opts, "lora_dir", None)
        if path:
            return Path(path)
    except Exception:
        pass
    # Fallback: assume standard A1111 layout (models/Lora next to extensions/)
    # EXT_DIR = .../extensions/sd-combinator-ext  ->  webui root is parents[1]
    try:
        from combinator.shared import EXT_DIR
        webui_root = EXT_DIR.parent.parent
        candidate = webui_root / "models" / "Lora"
        if candidate.exists():
            return candidate
    except Exception:
        pass
    return None


def discover_loras() -> List[LoRA]:
    """
    Discover available LoRAs.

    Priority:
      1. Built-in Lora extension's `networks.available_networks` (modern A1111).
      2. Built-in Lora extension's `lora.available_loras` (legacy).
      3. Direct scan of A1111's lora_dir (no metadata, just filenames).
    """
    loras = []

    # 1. Modern A1111 (1.5+) built-in Lora extension exposes top-level `networks`
    try:
        import networks  # type: ignore
        available = getattr(networks, "available_networks", {}) or {}
        for name, entry in available.items():
            loras.append(_lora_from_registry_entry(name, entry))
    except Exception as e:
        print(f"[combinator] networks.available_networks unavailable: {e}")

    # 2. Legacy: top-level `lora` module
    if not loras:
        try:
            import lora as lora_ext  # type: ignore
            available = getattr(lora_ext, "available_loras", {}) or {}
            for name, entry in available.items():
                loras.append(_lora_from_registry_entry(name, entry))
        except Exception as e:
            print(f"[combinator] lora.available_loras unavailable: {e}")

    # 3. Direct disk scan
    if not loras:
        lora_dir = _lora_dir()
        if lora_dir and lora_dir.exists():
            print(f"[combinator] scanning LoRA dir directly: {lora_dir}")
            for ext in ("*.safetensors", "*.ckpt", "*.pt"):
                for f in lora_dir.rglob(ext):
                    name = f.stem
                    loras.append(LoRA(
                        name=name,
                        filepath=str(f),
                        weight=1.0,
                        prompt=get_activation_text(name),
                    ))
        else:
            print(f"[combinator] no LoRA dir found (resolved: {lora_dir})")

    loras.sort(key=lambda x: x.name.lower())
    print(f"[combinator] discovered {len(loras)} LoRAs")
    return loras


def refresh_lora_registry():
    """Tell A1111 to refresh its LoRA list."""
    try:
        import networks  # type: ignore
        if hasattr(networks, "list_available_networks"):
            networks.list_available_networks()
            return
    except Exception:
        pass
    try:
        import lora as lora_ext  # type: ignore
        if hasattr(lora_ext, "list_available_loras"):
            lora_ext.list_available_loras()
    except Exception:
        pass
