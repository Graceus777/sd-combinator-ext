import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from patch_lora_activations import patch, index_sidecars

def test_dry_run_preserves_config_and_apply_backs_up(tmp_path):
    loras = tmp_path / "loras"; loras.mkdir()
    (loras / "hero.json").write_text(json.dumps({"activation text": "hero trigger"}), encoding="utf-8")
    config = tmp_path / "zones.json"
    original = json.dumps({"loop": {"hero": {"weight": 0.8}}})
    config.write_text(original, encoding="utf-8")
    index = index_sidecars(loras)
    assert patch(config, index, False, True) == (1, 0)
    assert config.read_text() == original
    assert not list(tmp_path.glob("*.bak"))
    assert patch(config, index, False, False) == (1, 0)
    assert json.loads(config.read_text())["loop"]["hero"]["activation"] == "hero trigger"
    assert list(tmp_path.glob("*.bak"))[0].read_text() == original
    assert patch(config, index, False, False) == (0, 0)
