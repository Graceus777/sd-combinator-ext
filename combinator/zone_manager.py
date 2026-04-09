"""
Zone management for the LoRA Combinator.

Three zones:
  - ALWAYS: LoRAs included in every generation
  - LOOP: One image per LoRA, cycling through each
  - RANDOM: Random weighted selection from pool
"""
import json
import os
import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from combinator.shared import CONFIGS_DIR, PROMPT_CONFIGS_DIR, config, save_config
from combinator.lora_utils import LoRA, get_activation_text


@dataclass
class LoRAEntry:
    """LoRA entry with weight and activation text."""
    weight: float = 1.0
    activation: str = ""


@dataclass
class AppState:
    """Application state for the combinator."""
    all_loras: List[LoRA] = field(default_factory=list)
    bank_loras: List[str] = field(default_factory=list)
    always_loras: Dict[str, LoRAEntry] = field(default_factory=dict)
    loop_loras: Dict[str, LoRAEntry] = field(default_factory=dict)
    random_loras: Dict[str, LoRAEntry] = field(default_factory=dict)
    is_running: bool = False
    should_stop: bool = False
    current_job: int = 0
    total_jobs: int = 0

    def get_lora_by_name(self, name: str) -> Optional[LoRA]:
        for lora in self.all_loras:
            if lora.name == name:
                return lora
        return None


# Module-level singleton
state = AppState()


# --- Zone operations ---

def format_zone(zone_dict: Dict[str, LoRAEntry]) -> str:
    """Format zone contents for display."""
    if not zone_dict:
        return "(empty)"
    lines = []
    for name, entry in zone_dict.items():
        line = f"{name} (w={entry.weight})"
        if entry.activation:
            act_preview = (
                entry.activation[:30] + "..."
                if len(entry.activation) > 30
                else entry.activation
            )
            line += f" [{act_preview}]"
        lines.append(line)
    return "\n".join(lines)


def get_zone_dict(zone: str) -> Optional[Dict[str, LoRAEntry]]:
    """Get the zone dict by name."""
    return {
        "always": state.always_loras,
        "loop": state.loop_loras,
        "random": state.random_loras,
    }.get(zone)


def get_zone_lora_choices(zone: str) -> list:
    """Get list of LoRA names in a zone."""
    zone_dict = get_zone_dict(zone)
    return list(zone_dict.keys()) if zone_dict else []


def add_to_zone(selected: List[str], zone: str, default_weight: float):
    """Move selected LoRAs from bank to a zone. Returns count added."""
    zone_dict = get_zone_dict(zone)
    if zone_dict is None or not selected:
        return 0

    count = 0
    for name in selected:
        if name in state.bank_loras:
            lora = state.get_lora_by_name(name)
            activation = get_activation_text(name) or (lora.prompt if lora else "")
            zone_dict[name] = LoRAEntry(weight=default_weight, activation=activation)
            state.bank_loras.remove(name)
            count += 1
    return count


def remove_from_zone(zone: str, lora_name: str):
    """Remove a LoRA from a zone back to bank."""
    zone_dict = get_zone_dict(zone)
    if zone_dict and lora_name in zone_dict:
        del zone_dict[lora_name]
        state.bank_loras.append(lora_name)
        state.bank_loras.sort()


def clear_zone(zone: str) -> int:
    """Move all LoRAs from a single zone back to bank. Returns count."""
    zone_dict = get_zone_dict(zone)
    if not zone_dict:
        return 0
    count = len(zone_dict)
    for name in list(zone_dict.keys()):
        state.bank_loras.append(name)
    zone_dict.clear()
    state.bank_loras.sort()
    return count


def clear_all_zones() -> int:
    """Move all LoRAs from all zones back to bank. Returns count."""
    count = len(state.always_loras) + len(state.loop_loras) + len(state.random_loras)
    for zone_dict in [state.always_loras, state.loop_loras, state.random_loras]:
        for name in list(zone_dict.keys()):
            state.bank_loras.append(name)
        zone_dict.clear()
    state.bank_loras.sort()
    return count


def update_zone_weight(zone: str, lora_name: str, weight: float):
    """Update the weight of a LoRA in a zone."""
    zone_dict = get_zone_dict(zone)
    if zone_dict and lora_name in zone_dict:
        zone_dict[lora_name].weight = weight


# --- Config save/load ---

