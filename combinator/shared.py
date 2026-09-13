"""
Shared paths, constants, and configuration for the CombinatorSD extension.
"""
import os
import json
from pathlib import Path

# Extension root: sd-combinator-ext/
EXT_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Data directories
LORA_TEXTS_DIR = EXT_DIR / "lora_texts"
CONFIGS_DIR = EXT_DIR / "configs"
PROMPT_CONFIGS_DIR = CONFIGS_DIR / "prompts"

# Files
CONFIG_FILE = EXT_DIR / "config.json"
HISTORY_FILE = EXT_DIR / "generation_history.jsonl"

# Default configuration
DEFAULT_CONFIG = {
    "last_zone_config": "",
    "last_prompt_config": "",
    "defaults": {
        "positive_prompt": "masterpiece, best quality, sharp focus, highres",
        "negative_prompt": "(low quality, worst quality:1.4)",
        "steps": 27,
        "sampler": "Euler a",
        "cfg_scale": 6.0,
        "width": 1024,
        "height": 1280,
        "batch_size": 1,
        "batch_count": 1,
        "random_count": 1,
        "cooldown": 0,
        "enable_hr": False,
        "hr_scale": 1.5,
        "hr_upscaler": "Latent",
        "denoising_strength": 0.5,
        "enable_adetailer": False,
        "skip_exists": False,
    },
}


def load_config() -> dict:
    """Load extension configuration from file."""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return DEFAULT_CONFIG.copy()


def save_config(config: dict):
    """Save extension configuration to file."""
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


# Module-level config singleton
config = load_config()
