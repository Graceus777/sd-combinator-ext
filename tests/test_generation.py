import sys
from pathlib import Path
from types import SimpleNamespace
import pytest
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from combinator import generation_engine as engine

@pytest.mark.parametrize("img2img", [False, True])
def test_tab_settings_survive_alwayson_setup(monkeypatch, tmp_path, img2img):
    captured = []
    def process(p):
        captured.append(p)
        return SimpleNamespace(images=[Image.new("RGB", (8, 8))])
    def setup(p, is_img2img):
        p.steps, p.sampler_name, p.seed = 20, "wrong sampler", -1
    shared = SimpleNamespace(sd_model=None, state=SimpleNamespace(interrupted=False, skipped=False), opts=SimpleNamespace(outdir_txt2img_samples=str(tmp_path), outdir_txt2img_grids=str(tmp_path), outdir_img2img_samples=str(tmp_path), outdir_img2img_grids=str(tmp_path)))
    processing = SimpleNamespace(StableDiffusionProcessingTxt2Img=lambda **kw: SimpleNamespace(**kw), StableDiffusionProcessingImg2Img=lambda **kw: SimpleNamespace(**kw), process_images=process)
    monkeypatch.setitem(sys.modules, "modules", SimpleNamespace(shared=shared, processing=processing))
    monkeypatch.setattr(engine, "_ensure_scripts_runner", setup)
    monkeypatch.setattr(engine, "_attach_adetailer", lambda p: None)
    monkeypatch.setattr(engine, "_save_images", lambda *args: [str(tmp_path / "sample.png")])
    kwargs = dict(prompt="test", steps=31, sampler_name="Euler a", cfg_scale=4.5, width=640, height=768, seed=42, enable_adetailer=True)
    if img2img:
        result = engine.generate_img2img(init_image=Image.new("RGB", (8, 8)), **kwargs)
    else:
        result = engine.generate_txt2img(**kwargs)
    assert result[0]
    p = captured[0]
    assert (p.steps, p.sampler_name, p.seed, p.cfg_scale, p.width, p.height) == (31, "Euler a", 42, 4.5, 640, 768)
    assert p.do_not_save_samples and p.do_not_save_grid

def test_a1111_saver_receives_metadata_and_output_path(monkeypatch, tmp_path):
    calls = []
    def save_image(image, **kwargs):
        calls.append(kwargs)
        return str(tmp_path / "image.png"), None
    monkeypatch.setitem(sys.modules, "modules", SimpleNamespace(images=SimpleNamespace(save_image=save_image), shared=SimpleNamespace(opts=SimpleNamespace(samples_format="png"))))
    image = Image.new("RGB", (8, 8)); image.info["custom"] = "retained"
    p = SimpleNamespace(outpath_samples=str(tmp_path), prompt="fallback")
    processed = SimpleNamespace(infotexts=["Steps: 31"], all_seeds=[42], all_prompts=["actual"])
    assert len(engine._save_images([image], p, processed, "bad/name")) == 1
    saved = calls[0]
    assert (saved["path"], saved["seed"], saved["prompt"], saved["info"]) == (str(tmp_path), 42, "actual", "Steps: 31")
    assert saved["existing_info"]["custom"] == "retained"
    assert saved["basename"] == "bad_name"
