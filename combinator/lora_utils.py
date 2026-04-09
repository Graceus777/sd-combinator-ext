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


def discover_loras() -> List[LoRA]:
    """
    Discover available LoRAs from A1111's internal registry.
    Falls back to scanning the lora_texts/ directory if the
    internal registry is unavailable.
    """
    loras = []

    # Try A1111 internal LoRA registry
    try:
        import modules.extra_networks_lora as lora_module
        available = getattr(lora_module, "available_loras", None)
        if available is None:
            # Newer A1111 versions may use a different path
            from modules import sd_models
            import lora as lora_ext
            available = getattr(lora_ext, "available_loras", {})

        for name, lora_on_disk in available.items():
            activation = get_activation_text(name)
            if not activation:
                meta = getattr(lora_on_disk, "metadata", {}) or {}
                activation = extract_activation_from_metadata(meta)
            loras.append(LoRA(
                name=name,
                filepath=getattr(lora_on_disk, "filename", ""),
                weight=1.0,
                prompt=activation,
            ))
    except Exception:
        # Fallback: try the sd-webui Lora extension module
        try:
            from extensions.Lora import lora
            for name, lora_on_disk in lora.available_loras.items():
                activation = get_activation_text(name)
                if not activation:
                    meta = getattr(lora_on_disk, "metadata", {}) or {}
                    activation = extract_activation_from_metadata(meta)
                loras.append(LoRA(
                    name=name,
                    filepath=getattr(lora_on_disk, "filename", ""),
                    weight=1.0,
                    prompt=activation,
                ))
        except Exception:
            pass

    # If internal registry unavailable, discover from lora_texts/ names
    if not loras and LORA_TEXTS_DIR.exists():
        for json_file in LORA_TEXTS_DIR.glob("*.json"):
            name = json_file.stem
            activation = get_activation_text(name)
            loras.append(LoRA(
                name=name,
                filepath="",
                weight=1.0,
                prompt=activation,
            ))

    loras.sort(key=lambda x: x.name.lower())
    return loras


def refresh_lora_registry():
    """Tell A1111 to refresh its LoRA list."""
    try:
        from modules import sd_models
        sd_models.list_models()
    except Exception:
        pass
    try:
        import modules.extra_networks_lora as lora_module
        if hasattr(lora_module, "list_available_loras"):
            lora_module.list_available_loras()
    except Exception:
        pass
