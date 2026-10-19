"""Puff Sleeves Prefab (3D Outer Layer +0.5px Volumetric Sleeves for Alex Slim Model)."""

from typing import Tuple, List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANSPARENT: Color = (0, 0, 0, 0)

def apply_puff_sleeves(
    builder: SkinBuilder,
    palette: PaletteSpec
) -> SkinBuilder:
    """Apply Victorian puff sleeves onto both arms (base + outer 3D layers)."""
    cp = palette.cloth_primary        # Rose crimson
    cs = palette.cloth_secondary      # Pink accent
    cd = palette.cloth_shadow         # Deep wine shadow
    ca = palette.cloth_accent         # Gold
    w = (255, 255, 255, 255)          # White lace
    ws = (235, 230, 240, 255)         # Lace soft shadow
    wd = (210, 205, 218, 255)         # Lace deep shadow
    s = palette.skin                  # Skin
    t = TRANSPARENT

    # Slim Alex Arm is 3x12x4 (width=3, height=12, depth=4)
    # Front/Back are 3x12; Left/Right are 4x12; Top/Bottom are 3x4

    # Arm Top (3x4) Base & Outer
    a_top_base = [
        [w,  ws, w ],
        [cp, cp, cp],
        [cp, cd, cp],
        [cd, cd, cd],
    ]
    a_top_outer = [
        [w,  w,  w ],
        [cp, cp, cp],
        [t,  t,  t ],
        [w,  w,  w ],
    ]

    # Arm Bottom (3x4) Base - Porcelain wrist/palm
    a_bottom_base = [
        [s,  s,  s ],
        [s,  s,  s ],
        [ws, w,  ws],
        [wd, ws, wd],
    ]

    # Arm Front (3x12) Base
    # Rows 0-3: Puff base, Rows 4-8: Mid sleeve, Rows 9-10: Lace cuff, Row 11: Hand
    a_front_base = [
        [w,  ws, w ],   # row 0: lace shoulder rim
        [cp, cp, cp],   # row 1: puff top
        [cp, cd, cp],   # row 2: puff swell
        [w,  w,  w ],   # row 3: lace armband band
        [cd, cp, cd],   # row 4: forearm sleeve
        [cp, cd, cp],   # row 5: forearm sleeve
        [cd, cp, cd],   # row 6: forearm sleeve
        [cp, cd, cd],   # row 7: sleeve fold
        [cd, cd, cd],   # row 8: sleeve taper
        [w,  w,  w ],   # row 9: flared lace cuff
        [ws, wd, ws],   # row 10: cuff shadow
        [s,  s,  s ],   # row 11: dainty hand
    ]

    # Arm Front (3x12) Outer (3D Floating Layer +0.5px)
    a_front_outer = [
        [w,  w,  w ],   # row 0: 3D lace rim
        [cp, cp, cp],   # row 1: 3D puff volume
        [cp, cd, cp],   # row 2: 3D puff volume
        [w,  w,  w ],   # row 3: 3D armband
        [t,  t,  t ],   # row 4: flush
        [t,  t,  t ],   # row 5: flush
        [t,  t,  t ],   # row 6: flush
        [cp, cp, cp],   # row 7: 3D lower bell flare
        [cp, cd, cp],   # row 8: 3D bell flare
        [w,  w,  w ],   # row 9: 3D ruffled cuff flare
        [ws, ws, ws],   # row 10: 3D cuff edge
        [t,  t,  t ],   # row 11: hand exposed
    ]

    # Arm Back (3x12) Base
    a_back_base = [
        [w,  ws, w ],
        [cp, cd, cp],
        [cd, cd, cd],
        [w,  w,  w ],
        [cd, cp, cd],
        [cp, cd, cp],
        [cd, cp, cd],
        [cd, cd, cd],
        [cd, cd, cd],
        [w,  w,  w ],
        [ws, wd, ws],
        [s,  s,  s ],
    ]

    # Arm Back (3x12) Outer
    a_back_outer = [
        [w,  w,  w ],
        [cp, cd, cp],
        [cd, cd, cd],
        [w,  w,  w ],
        [t,  t,  t ],
        [t,  t,  t ],
        [t,  t,  t ],
        [cp, cd, cp],
        [cd, cd, cd],
        [w,  w,  w ],
        [ws, ws, ws],
        [t,  t,  t ],
    ]

    # Arm Sides (4x12) Base
    a_side_base = [
        [w,  ws, ws, w ],
        [cp, cp, cd, cp],
        [cp, cd, cd, cd],
        [w,  w,  w,  w ],
        [cd, cp, cp, cd],
        [cp, cd, cd, cp],
        [cd, cp, cp, cd],
        [cd, cd, cd, cd],
        [cd, cd, cd, cd],
        [w,  w,  w,  w ],
        [ws, wd, wd, ws],
        [s,  s,  s,  s ],
    ]

    # Arm Sides (4x12) Outer
    a_side_outer = [
        [w,  w,  w,  w ],
        [cp, cp, cd, cp],
        [cp, cd, cd, cd],
        [w,  w,  w,  w ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [cp, cp, cd, cp],
        [cp, cd, cd, cd],
        [w,  w,  w,  w ],
        [ws, ws, ws, ws],
        [t,  t,  t,  t ],
    ]

    for arm in ["rightArm", "leftArm"]:
        builder.set_face(f"{arm}.top", "base", a_top_base)
        builder.set_face(f"{arm}.top", "outer", a_top_outer)
        builder.set_face(f"{arm}.bottom", "base", a_bottom_base)
        builder.set_face(f"{arm}.front", "base", a_front_base)
        builder.set_face(f"{arm}.front", "outer", a_front_outer)
        builder.set_face(f"{arm}.back", "base", a_back_base)
        builder.set_face(f"{arm}.back", "outer", a_back_outer)
        for side in ["right", "left"]:
            builder.set_face(f"{arm}.{side}", "base", a_side_base)
            builder.set_face(f"{arm}.{side}", "outer", a_side_outer)

    return builder
