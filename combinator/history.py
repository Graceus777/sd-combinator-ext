"""
Generation history tracking via JSONL.

Used for:
  - Duplicate detection (skip combos already generated)
  - Frequency-weighted random sampling (least-used LoRAs get priority)
"""
import hashlib
import json
import os
from typing import Dict, List

from combinator.shared import HISTORY_FILE


def load_history() -> List[Dict]:
    """Load generation history from JSONL file."""
    records = []
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        records.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
    return records


def append_history_record(record: Dict):
    """Append a single generation record to history."""
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


def compute_generation_hash(
    prompt: str,
    negative_prompt: str,
    steps: int,
    sampler: str,
    cfg: float,
    width: int,
    height: int,
    enable_hr: bool,
    hr_scale: float,
    hr_upscaler: str,
    denoising: float,
    enable_adetailer: bool,
    batch_size: int,
) -> str:
    """Hash generation parameters for duplicate detection (excludes seed)."""
    key_data = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "steps": int(steps),
        "sampler": sampler,
        "cfg": float(cfg),
        "width": int(width),
        "height": int(height),
        "enable_hr": bool(enable_hr),
        "batch_size": int(batch_size),
        "enable_adetailer": bool(enable_adetailer),
    }
    if enable_hr:
        key_data["hr_scale"] = float(hr_scale)
        key_data["hr_upscaler"] = hr_upscaler
        key_data["denoising"] = float(denoising)
    key_str = json.dumps(key_data, sort_keys=True)
    return hashlib.sha256(key_str.encode()).hexdigest()[:16]


def build_frequency_map(history: List[Dict]) -> Dict[str, int]:
    """Count how many times each LoRA has been used across all history."""
    freq: Dict[str, int] = {}
    for record in history:
        for lora in record.get("loras", []):
            freq[lora] = freq.get(lora, 0) + 1
    return freq
