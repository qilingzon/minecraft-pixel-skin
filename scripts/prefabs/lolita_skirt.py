"""Lolita Multi-Layer Dress & Striped Stockings Prefab (3D Volumetric Bell Skirt Outer Layer)."""

from typing import Tuple, List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANS: Color = (0, 0, 0, 0)

def apply_lolita_skirt(
    builder: SkinBuilder,
    palette: PaletteSpec
) -> SkinBuilder:
    """Apply Victorian multi-layer lolita dress: 3D outer skirt on legs and striped stockings."""
    cp = palette.cloth_primary        # Crimson rose #BA2D5C
    cs = palette.cloth_secondary      # Candy pink #E65A88
    cd = palette.cloth_shadow         # Deep wine #7A1838
    c_deep = (112, 22, 56, 255)       # Extra deep shadow

    # Ivory Petticoat / Lace Palette
    w  = (255, 255, 255, 255)         # Crisp white lace
    ws = (235, 228, 238, 255)         # Lace mid shadow
    wd = (205, 198, 212, 255)         # Lace crease shadow

    # Stockings & Shoes (Beatrice Signature Alternating Striped Stockings!)
    # Right Leg: Pink base with Plum stripes / Left Leg: Plum base with Pink stripes
    stk_plum = (82, 36, 76, 255)      # Deep plum purple
    stk_plum_d = (64, 26, 60, 255)
    stk_pink = (236, 92, 138, 255)    # Vibrant candy pink
    stk_pink_d = (208, 72, 116, 255)
    shoe = (192, 44, 82, 255)         # Mary Jane shoe
    shoe_d = (140, 24, 58, 255)
    sole = (88, 18, 42, 255)
    t = TRANS

    # Leg Base Pattern Builder
    def make_leg_base(c1, c1_d, c2, c2_d):
        return [
            [w,    w,    w,    w   ], # row 0: lace garter band
            [c1,   c1_d, c1_d, c1  ], # row 1: stripe 1
            [c1,   c1_d, c1_d, c1  ], # row 2: stripe 1
            [c2,   c2_d, c2_d, c2  ], # row 3: stripe 2
            [c2,   c2_d, c2_d, c2  ], # row 4: stripe 2
            [c1,   c1_d, c1_d, c1  ], # row 5: stripe 3
            [c1,   c1_d, c1_d, c1  ], # row 6: stripe 3
            [c2,   c2_d, c2_d, c2  ], # row 7: stripe 4
            [c2,   c2_d, c2_d, c2  ], # row 8: stripe 4
            [w,    ws,   ws,   w   ], # row 9: white frilled ankle sock
            [shoe, shoe, shoe, shoe], # row 10: Mary Jane shoe body
            [sole, sole, sole, sole], # row 11: shoe sole
        ]

    r_leg_base = make_leg_base(stk_pink, stk_pink_d, stk_plum, stk_plum_d)
    l_leg_base = make_leg_base(stk_plum, stk_plum_d, stk_pink, stk_pink_d)

    for f in ["front", "back", "left", "right"]:
        builder.set_face(f"rightLeg.{f}", "base", r_leg_base)
        builder.set_face(f"leftLeg.{f}", "base", l_leg_base)

    builder.set_face("rightLeg.top", "base", [[stk_pink, stk_pink_d, stk_pink_d, stk_pink] for _ in range(4)])
    builder.set_face("leftLeg.top", "base", [[stk_plum, stk_plum_d, stk_plum_d, stk_plum] for _ in range(4)])
    builder.set_face("rightLeg.bottom", "base", [[sole]*4 for _ in range(4)])
    builder.set_face("leftLeg.bottom", "base", [[sole]*4 for _ in range(4)])

    # 3D Outer Layer Skirt (+0.5px Volume Flare on Legs rows 0-5)
    # Right Leg Front Outer: Right half of the open-V skirt drape
    # Left Leg Front Outer: Left half of the open-V skirt drape
    r_leg_front_outer = [
        [cp, cp, cd, cd], # row 0: skirt top
        [cp, cp, cd, cd], # row 1: drape fold
        [cp, cp, cd, cd], # row 2: drape fold
        [cp, cp, cp, cd], # row 3: skirt flare
        [w,  w,  w,  w ], # row 4: scalloped white lace hem
        [ws, ws, ws, ws], # row 5: lace shadow
        [t,  t,  t,  t ], # row 6: stockings exposed
        [t,  t,  t,  t ], # row 7
        [t,  t,  t,  t ], # row 8
        [w,  w,  w,  w ], # row 9: 3D ruffled sock collar
        [t,  t,  t,  t ], # row 10
        [t,  t,  t,  t ], # row 11
    ]

    l_leg_front_outer = [
        [cd, cd, cp, cp], # row 0: skirt top
        [cd, cd, cp, cp], # row 1: drape fold
        [cd, cd, cp, cp], # row 2: drape fold
        [cd, cp, cp, cp], # row 3: skirt flare
        [w,  w,  w,  w ], # row 4: scalloped white lace hem
        [ws, ws, ws, ws], # row 5: lace shadow
        [t,  t,  t,  t ], # row 6: stockings exposed
        [t,  t,  t,  t ], # row 7
        [t,  t,  t,  t ], # row 8
        [w,  w,  w,  w ], # row 9: 3D ruffled sock collar
        [t,  t,  t,  t ], # row 10
        [t,  t,  t,  t ], # row 11
    ]

    # Outer Skirt Sides & Back (Full Skirt Drape)
    leg_back_outer = [
        [cp, cd, cd, cp],
        [cp, cp, cd, cd],
        [cp, cp, cd, cd],
        [cd, cp, cp, cd],
        [w,  w,  w,  w ],
        [ws, ws, ws, ws],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [w,  w,  w,  w ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
    ]

    leg_side_outer = [
        [cp, cp, cd, cd],
        [cp, cp, cd, cd],
        [cp, cp, cp, cd],
        [cd, cp, cp, cd],
        [w,  w,  w,  w ],
        [ws, ws, ws, ws],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [w,  w,  w,  w ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
    ]

    builder.set_face("rightLeg.front", "outer", r_leg_front_outer)
    builder.set_face("leftLeg.front", "outer", l_leg_front_outer)
    builder.set_face("rightLeg.back", "outer", leg_back_outer)
    builder.set_face("leftLeg.back", "outer", leg_back_outer)
    builder.set_face("rightLeg.right", "outer", leg_side_outer)
    builder.set_face("rightLeg.left", "outer", leg_side_outer)
    builder.set_face("leftLeg.right", "outer", leg_side_outer)
    builder.set_face("leftLeg.left", "outer", leg_side_outer)

    return builder
