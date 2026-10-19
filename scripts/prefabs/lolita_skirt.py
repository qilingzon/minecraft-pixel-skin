"""Lolita Multi-Layer Dress & Striped Stockings Prefab (Zero-Exposed-Skin Architecture)."""

from typing import Tuple, List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANSPARENT: Color = (0, 0, 0, 0)

def apply_lolita_skirt(
    builder: SkinBuilder,
    palette: PaletteSpec
) -> SkinBuilder:
    """Apply complete Victorian multi-layer lolita dress and striped stockings.
    
    Guarantees 100% coverage on torso base: ivory ruffled petticoat fills the
    inverted-V opening so that no skin is exposed on the abdomen or thighs.
    """
    cp = palette.cloth_primary        # Crimson rose
    cs = palette.cloth_secondary      # Candy pink
    ca = palette.cloth_accent         # Gold
    cd = palette.cloth_shadow         # Deep wine shadow
    c_deep = (112, 22, 56, 255)       # Extra deep shadow
    lace_dk = (112, 32, 66, 255)      # Corset border

    # Ivory Petticoat / Lace Palette
    w = (255, 255, 255, 255)          # Crisp white lace
    ws = (238, 232, 242, 255)         # Lace mid shadow
    wd = (212, 204, 220, 255)         # Lace crease shadow
    pw = (254, 250, 242, 255)         # Ivory petticoat highlight
    ps = (235, 226, 215, 255)         # Ivory petticoat shadow
    pd = (208, 196, 182, 255)         # Ivory petticoat deep fold

    # Stockings & Shoes
    stk_p = (80, 35, 75, 255)         # Deep purple-plum
    stk_ps = (62, 26, 58, 255)        # Plum crease shadow
    stk_l = cs                        # Candy pink stripe
    stk_ls = (220, 128, 168, 255)     # Pink stripe shadow
    shoe = (192, 44, 82, 255)         # Mary Jane shoe
    shoe_d = (140, 24, 58, 255)
    sole = (88, 18, 42, 255)

    # 1. Body Top (8x4) Base & Outer
    b_top_base = [
        [w,   ws,  w,   w,   w,   w,   ws,  w  ],
        [ws,  cp,  cp,  cp,  cp,  cp,  cp,  ws ],
        [w,   cp,  cd,  cd,  cd,  cd,  cp,  w  ],
        [ws,  cd,  c_deep, c_deep, c_deep, c_deep, cd, ws ],
    ]
    builder.set_face("body.top", "base", b_top_base)

    # 2. Body Bottom (8x4) Base - Under-skirt petticoat shading (never bare skin!)
    b_bottom_base = [
        [pd,  pd,  pd,  pd,  pd,  pd,  pd,  pd ],
        [pd,  ps,  ps,  ps,  ps,  ps,  pd,  pd ],
        [cd,  cd,  cd,  cd,  cd,  cd,  cd,  cd ],
        [c_deep, c_deep, c_deep, c_deep, c_deep, c_deep, c_deep, c_deep],
    ]
    builder.set_face("body.bottom", "base", b_bottom_base)

    # 3. Body Front (8x12) Base - Corset, Criss-cross Lacing & Tiered Ivory Petticoat
    b_front_base = [
        # Rows 0-1: Neckline and ruffled chemise top
        [w,      w,      w,      ws,     ws,     w,      w,      w     ],
        [cp,     cp,     w,      w,      w,      w,      cp,     cp    ],
        # Rows 2-6: Bodice with Criss-cross pink/white corset lacing
        [cd,     cp,     lace_dk,w,      cs,     lace_dk,cp,     cd    ],
        [cd,     cp,     lace_dk,cs,     w,      lace_dk,cp,     cd    ],
        [cd,     cp,     lace_dk,w,      cs,     lace_dk,cp,     cd    ],
        [cp,     cd,     lace_dk,cs,     w,      lace_dk,cd,     cp    ],
        [cd,     c_deep, lace_dk,w,      cs,     lace_dk,c_deep, cd    ],
        # Row 7: Waistband (White lace trim & ribbon sash)
        [w,      w,      w,      ws,     ws,     w,      cs,     cs    ],
        # Rows 8-11: TIERED IVORY PETTICOAT (ZERO BARE SKIN!)
        [cp,     w,      pw,     ps,     ps,     pw,     w,      cp    ],
        [cp,     w,      ps,     pd,     pd,     ps,     w,      cp    ],
        [cd,     w,      pw,     ps,     ps,     pw,     w,      cd    ],
        [w,      ws,     pw,     pd,     pd,     pw,     ws,     w     ],
    ]
    builder.set_face("body.front", "base", b_front_base)

    # 4. Body Back (8x12) Base - Flowing Crimson Gown & Back Capelet
    b_back_base = [
        [w,      w,      ws,     ws,     ws,     ws,     w,      w     ], # row 0
        [cp,     cp,     cd,     cd,     cd,     cd,     cp,     cp    ], # row 1
        [cd,     cp,     cp,     ca,     ca,     cp,     cp,     cd    ], # row 2: gold buttons
        [cp,     cd,     cd,     ca,     ca,     cd,     cd,     cp    ], # row 3
        [w,      w,      ws,     ws,     ws,     ws,     w,      w     ], # row 4: capelet edge
        [cd,     cp,     cd,     cd,     cd,     cd,     cp,     cd    ], # row 5
        [w,      ws,     w,      w,      w,      w,      ws,     w     ], # row 6: waist sash
        [cp,     cp,     cd,     cd,     cd,     cd,     cp,     cp    ], # row 7
        [cd,     cp,     cp,     cd,     cd,     cp,     cp,     cd    ], # row 8
        [c_deep, cd,     cp,     cp,     cp,     cp,     cd,     c_deep], # row 9
        [cp,     c_deep, cd,     cp,     cp,     cd,     c_deep, cp    ], # row 10
        [cd,     cp,     c_deep, cd,     cd,     c_deep, cp,     cd    ], # row 11
    ]
    builder.set_face("body.back", "base", b_back_base)

    # 5. Body Sides (4x12) Base
    for side in ["right", "left"]:
        b_side_base = [
            [w,      ws,     ws,     w     ], # row 0
            [cp,     cd,     cd,     cp    ], # row 1
            [cd,     cp,     cp,     cd    ], # row 2
            [cp,     cd,     cd,     cp    ], # row 3
            [w,      ws,     ws,     w     ], # row 4
            [cd,     c_deep, c_deep, cd    ], # row 5
            [w,      ws,     ws,     w     ], # row 6: waist
            [cp,     cd,     cd,     cp    ], # row 7
            [cd,     cp,     cp,     cd    ], # row 8
            [c_deep, cd,     cd,     c_deep], # row 9
            [cp,     c_deep, c_deep, cp    ], # row 10
            [cd,     c_deep, c_deep, cd    ], # row 11
        ]
        builder.set_face(f"body.{side}", "base", b_side_base)

    # 6. Legs (4x12) Base - Striped Stockings & Mary Jane Shoes
    leg_face = [
        [w,      w,      w,      w     ], # row 0: lace garter band
        [stk_p,  stk_ps, stk_ps, stk_p ], # row 1: plum stripe
        [stk_p,  stk_ps, stk_ps, stk_p ], # row 2: plum stripe
        [stk_l,  stk_ls, stk_ls, stk_l ], # row 3: candy pink stripe
        [stk_l,  stk_ls, stk_ls, stk_l ], # row 4: candy pink stripe
        [stk_p,  stk_ps, stk_ps, stk_p ], # row 5: plum stripe
        [stk_p,  stk_ps, stk_ps, stk_p ], # row 6: plum stripe
        [stk_l,  stk_ls, stk_ls, stk_l ], # row 7: candy pink stripe
        [stk_l,  stk_ls, stk_ls, stk_l ], # row 8: candy pink stripe
        [w,      ws,     ws,     w     ], # row 9: white frill ankle sock
        [shoe,   shoe,   shoe,   shoe  ], # row 10: Mary Jane shoe body
        [sole,   sole,   sole,   sole  ], # row 11: sole
    ]
    for leg in ["rightLeg", "leftLeg"]:
        for f in ["front", "back", "left", "right"]:
            builder.set_face(f"{leg}.{f}", "base", leg_face)
        # Leg tops & bottoms
        builder.set_face(f"{leg}.top", "base", [[stk_p, stk_ps, stk_ps, stk_p] for _ in range(4)])
        builder.set_face(f"{leg}.bottom", "base", [[sole]*4 for _ in range(4)])

    return builder
