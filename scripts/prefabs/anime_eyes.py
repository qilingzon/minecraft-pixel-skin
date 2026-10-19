"""Anime Eyes & Facial Features Prefab (Crystal Turquoise Anime Eyes & Porcelain Skin)."""

from typing import Tuple, Optional
import sys
from pathlib import Path

# Add scripts root to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANS: Color = (0, 0, 0, 0)

def apply_anime_eyes(
    builder: SkinBuilder,
    palette: PaletteSpec,
    eye_row: int = 4
) -> SkinBuilder:
    """Apply reference-perfect anime face, high forehead bangs, crystal turquoise eyes & blush."""
    s = palette.skin
    blush = palette.skin_blush
    hb = palette.hair_base
    hl = palette.hair_highlight
    hm = (246, 218, 150, 255)  # Hair mid-tone
    hs = palette.hair_shadow
    hd = (218, 178, 112, 255)  # Hair deep crease

    lash_d = palette.eye_lash
    lash_m = (72, 65, 78, 255)
    eye_w = palette.eye_sclera
    eye_l = (135, 222, 220, 255)  # Vibrant turquoise highlight
    eye_m = palette.eye_iris_light # Crystal turquoise iris
    eye_d = palette.eye_iris_dark  # Deep cyan depth

    bow_m = palette.cloth_secondary
    bow_l = (255, 218, 235, 255)

    # 1. Head.Front Base (8x8)
    h_front_base = [
        [hm,   hb,    hl,    hb,    hb,    hl,    hb,    hm   ], # Row 0: Bangs top highlight
        [hb,   hb,    hs,    s,     s,     hs,    hb,    hb   ], # Row 1: Bangs parting revealing porcelain forehead
        [hb,   hs,    s,     s,     s,     s,     hs,    hb   ], # Row 2: Forehead & temple hair
        [hs,   lash_d, lash_d, s,   s,     lash_d, lash_d, hs  ], # Row 3: Lash line top
        [hm,   lash_m, eye_m,  s,   s,     eye_m,  lash_m, hm   ], # Row 4: Pupil & soft lash edge
        [hb,   eye_w,  eye_l,  s,   s,     eye_l,  eye_w,  hb   ], # Row 5: Sclera & turquoise highlight
        [hm,   blush,  blush,  s,   s,     blush,  blush,  hm   ], # Row 6: Adorable peach blush cheeks
        [hs,   s,      s,      s,   s,     s,      s,      hs   ], # Row 7: Pure porcelain chin (ZERO dark pixels!)
    ]
    builder.set_face("head.front", "base", h_front_base)

    # 2. Head.Front Outer (8x8) - 3D Floating Fringe & Corner Bows
    h_front_outer = [
        [bow_m, hb,    hl,    hm,    hm,    hl,    hb,    bow_m], # Row 0: Corner bows + 3D bangs
        [bow_l, hb,    hm,    TRANS, TRANS, hm,    hb,    bow_l], # Row 1: Ribbon highlights + parted bangs
        [hb,    hm,    TRANS, TRANS, TRANS, TRANS, hm,    hb   ], # Row 2: Floating bangs over eyes
        [hm,    TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, hm   ], # Row 3: Temple locks
        [TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS], # Row 4
        [TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS], # Row 5
        [TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS], # Row 6
        [TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS, TRANS], # Row 7
    ]
    builder.set_face("head.front", "outer", h_front_outer)

    return builder
