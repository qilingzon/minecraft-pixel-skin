"""Lolita Skirt & Striped Stockings Prefab (Open-V Dress Structure)."""

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
    """Apply lolita split dress and striped stockings onto body and legs."""
    cp = palette.cloth_primary
    cs = palette.cloth_secondary
    ca = palette.cloth_accent
    cd = palette.cloth_shadow
    w = (255, 255, 255, 255)
    t = TRANSPARENT

    # Body.Front Outer (8x12) - Bodice, Capelet Buttons & Inverted-V Open Skirt
    body_f_outer = [
        [w,  w,  t,  t,  t,  t,  w,  w],   # row 0: white collar shoulders
        [w,  ca, t,  t,  t,  t,  ca, w],   # row 1: gold capelet buttons
        [t,  cp, cp, cp, cp, cp, cp, t],   # row 2: crimson bodice top
        [t,  cp, cs, cs, cs, cs, cp, t],   # row 3: pink chest ribbon
        [t,  cp, cp, ca, ca, cp, cp, t],   # row 4: gold brooch accent
        [t,  cd, cp, cp, cp, cp, cd, t],   # row 5: waist contour
        [w,  w,  w,  w,  w,  w,  w,  w],   # row 6: lace waist sash
        [cp, cp, cp, cp, cp, cp, cp, cp], # row 7: skirt top belt
        [cp, cp, cp, t,  t,  cp, cp, cp], # row 8: open-V skirt starts
        [cp, cp, t,  t,  t,  t,  cp, cp], # row 9: opening widens
        [cp, t,  t,  t,  t,  t,  t,  cp], # row 10: lower hem opening
        [w,  t,  t,  t,  t,  t,  t,  w],  # row 11: white frill edges
    ]
    builder.set_face("body.front", "outer", body_f_outer)

    # Body.Back Outer (8x12) - Back Bodice & Tiered Bustle Skirt
    body_b_outer = [
        [w,  w,  t,  t,  t,  t,  w,  w],
        [t,  cp, cp, cp, cp, cp, cp, t],
        [t,  cp, cp, ca, ca, cp, cp, t],
        [t,  cs, cs, cs, cs, cs, cs, t],
        [t,  cp, cp, cp, cp, cp, cp, t],
        [t,  cd, cp, cp, cp, cp, cd, t],
        [w,  w,  w,  w,  w,  w,  w,  w],
        [cp, cp, cp, cp, cp, cp, cp, cp],
        [cd, cp, cp, cp, cp, cp, cp, cd],
        [cp, cp, cd, cd, cd, cd, cp, cp],
        [cp, cd, cp, cp, cp, cp, cd, cp],
        [w,  w,  w,  w,  w,  w,  w,  w],
    ]
    builder.set_face("body.back", "outer", body_b_outer)

    # Legs (4x12) - Striped Stockings & Mary Jane Shoes
    leg_face = [
        [w,  w,  w,  w],   # row 0: lace garter
        [cp, cd, cd, cp], # row 1: dark stripe
        [cp, cd, cd, cp], # row 2: dark stripe
        [cs, cs, cs, cs], # row 3: pink stripe
        [cs, cs, cs, cs], # row 4: pink stripe
        [cp, cd, cd, cp], # row 5: dark stripe
        [cp, cd, cd, cp], # row 6: dark stripe
        [cs, cs, cs, cs], # row 7: pink stripe
        [cs, cs, cs, cs], # row 8: pink stripe
        [w,  w,  w,  w],   # row 9: white sock ankle
        [cp, cp, cp, cp], # row 10: shoe body
        [cd, cd, cd, cd], # row 11: shoe sole
    ]
    for leg in ["rightLeg", "leftLeg"]:
        for f in ["front", "back", "left", "right"]:
            builder.set_face(f"{leg}.{f}", "base", leg_face)

    return builder

