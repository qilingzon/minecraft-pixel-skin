"""Anime Eyes Prefab (Sparkling Moe Eyes for Minecraft Skins)."""

from typing import Tuple, Optional
import sys
from pathlib import Path

# Add scripts root to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]

def apply_anime_eyes(
    builder: SkinBuilder,
    palette: PaletteSpec,
    eye_row: int = 4
) -> SkinBuilder:
    """Apply sparkling anime eyes onto head.front base layer."""
    s = palette.skin
    l = palette.eye_lash
    w = palette.eye_sclera
    d = palette.eye_iris_dark
    b = palette.eye_iris_light
    h = (255, 255, 255, 255) # primary reflection sparkle

    # Row 4: Eyelash line (8px)
    r4 = [s, l, l, s, s, l, l, s]
    # Row 5: Upper eye (sclera + deep iris with glint)
    r5 = [s, w, d, s, s, d, w, s]
    # Row 6: Lower eye (sclera / light glint + vibrant jewel iris)
    r6 = [s, w, b, s, s, b, w, s]

    builder.set_face("head.front", "base", [
        [s]*8, [s]*8, [s]*8, [s]*8,
        r4, r5, r6, [s]*8
    ])
    return builder
