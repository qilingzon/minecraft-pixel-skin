"""Tests for MoA Orchestration Pipeline and Prefabs."""

import sys
from pathlib import Path

# Add scripts root
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from skin_builder import SkinBuilder
from moa.spec_schema import CharacterSpec, PaletteSpec, TopologySpec
from moa.critic_protocol import CriticReview, CriticPatch
from moa.pipeline import MoAPipeline
from prefabs import apply_anime_eyes, apply_twintails, apply_lolita_skirt

def test_prefabs_standalone():
    """Test that all three anime prefabs assemble cleanly onto SkinBuilder."""
    sb = SkinBuilder("slim")
    pal = PaletteSpec()
    apply_anime_eyes(sb, pal)
    apply_twintails(sb, pal)
    apply_lolita_skirt(sb, pal)
    val = sb.validate()
    assert val["passed"] is True, f"Validation failed: {val.get('errors')}"
    print("[TEST PASSED] test_prefabs_standalone")

def test_moa_pipeline_pass():
    """Test that pipeline assembles and passes critic evaluation."""
    pipe = MoAPipeline()
    builder, history = pipe.run_pipeline()
    assert len(history) >= 1
    assert history[-1].status == "PASS"
    assert history[-1].score >= 90
    print(f"[TEST PASSED] test_moa_pipeline_pass (Score: {history[-1].score})")

def test_moa_pipeline_critic_patch():
    """Test that critic identifies defects and coder applies patch."""
    spec = CharacterSpec()
    pipe = MoAPipeline(spec)
    builder = pipe.assemble_base_skin()

    # Intentionally inject chin defect
    box_hf = builder.faces["head.front"]["base"]
    builder.image.putpixel((box_hf[0] + 3, box_hf[1] + 7), (50, 20, 20, 255))

    review = pipe.evaluate_aesthetic_rules(builder)
    assert review.status == "REVISE"
    assert len(review.patches) > 0
    assert "chin" in review.patches[0].reason.lower()

    # Apply patch
    for patch in review.patches:
        pipe.apply_patch(builder, patch)

    # Re-evaluate
    review_after = pipe.evaluate_aesthetic_rules(builder)
    assert review_after.status == "PASS"
    print("[TEST PASSED] test_moa_pipeline_critic_patch (Defect detected and patched successfully)")

if __name__ == "__main__":
    test_prefabs_standalone()
    test_moa_pipeline_pass()
    test_moa_pipeline_critic_patch()
    print("ALL 3 MOA TESTS COMPLETED SUCCESSFULLY!")