def save_zone_config(config_name: str) -> str:
    """Save current zone configuration to a JSON file."""
    if not config_name:
        return "Please enter a config name"

    config_data = {
        "always": {
            name: {"weight": entry.weight, "activation": entry.activation}
            for name, entry in state.always_loras.items()
        },
        "loop": {
            name: {"weight": entry.weight, "activation": entry.activation}
            for name, entry in state.loop_loras.items()
        },
        "random": {
            name: {"weight": entry.weight, "activation": entry.activation}
            for name, entry in state.random_loras.items()
        },
    }

    CONFIGS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = CONFIGS_DIR / f"{config_name}.json"
    with open(filepath, "w") as f:
        json.dump(config_data, f, indent=2)

    return f"Saved LoRA config: {config_name}"


def load_zone_config(config_name: str) -> Tuple[str, str, str, str]:
    """Load zone configuration from a JSON file.
    Returns (always_display, loop_display, random_display, status_msg).
    """
    if not config_name:
        return "(empty)", "(empty)", "(empty)", "Please enter a config name"

    config["last_zone_config"] = config_name
    save_config(config)

    filepath = CONFIGS_DIR / f"{config_name}.json"
    if not filepath.exists():
        return "(empty)", "(empty)", "(empty)", f"Config not found: {config_name}"

    try:
        with open(filepath, "r") as f:
            config_data = json.load(f)

        state.always_loras.clear()
        state.loop_loras.clear()
        state.random_loras.clear()

        for name, data in config_data.get("always", {}).items():
            activation = data.get("activation", "") or get_activation_text(name)
            state.always_loras[name] = LoRAEntry(
                weight=data.get("weight", 1.0), activation=activation
            )
        for name, data in config_data.get("loop", {}).items():
            activation = data.get("activation", "") or get_activation_text(name)
            state.loop_loras[name] = LoRAEntry(
                weight=data.get("weight", 1.0), activation=activation
            )
        for name, data in config_data.get("random", {}).items():
            activation = data.get("activation", "") or get_activation_text(name)
            state.random_loras[name] = LoRAEntry(
                weight=data.get("weight", 1.0), activation=activation
            )

        return (
            format_zone(state.always_loras),
            format_zone(state.loop_loras),
            format_zone(state.random_loras),
            f"Loaded LoRA config: {config_name}",
        )
    except Exception as e:
        return "(empty)", "(empty)", "(empty)", f"Error loading config: {e}"


def list_saved_configs() -> List[str]:
    """List all saved zone config files."""
    if not CONFIGS_DIR.exists():
        return []
    return sorted(
        f.stem for f in CONFIGS_DIR.iterdir()
        if f.suffix == ".json" and f.parent == CONFIGS_DIR
    )


def save_prompt_config(config_name: str, positive: str, negative: str) -> str:
    """Save prompt configuration to a JSON file."""
    if not config_name:
        return "Please enter a config name"
    PROMPT_CONFIGS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = PROMPT_CONFIGS_DIR / f"{config_name}.json"
    with open(filepath, "w") as f:
        json.dump({"positive_prompt": positive, "negative_prompt": negative}, f, indent=2)
    return f"Saved prompt config: {config_name}"


def load_prompt_config(config_name: str) -> Tuple[str, str, str]:
    """Load prompt configuration. Returns (positive, negative, status)."""
    if not config_name:
        return "", "", "Please enter a config name"
    config["last_prompt_config"] = config_name
    save_config(config)
    filepath = PROMPT_CONFIGS_DIR / f"{config_name}.json"
    if not filepath.exists():
        return "", "", f"Config not found: {config_name}"
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        return (
            data.get("positive_prompt", ""),
            data.get("negative_prompt", ""),
            f"Loaded prompt config: {config_name}",
        )
    except Exception as e:
        return "", "", f"Error loading config: {e}"


def list_prompt_configs() -> List[str]:
    """List all saved prompt config files."""
    if not PROMPT_CONFIGS_DIR.exists():
        return []
    return sorted(f.stem for f in PROMPT_CONFIGS_DIR.glob("*.json"))


# --- Weighted sampling ---

def weighted_sample(pool: list, weights: list, k: int) -> list:
    """Weighted random sample without replacement."""
    pool = list(pool)
    weights = list(weights)
    selected = []
    for _ in range(min(k, len(pool))):
        if not pool:
            break
        total = sum(weights)
        if total <= 0:
            idx = random.randint(0, len(pool) - 1)
        else:
            r = random.uniform(0, total)
            cumulative = 0
            idx = 0
            for i, w in enumerate(weights):
                cumulative += w
                if cumulative >= r:
                    idx = i
                    break
        selected.append(pool[idx])
        pool.pop(idx)
        weights.pop(idx)
    return selected
