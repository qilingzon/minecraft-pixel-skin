"""Drills Twintails Prefab (Stepped 45-degree 3D Outer-Layer Spirals for Anime Characters)."""

from typing import Tuple, List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANSPARENT: Color = (0, 0, 0, 0)

def apply_twintails(
    builder: SkinBuilder,
    palette: PaletteSpec,
    ribbon_color: Optional[Color] = None
) -> SkinBuilder:
    """Apply stepped 45-degree 3D spiral twintails and head hair volume."""
    hb = palette.hair_base             # Warm vanilla blonde #FCEBA8
    hs = palette.hair_shadow           # Warm honey shade #EBC682
    hh = palette.hair_highlight        # Luminous cream #FFF7C3
    hm = (246, 218, 150, 255)          # Golden peach mid-tone
    hd = (218, 178, 112, 255)          # Deep crease warmth
    rc = ribbon_color or palette.cloth_secondary # Candy pink ribbon
    rc_m = rc
    rc_l = (255, 218, 235, 255)
    rc_d = (220, 118, 162, 255)
    w = (255, 255, 255, 255)
    t = TRANSPARENT

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

    # 2. Head Back (8x8) Base Hair
    h_back_base = [
        [hs, hm, hb, hb, hb, hb, hm, hs],
        [hm, hb, hh, hh, hh, hh, hb, hm],
        [hb, hm, hb, hb, hb, hb, hm, hb],
        [hm, hs, hm, hb, hb, hm, hs, hm],
        [hs, hd, hs, hm, hm, hs, hd, hs],
        [hd, hd, hs, hs, hs, hs, hd, hd],
        [hd, hd, hd, hs, hs, hd, hd, hd],
        [hd, hd, hd, hd, hd, hd, hd, hd],
    ]
    builder.set_face("head.back", "base", h_back_base)

    # 3. Head Right Outer (8x8) - 3D Spiral Drill
    # Rows 0-1: Candy Pink Ribbon Bow with white stripes
    # Rows 2-7: 45-degree rotating stepped spiral coil
    r_side = [
        [rc_d, rc_m, rc_l, w,    rc_l, rc_m, rc_d, t   ], # row 0: ribbon loop
        [rc_m, w,    rc_m, rc_m, rc_m, w,    rc_m, t   ], # row 1: ribbon bow
        [rc_d, rc_m, rc_d, hb,   hb,   rc_m, rc_d, t   ], # row 2: ribbon anchor knot
        [t,    hb,   hh,   hm,   hs,   hb,   t,    t   ], # row 3: spiral turn 1
        [t,    hm,   hs,   hd,   hm,   hb,   t,    t   ], # row 4: spiral turn 1 shadow
        [hb,   hs,   hd,   hb,   hh,   hm,   t,    t   ], # row 5: spiral turn 2
        [hm,   hb,   hh,   hs,   hd,   hs,   t,    t   ], # row 6: spiral turn 2 highlight
        [hs,   hm,   hb,   hb,   hs,   hd,   t,    t   ], # row 7: spiral drill tip
    ]
    builder.set_face("head.right", "outer", r_side)

    # 4. Head Left Outer (8x8) - Mirrored 3D Spiral Drill
    l_side = [row[::-1] for row in r_side]
    builder.set_face("head.left", "outer", l_side)

    # 5. Head Back Outer (8x8) - Outer Ribbon Flare & Hair Volume
    h_back_o = [
        [rc_m, rc_d, t,    t,    t,    t,    rc_d, rc_m], # row 0: bow tips
        [rc_l, rc_m, t,    t,    t,    t,    rc_m, rc_l], # row 1: bow loops
        [hb,   hm,   t,    t,    t,    t,    hm,   hb  ], # row 2: anchored hair
        [hm,   hs,   hb,   t,    t,    hb,   hs,   hm  ], # row 3: volume
        [hs,   hd,   hm,   t,    t,    hm,   hd,   hs  ], # row 4: cascade
        [hb,   hs,   hb,   hm,   hm,   hb,   hs,   hb  ], # row 5: hair mantle
        [hm,   hb,   hs,   hd,   hd,   hs,   hb,   hm  ], # row 6: hair tips
        [hs,   hm,   hb,   hs,   hs,   hb,   hm,   hs  ], # row 7: lower edge
    ]
    builder.set_face("head.back", "outer", h_back_o)

    # 6. Front hair curls falling over shoulders on body.front.outer (cols 1 and 6, rows 2-4)
    # Applied to body.front.outer to give 3D depth to the front hair locks
    box_bfo = builder.faces["body.front"]["outer"]
    builder.image.putpixel((box_bfo[0] + 1, box_bfo[1] + 2), hb)
    builder.image.putpixel((box_bfo[0] + 6, box_bfo[1] + 2), hb)
    builder.image.putpixel((box_bfo[0] + 1, box_bfo[1] + 3), hm)
    builder.image.putpixel((box_bfo[0] + 6, box_bfo[1] + 3), hm)
    builder.image.putpixel((box_bfo[0] + 1, box_bfo[1] + 4), hs)
    builder.image.putpixel((box_bfo[0] + 6, box_bfo[1] + 4), hs)

    return builder
