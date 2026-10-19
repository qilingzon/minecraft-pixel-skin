"""Drills Twintails Prefab (Stepped 45-degree 3D Outer-Layer Spirals, Ribbons & Mini Crown)."""

from typing import Tuple, List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANS: Color = (0, 0, 0, 0)

def apply_twintails(
    builder: SkinBuilder,
    palette: PaletteSpec,
    ribbon_color: Optional[Color] = None
) -> SkinBuilder:
    """Apply stepped 45-degree 3D spiral twintails, corner bows, tiara, and head hair volume."""
    hb = palette.hair_base             # Warm vanilla blonde #FCEBA8
    hs = palette.hair_shadow           # Warm honey shade #EBC682
    hh = palette.hair_highlight        # Luminous cream #FFF7C3
    hm = (246, 218, 150, 255)          # Golden peach mid-tone
    hd = (218, 178, 112, 255)          # Deep crease warmth
    s  = palette.skin

    rc_m = ribbon_color or palette.cloth_secondary # Candy pink ribbon
    rc_l = (255, 218, 235, 255)
    rc_d = (220, 118, 162, 255)
    w    = (255, 255, 255, 255)

    gold   = (246, 198, 62, 255)       # Gold tiara
    gold_d = (206, 152, 32, 255)
    ruby   = (198, 35, 75, 255)        # Tiara ruby center

    # 1. Head Top (8x8) Base Hair
    h_top = [
        [hs, hm, hb, hb, hb, hb, hm, hs],
        [hm, hb, hh, hh, hh, hh, hb, hm],
        [hb, hh, hh, hh, hh, hh, hh, hb],
        [hb, hb, hh, hb, hb, hh, hb, hb],
        [hm, hb, hb, hm, hm, hb, hb, hm],
        [hs, hm, hb, hm, hm, hb, hm, hs],
        [hs, hs, hm, hb, hb, hm, hs, hs],
        [hd, hs, hs, hm, hm, hs, hs, hd],
    ]
    builder.set_face("head.top", "base", h_top)

    # 2. Head Bottom (8x8) Base Skin
    builder.set_face("head.bottom", "base", [[s]*8 for _ in range(8)])

    # 3. Head Back (8x8) Base Hair
    h_back_base = [
        [hs, hm, hb, hb, hb, hb, hm, hs],
        [hm, hb, hh, hh, hh, hh, hb, hm],
        [hb, hb, hb, hb, hb, hb, hb, hb],
        [hb, hm, hs, hs, hs, hs, hm, hb],
        [hm, hs, hd, hd, hd, hd, hs, hm],
        [hs, hm, hb, hb, hb, hb, hm, hs],
        [hs, hs, hm, hb, hb, hm, hs, hs],
        [hd, hs, hm, hm, hm, hm, hs, hd],
    ]
    builder.set_face("head.back", "base", h_back_base)

    # 4. Head Top Outer (8x8) - Corner Bows & Beatrice Mini Gold Tiara!
    h_top_o = [
        [rc_m, rc_m, TRANS, TRANS, TRANS, TRANS, rc_m, rc_m], # row 0: ribbon bows
        [rc_l, w,    TRANS, TRANS, TRANS, gold,  gold, rc_l ], # row 1: tiara gold base
        [TRANS, TRANS, TRANS, TRANS, TRANS, gold, ruby,  gold_d], # row 2: ruby gem!
        [TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, gold_d, TRANS], # row 3: tiara tip
        [TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS], # row 4
        [TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS], # row 5
        [hb,   hm,   TRANS, TRANS, TRANS, TRANS, hm,   hb   ], # row 6: 3D hair crown
        [hs,   hb,   TRANS, TRANS, TRANS, TRANS, hb,   hs   ], # row 7
    ]
    builder.set_face("head.top", "outer", h_top_o)

    # 5. Head Right Outer (8x8) - 3D Spiral Drill & Big Ribbon
    r_side = [
        [rc_d, rc_m, rc_l, w,    rc_l, rc_m, rc_d, TRANS], # row 0: ribbon loop
        [rc_m, w,    rc_m, rc_m, rc_m, w,    rc_m, TRANS], # row 1: ribbon bow
        [rc_d, rc_m, rc_d, hb,   hb,   rc_m, rc_d, TRANS], # row 2: ribbon anchor knot
        [TRANS, hb,   hh,   hm,   hs,   hb,   TRANS, TRANS], # row 3: spiral turn 1
        [TRANS, hm,   hs,   hd,   hm,   hb,   TRANS, TRANS], # row 4: spiral turn 1 shadow
        [hb,   hs,   hd,   hb,   hh,   hm,   TRANS, TRANS], # row 5: spiral turn 2
        [hm,   hb,   hh,   hs,   hd,   hs,   TRANS, TRANS], # row 6: spiral turn 2 highlight
        [hs,   hm,   hb,   hb,   hs,   hd,   TRANS, TRANS], # row 7: spiral drill tip
    ]
    builder.set_face("head.right", "outer", r_side)

    # 6. Head Left Outer (8x8) - Mirrored 3D Spiral Drill & Big Ribbon
    l_side = [row[::-1] for row in r_side]
    builder.set_face("head.left", "outer", l_side)

    # 7. Head Back Outer (8x8) - Outer Ribbon Flare & Hair Volume
    h_back_o = [
        [rc_m, rc_d, TRANS, TRANS, TRANS, TRANS, rc_d, rc_m], # row 0: bow tips
        [rc_l, rc_m, TRANS, TRANS, TRANS, TRANS, rc_m, rc_l], # row 1: bow loops
        [hb,   hm,   TRANS, TRANS, TRANS, TRANS, hm,   hb  ], # row 2: anchored hair
        [hm,   hs,   hb,   TRANS, TRANS, hb,   hs,   hm  ], # row 3: volume
        [hs,   hd,   hm,   TRANS, TRANS, hm,   hd,   hs  ], # row 4: cascade
        [hb,   hs,   hb,   TRANS, TRANS, hb,   hs,   hb  ], # row 5: center void so it's not a flat wall
        [hm,   hb,   hs,   hd,   hd,   hs,   hb,   hm  ], # row 6: hair tips
        [hs,   hm,   hb,   hs,   hs,   hb,   hm,   hs  ], # row 7: lower edge
    ]
    builder.set_face("head.back", "outer", h_back_o)

    # 8. Front hair curls falling over shoulders on body.front.outer (cols 1 and 6, rows 2-4)
    box_bfo = builder.faces["body.front"]["outer"]
    builder.image.putpixel((box_bfo[0] + 1, box_bfo[1] + 2), hb)
    builder.image.putpixel((box_bfo[0] + 6, box_bfo[1] + 2), hb)
    builder.image.putpixel((box_bfo[0] + 1, box_bfo[1] + 3), hm)
    builder.image.putpixel((box_bfo[0] + 6, box_bfo[1] + 3), hm)
    builder.image.putpixel((box_bfo[0] + 1, box_bfo[1] + 4), hs)
    builder.image.putpixel((box_bfo[0] + 6, box_bfo[1] + 4), hs)

    return builder
