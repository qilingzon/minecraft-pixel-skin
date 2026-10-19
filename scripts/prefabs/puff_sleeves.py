"""Puff Sleeves Prefab (Reference-Accurate Bare Upper Arm + Floating Puff Shoulder + Bell Cuff)."""

from typing import Tuple, List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANS: Color = (0, 0, 0, 0)

def apply_puff_sleeves(
    builder: SkinBuilder,
    palette: PaletteSpec
) -> SkinBuilder:
    """Apply reference-accurate sleeves: 3D puff shoulder, bare skin mid arm, wine lace bell cuff."""
    cp = palette.cloth_primary        # Rose crimson
    cs = palette.cloth_secondary      # Pink accent
    cd = palette.cloth_shadow         # Deep wine shadow
    w  = (255, 255, 255, 255)         # White lace
    ws = (235, 228, 238, 255)        # Lace soft shadow
    wd = (205, 198, 212, 255)        # Lace deep shadow
    s  = palette.skin                 # Porcelain skin
    sb = palette.skin_blush           # Elbow/blush accent
    t  = TRANS

    # Slim Alex Arm is 3x12x4 (width=3, height=12, depth=4)
    # Top/Bottom: 3x4
    a_top_base = [
        [w,  w,  w ],
        [cp, cp, cp],
        [cp, cd, cp],
        [cd, cd, cd],
    ]
    a_top_outer = [
        [w,  w,  w ],
        [cp, cs, cp],
        [cp, cp, cp],
        [w,  w,  w ],
    ]

    a_bottom_base = [
        [s,  s,  s ],
        [s,  s,  s ],
        [ws, w,  ws],
        [wd, ws, wd],
    ]

    # Front (3x12)
    # Rows 0-2: Puff top & ruffle
    # Rows 3-7: Porcelain bare arm! (Elegant loli skin tone with subtle shadow)
    # Rows 8-10: Bell sleeve & ruffled white lace cuff
    # Row 11: Dainty hand
    a_front_base = [
        [w,  w,  w ],   # row 0: lace shoulder collar
        [cp, cs, cp],   # row 1: puff top
        [w,  w,  w ],   # row 2: puff lower ruffle
        [s,  s,  s ],   # row 3: upper bare arm
        [s,  s,  s ],   # row 4: mid bare arm
        [s,  sb, s ],   # row 5: elbow soft blush
        [s,  s,  s ],   # row 6: lower arm
        [s,  s,  s ],   # row 7: wrist
        [cp, cs, cp],   # row 8: flared bell sleeve top
        [cd, cp, cd],   # row 9: sleeve fold
        [w,  w,  w ],   # row 10: white lace cuff edge
        [s,  s,  s ],   # row 11: delicate hand
    ]

    # Front Outer (3x12) - 3D Volume on Shoulder and Cuff Flare!
    a_front_outer = [
        [w,  w,  w ],   # row 0: 3D lace rim
        [cp, cs, cp],   # row 1: 3D puff volume
        [w,  w,  w ],   # row 2: 3D ruffle
        [t,  t,  t ],   # row 3: bare arm flush
        [t,  t,  t ],   # row 4: flush
        [t,  t,  t ],   # row 5: flush
        [t,  t,  t ],   # row 6: flush
        [t,  t,  t ],   # row 7: flush
        [cp, cs, cp],   # row 8: 3D bell cuff flare
        [cd, cp, cd],   # row 9: 3D bell cuff flare
        [w,  ws, w ],   # row 10: 3D ruffled lace edge
        [t,  t,  t ],   # row 11: hand flush
    ]

    # Back (3x12) Base
    a_back_base = [
        [w,  w,  w ],
        [cp, cd, cp],
        [w,  w,  w ],
        [s,  s,  s ],
        [s,  s,  s ],
        [s,  s,  s ],
        [s,  s,  s ],
        [s,  s,  s ],
        [cd, cp, cd],
        [cd, cd, cd],
        [w,  w,  w ],
        [s,  s,  s ],
    ]

    # Back Outer (3x12)
    a_back_outer = [
        [w,  w,  w ],
        [cp, cd, cp],
        [w,  w,  w ],
        [t,  t,  t ],
        [t,  t,  t ],
        [t,  t,  t ],
        [t,  t,  t ],
        [t,  t,  t ],
        [cd, cp, cd],
        [cd, cd, cd],
        [w,  ws, w ],
        [t,  t,  t ],
    ]

    # Sides (4x12) Base
    a_side_base = [
        [w,  w,  w,  w ],
        [cp, cs, cp, cd],
        [w,  w,  w,  w ],
        [s,  s,  s,  s ],
        [s,  s,  s,  s ],
        [s,  s,  sb, s ],
        [s,  s,  s,  s ],
        [s,  s,  s,  s ],
        [cp, cs, cp, cd],
        [cd, cd, cd, cd],
        [w,  w,  w,  w ],
        [s,  s,  s,  s ],
    ]

    # Sides (4x12) Outer
    a_side_outer = [
        [w,  w,  w,  w ],
        [cp, cs, cp, cd],
        [w,  w,  w,  w ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [cp, cs, cp, cd],
        [cd, cd, cd, cd],
        [w,  ws, ws, w ],
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
