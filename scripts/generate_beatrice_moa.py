"""Generate Beatrice Skin using MoA Collaborative Pipeline."""

import sys
from pathlib import Path

# Add scripts root
sys.path.insert(0, str(Path(__file__).parent))

from skin_builder import SkinBuilder
from moa.spec_schema import CharacterSpec, PaletteSpec, TopologySpec
from moa.pipeline import MoAPipeline
from prefabs import apply_anime_eyes, apply_twintails, apply_lolita_skirt

def generate_beatrice_moa() -> SkinBuilder:
    # 1. Spec Architecting (Gemini)
    palette = PaletteSpec(
        skin=(255, 238, 227, 255),
        skin_blush=(255, 224, 222, 255),
        hair_base=(252, 235, 168, 255),
        hair_shadow=(235, 210, 135, 255),
        hair_highlight=(255, 248, 205, 255),
        eye_iris_dark=(22, 110, 145, 255),
        eye_iris_light=(45, 205, 220, 255),
        eye_lash=(40, 30, 45, 255),
        eye_sclera=(255, 255, 255, 255),
        cloth_primary=(168, 38, 62, 255),
        cloth_secondary=(245, 185, 205, 255),
        cloth_accent=(235, 195, 65, 255),
        cloth_shadow=(120, 25, 45, 255)
    )

    topology = TopologySpec(
        model="slim",
        eye_row=4,
        has_twintails=True,
        has_lolita_skirt=True,
        negative_rules=["no_mouth_on_chin_row", "no_flat_tails_on_body_back"]
    )

    spec = CharacterSpec(
        name="Beatrice (MoA Edition)",
        version="2.0.0",
        palette=palette,
        topology=topology
    )

    # Pipeline Execution & Closed-Loop Review
    pipeline = MoAPipeline(spec)
    builder, history = pipeline.run_pipeline()

    # Hair crown and front bangs (Outer & Base)
    hb = palette.hair_base
    hh = palette.hair_highlight
    hs = palette.hair_shadow
    s = palette.skin
    b = palette.skin_blush
    t = (0, 0, 0, 0)

    # Fill head top, bottom, sides and back base with hair
    builder.set_face("head.top", "base", [[hb]*8 for _ in range(8)])
    builder.set_face("head.bottom", "base", [[s]*8 for _ in range(8)])
    builder.set_face("head.back", "base", [
        [hb]*8,
        [hh, hb, hb, hh, hh, hb, hb, hh],
        [hb, hb, hb, hb, hb, hb, hb, hb],
        [hb, hs, hs, hb, hb, hs, hs, hb],
        [hb, hb, hs, hs, hs, hs, hb, hb],
        [hs, hb, hb, hb, hb, hb, hb, hs],
        [hs, hs, hb, hb, hb, hb, hs, hs],
        [hb, hb, hs, hs, hs, hs, hb, hb],
    ])
    for s_face in ["head.left", "head.right"]:
        builder.set_face(s_face, "base", [
            [hb]*8,
            [hb, hh, hb, hb, hb, hb, hb, hb],
            [hb, hb, hb, hb, hb, hb, hb, hb],
            [s,  hb, hb, hb, hb, hb, hb, hb],
            [s,  s,  hb, hb, hb, hb, hb, hb],
            [s,  s,  hb, hb, hb, hb, hb, hb],
            [s,  s,  s,  hb, hb, hb, hb, hb],
            [s,  s,  s,  s,  hb, hb, hb, hb],
        ])

    # Head Front Base - blush cheeks
    hf_base = [
        [hb]*8,
        [hb, hh, hb, hb, hh, hb, hb, hb],
        [hb, hb, hb, hb, hb, hb, hb, hb],
        [hb, s,  hb, hb, hb, hb, s,  hb],
        # Eyes handled by prefab (row 4, 5, 6)
        [s, (40,30,45,255), (40,30,45,255), s, s, (40,30,45,255), (40,30,45,255), s],
        [s, (255,255,255,255), (22,110,145,255), s, s, (22,110,145,255), (255,255,255,255), s],
        [s, (255,255,255,255), (45,205,220,255), s, s, (45,205,220,255), (255,255,255,255), s],
        [s, b, s, s, s, s, b, s] # Row 7: subtle porcelain blush at corners, clean chin!
    ]
    builder.set_face("head.front", "base", hf_base)

    # Head Front Outer - Crown & 3D Layered Fringe
    rc = palette.cloth_secondary # pink crown ribbon
    hf_outer = [
        [t,  t,  rc, rc, rc, rc, t,  t],
        [t,  rc, rc, (235,195,65,255), (235,195,65,255), rc, rc, t],
        [hb, hh, hb, hb, hh, hb, hb, hb],
        [hb, hb, t,  t,  t,  t,  hb, hb],
        [hb, t,  t,  t,  t,  t,  t,  hb],
        [hs, t,  t,  t,  t,  t,  t,  hs],
        [t,  t,  t,  t,  t,  t,  t,  t],
        [t,  t,  t,  t,  t,  t,  t,  t]
    ]
    builder.set_face("head.front", "outer", hf_outer)

    # Arms - Puff Sleeves & Cuffs
    w = (255, 255, 255, 255)
    cp = palette.cloth_primary
    cd = palette.cloth_shadow

    arm_3w = [
        [w]*3,
        [cp]*3,
        [cd, cp, cd],
        [cp]*3,
        [w]*3,
        [s]*3,
        [s]*3,
        [s]*3,
        [s]*3,
        [w]*3,
        [s]*3,
        [s]*3
    ]
    arm_4w = [
        [w]*4,
        [cp]*4,
        [cd, cp, cp, cd],
        [cp]*4,
        [w]*4,
        [s]*4,
        [s]*4,
        [s]*4,
        [s]*4,
        [w]*4,
        [s]*4,
        [s]*4
    ]

    for arm in ["rightArm", "leftArm"]:
        builder.set_face(f"{arm}.front", "base", arm_3w)
        builder.set_face(f"{arm}.back", "base", arm_3w)
        builder.set_face(f"{arm}.left", "base", arm_4w)
        builder.set_face(f"{arm}.right", "base", arm_4w)

    return builder

if __name__ == "__main__":
    builder = generate_beatrice_moa()
    out_path = Path(__file__).parent.parent / "examples" / "beatrice" / "beatrice_moa_skin.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    builder.save(str(out_path))
    print(f"MoA Beatrice Skin generated and saved to: {out_path}")

    # Also save to workspace root for user direct access
    root_out = Path(r"D:\deepseek\mc\beatrice_moa_skin.png")
    builder.save(str(root_out))
    print(f"Saved copy to workspace root: {root_out}")
