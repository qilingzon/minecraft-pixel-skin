"""Generate Beatrice Skin using MoA Collaborative Pipeline."""

import sys
from pathlib import Path

# Add scripts root
sys.path.insert(0, str(Path(__file__).parent))

from skin_builder import SkinBuilder
from moa.spec_schema import CharacterSpec, PaletteSpec, TopologySpec
from moa.pipeline import MoAPipeline
from prefabs import (
    apply_anime_eyes,
    apply_twintails,
    apply_lolita_skirt,
    apply_puff_sleeves,
    apply_ribbon_sash,
)

def generate_beatrice_moa() -> SkinBuilder:
    """Generate high-fidelity Beatrice skin via MoA pipeline."""
    # 1. Spec Architecting (Gemini)
    palette = PaletteSpec(
        skin=(254, 238, 228, 255),        # #FEEFE4 Pure porcelain
        skin_blush=(252, 212, 204, 255),  # #FCD4CC Soft peach-pink blush
        hair_base=(252, 235, 168, 255),   # #FCEBA8 Warm vanilla blonde
        hair_shadow=(235, 198, 130, 255), # #EBC682 Warm honey shade
        hair_highlight=(255, 247, 195, 255), # #FFF7C3 Luminous cream highlight
        eye_iris_dark=(30, 120, 128, 255), # #1E7880 Deep cyan depth
        eye_iris_light=(45, 172, 175, 255),# #2DACAF Crystal turquoise iris
        eye_lash=(42, 40, 50, 255),       # #2A2832 Deep espresso lash
        eye_sclera=(255, 255, 255, 255),
        cloth_primary=(208, 55, 95, 255), # #D0375F Victorian rose red
        cloth_secondary=(250, 156, 196, 255), # #FA9CC4 Classic Beatrice pink
        cloth_accent=(246, 198, 62, 255), # #F6C63E Gold
        cloth_shadow=(145, 35, 70, 255)   # #912346 Deep rose shadow
    )

    topology = TopologySpec(
        model="slim",
        eye_row=4,
        has_twintails=True,
        has_lolita_skirt=True,
        has_puff_sleeves=True,
        has_ribbon_sash=True,
        negative_rules=[
            "no_mouth_on_chin_row",
            "no_flat_tails_on_body_back",
            "no_bare_skin_on_torso",
            "must_have_puff_sleeves"
        ]
    )

    spec = CharacterSpec(
        name="Beatrice (MoA Edition)",
        version="2.0.0",
        palette=palette,
        topology=topology
    )

    # 2. Pipeline Execution & Closed-Loop Review
    pipeline = MoAPipeline(spec)
    builder, history = pipeline.run_pipeline()

    # Log review rounds
    print(f"MoA Pipeline completed with {len(history)} review rounds.")
    for i, rev in enumerate(history):
        print(f"  Round {i+1}: {rev.status} (Score: {rev.score}) - {rev.summary}")

    return builder

if __name__ == "__main__":
    builder = generate_beatrice_moa()

    # 1. Save in examples/beatrice/
    out_path = Path(__file__).parent.parent / "examples" / "beatrice" / "beatrice_moa_skin.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    builder.save(str(out_path))
    print(f"MoA Beatrice Skin saved to: {out_path}")

    # 2. Save in workspace root
    root_moa = Path(r"D:\deepseek\mc\beatrice_moa_skin.png")
    builder.save(str(root_moa))
    print(f"Saved copy to workspace root: {root_moa}")

    # 3. Synchronize to main beatrice_skin.png
    root_skin = Path(r"D:\deepseek\mc\beatrice_skin.png")
    builder.save(str(root_skin))
    print(f"Synchronized to main deliverable: {root_skin}")

    repo_skin = Path(__file__).parent.parent / "examples" / "beatrice" / "beatrice_skin.png"
    builder.save(str(repo_skin))
    print(f"Synchronized to repo example: {repo_skin}")
