"""Ribbon Sash & Capelet Prefab (Beatrice Diagonal Candy Bow & Victorian Capelet)."""

from typing import Tuple, List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANSPARENT: Color = (0, 0, 0, 0)

def apply_ribbon_sash(
    builder: SkinBuilder,
    palette: PaletteSpec
) -> SkinBuilder:
    """Apply diagonal candy-pink striped ribbon sash, chest bow, and gold-clasped capelet."""
    cp = palette.cloth_primary
    cs = palette.cloth_secondary      # Main candy pink
    ca = palette.cloth_accent         # Gold
    cd = palette.cloth_shadow
    w = (255, 255, 255, 255)          # Crisp white ribbon stripe / lace
    ws = (235, 230, 240, 255)
    t = TRANSPARENT

    # Pink ribbon shading
    pk_l = (255, 218, 235, 255)       # Light pink
    pk_m = cs                         # Mid pink
    pk_d = (220, 118, 162, 255)       # Deep pink shadow
    gold = ca
    gold_d = (206, 152, 32, 255)

    # 1. Body Front Outer (8x12) - Diagonal Sash & Grand Bow
    # Capelet collar (rows 0-1), Sash diagonal & bow knot (rows 4-8)
    b_front_o = [
        [w,     w,     w,     w,     w,     w,     w,     w    ], # row 0: capelet collar
        [cp,    cp,    w,     w,     w,     w,     cp,    cp   ], # row 1: capelet shoulders
        [t,     t,     t,     t,     t,     t,     t,     t    ], # row 2
        [t,     t,     t,     pk_d,  pk_m,  pk_l,  t,     t    ], # row 3: diagonal sash begins
        [t,     t,     t,     pk_m,  w,     pk_m,  pk_d,  t    ], # row 4: sash crossing
        [t,     t,     t,     t,     pk_d,  pk_m,  w,     pk_m ], # row 5: bow knot center
        [t,     t,     t,     t,     pk_m,  pk_l,  pk_m,  pk_d ], # row 6: bow loop & sash
        [t,     t,     t,     t,     t,     pk_d,  pk_m,  pk_l ], # row 7: sash ribbon tail
        [t,     t,     t,     t,     t,     t,     pk_d,  pk_m ], # row 8: tail downwards
        [t,     t,     t,     t,     t,     t,     t,     t    ], # row 9
        [cp,    w,     t,     t,     t,     t,     w,     cp   ], # row 10: skirt hem flare
        [w,     ws,    t,     t,     t,     t,     ws,    w    ], # row 11: skirt lace frill
    ]
    builder.set_face("body.front", "outer", b_front_o)

    # 2. Body Left Outer (4x12) - Ribbon knot overflow on waist
    b_left_o = [
        [w,     w,     w,     w    ], # row 0
        [cp,    cp,    cp,    cp   ], # row 1
        [t,     t,     t,     t    ], # row 2
        [pk_d,  pk_m,  pk_l,  pk_d ], # row 3: sash wrapping around side
        [pk_m,  w,     pk_m,  pk_m ], # row 4: sash fold
        [pk_l,  pk_m,  w,     pk_l ], # row 5: ribbon loop
        [pk_d,  pk_m,  pk_l,  pk_d ], # row 6: ribbon loop
        [t,     pk_d,  pk_m,  pk_m ], # row 7: hanging tail
        [t,     t,     pk_d,  pk_d ], # row 8: tail shadow
        [cp,    t,     t,     cp   ], # row 9
        [cp,    ws,    ws,    cp   ], # row 10
        [ws,    w,     w,     ws   ], # row 11
    ]
    builder.set_face("body.left", "outer", b_left_o)

    # 3. Body Back Outer (8x12) - Victorian Capelet with Gold Clasps
    b_back_o = [
        [w,     w,     w,     w,     w,     w,     w,     w    ], # row 0: capelet collar
        [cp,    cp,    cp,    cp,    cp,    cp,    cp,    cp   ], # row 1: capelet mantle
        [cp,    cd,    gold,  gold,  gold,  gold,  cd,    cp   ], # row 2: two golden back clasps
        [cd,    cp,    gold_d,gold_d,gold_d,gold_d,cp,    cd   ], # row 3: clasp shadow
        [w,     w,     w,     w,     w,     w,     w,     w    ], # row 4: capelet scalloped white trim
        [t,     t,     t,     t,     t,     t,     t,     t    ], # row 5
        [t,     t,     t,     t,     t,     t,     t,     t    ], # row 6
        [t,     t,     t,     t,     t,     t,     t,     t    ], # row 7
        [cp,    t,     t,     t,     t,     t,     t,     cp   ], # row 8
        [cd,    cp,    t,     t,     t,     t,     cp,    cd   ], # row 9
        [cp,    cd,    cp,    cp,    cp,    cp,    cd,    cp   ], # row 10
        [cd,    cp,    cd,    cd,    cd,    cd,    cp,    cd   ], # row 11
    ]
    builder.set_face("body.back", "outer", b_back_o)

    return builder
