"""Drills Twintails Prefab (Stepped 3D Outer-Layer Spirals for Anime Characters)."""

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
    """Apply stepped 3D spiral twintails onto head outer layer and back."""
    hb = palette.hair_base
    hs = palette.hair_shadow
    hh = palette.hair_highlight
    rc = ribbon_color or palette.cloth_secondary
    t = TRANSPARENT

    # Head.Right Outer (8x8) - Right Drill Side
    # Rows 0-1: Ribbon tie, Rows 2-7: Spiral drill curls with depth shading
    r_side = [
        [t,  t,  rc, rc, rc, t,  t,  t],
        [t,  rc, rc, rc, rc, rc, t,  t],
        [t,  hb, hh, hb, hs, hs, t,  t],
        [t,  hs, hb, hh, hb, hs, t,  t],
        [t,  t,  hs, hb, hh, hb, hs, t],
        [t,  t,  hb, hh, hb, hs, t,  t],
        [t,  t,  hs, hb, hh, hs, t,  t],
        [t,  t,  t,  hs, hs, t,  t,  t]
    ]
    builder.set_face("head.right", "outer", r_side)

    # Head.Left Outer (8x8) - Mirrored Left Drill Side
    l_side = [row[::-1] for row in r_side]
    builder.set_face("head.left", "outer", l_side)

    # Head.Back Outer (8x8) - Cascading Volume & Anchored Spirals
    r_back = [
        [hb, hb, hb, hb, hb, hb, hb, hb],
        [hh, hb, hb, hh, hh, hb, hb, hh],
        [rc, rc, hs, hb, hb, hs, rc, rc],
        [hb, hs, hs, hb, hb, hs, hs, hb],
        [hh, hb, hs, t,  t,  hs, hb, hh],
        [hs, hb, hs, t,  t,  hs, hb, hs],
        [hs, hs, t,  t,  t,  t,  hs, hs],
        [t,  t,  t,  t,  t,  t,  t,  t]
    ]
    builder.set_face("head.back", "outer", r_back)
    return builder

