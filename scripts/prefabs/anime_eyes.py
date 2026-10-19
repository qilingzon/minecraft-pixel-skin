"""Anime Eyes & Facial Features Prefab (Sparkling Moe Eyes, Bangs & Porcelain Skin)."""

from typing import Tuple, Optional
import sys
from pathlib import Path

# Add scripts root to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANSPARENT: Color = (0, 0, 0, 0)

def apply_anime_eyes(
    builder: SkinBuilder,
    palette: PaletteSpec,
    eye_row: int = 4
) -> SkinBuilder:
    """Apply sparkling anime eyes, forehead bangs base, and soft blush onto head.front."""
    s = palette.skin
    blush = (252, 212, 204, 255)      # Soft peach-pink blush
    l = palette.eye_lash              # Espresso lash line
    w = palette.eye_sclera            # Crisp white sclera
    d = palette.eye_iris_dark         # Deep crystal cyan
    b = palette.eye_iris_light        # Vibrant turquoise iris
    hb = palette.hair_base            # Warm vanilla blonde
    hh = palette.hair_highlight       # Cream highlight
    hm = (246, 218, 150, 255)         # Golden peach mid
    t = TRANSPARENT

    # Row 0-2: Forehead bangs roots
    r0 = [hb, hh, hh, hb, hb, hh, hh, hb]
    r1 = [hb, hb, hm, hb, hb, hm, hb, hb]
    r2 = [s,  hb, s,  s,  s,  s,  hb, s ]
    r3 = [s,  s,  s,  s,  s,  s,  s,  s ]
    # Row 4-6: Sparkling anime eyes
    r4 = [s,  l,  l,  s,  s,  l,  l,  s ]
    r5 = [s,  w,  d,  s,  s,  d,  w,  s ]
    r6 = [s,  w,  b,  s,  s,  b,  w,  s ]
    # Row 7: Pure porcelain chin with subtle side blush (strictly no beard / mouth artifact)
    r7 = [s,  blush, s, s, s, s, blush, s]

    builder.set_face("head.front", "base", [
        r0, r1, r2, r3, r4, r5, r6, r7
    ])

    # Head.Front Outer (8x8) - 3D Floating Fringe Bangs & Side Locks
    h_front_outer = [
        [hh, hb, hh, hh, hh, hh, hb, hh], # row 0: 3D bangs top
        [hb, hh, hb, hh, hh, hb, hh, hb], # row 1: 3D fringe
        [hb, hb, t,  t,  t,  t,  hb, hb], # row 2: parted bangs over eyes
        [hm, t,  t,  t,  t,  t,  t,  hm], # row 3: temple lock tips
        [t,  t,  t,  t,  t,  t,  t,  t ], # row 4
        [t,  t,  t,  t,  t,  t,  t,  t ], # row 5
        [t,  t,  t,  t,  t,  t,  t,  t ], # row 6
        [t,  t,  t,  t,  t,  t,  t,  t ], # row 7
    ]
    builder.set_face("head.front", "outer", h_front_outer)

    return builder
