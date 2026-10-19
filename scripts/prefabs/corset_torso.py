"""Corset Torso Prefab (Beatrice Gold Dual Capelet Clasps, V-Neck Lace, Waist Corset & Back Mantle)."""

from typing import Tuple, List, Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import PaletteSpec

Color = Tuple[int, int, int, int]
TRANS: Color = (0, 0, 0, 0)

def apply_corset_torso(
    builder: SkinBuilder,
    palette: PaletteSpec
) -> SkinBuilder:
    """Apply Beatrice torso: chest locks, dual golden clasp buttons, corset ribbon, & capelet mantle."""
    s      = palette.skin
    cp     = palette.cloth_primary        # Rose crimson #BA2D5C
    cs     = palette.cloth_secondary      # Pink #E65A88
    cd     = palette.cloth_shadow         # Deep wine #7A1838
    hb     = palette.hair_base            # Blonde locks #FCEBA8
    hm     = (246, 218, 150, 255)         # Hair mid
    w      = (255, 255, 255, 255)         # Crisp lace
    ws     = (235, 228, 238, 255)         # Lace soft shadow
    gold   = (248, 202, 64, 255)          # Luminous gold buttons
    gold_d = (204, 150, 28, 255)          # Gold shade
    t      = TRANS

    # 1. Body Top (8x4) Base - Porcelain collarbone & shoulder straps
    b_top_base = [
        [w,  w,  s,  s,  s,  s,  w,  w],
        [cp, w,  s,  s,  s,  s,  w,  cp],
        [cp, cp, w,  s,  s,  w,  cp, cp],
        [cd, cp, cp, w,  w,  cp, cp, cd],
    ]
    builder.set_face("body.top", "base", b_top_base)

    # 2. Body Top (8x4) Outer - 3D Floating Shoulder Capelet
    b_top_outer = [
        [w,  w,  t,  t,  t,  t,  w,  w],
        [cp, cp, t,  t,  t,  t,  cp, cp],
        [cp, cp, cp, t,  t,  cp, cp, cp],
        [cd, cp, cp, cp, cp, cp, cp, cd],
    ]
    builder.set_face("body.top", "outer", b_top_outer)

    # 3. Body Front (8x12) Base
    # Rows 0-1: Porcelain chest & blonde hair locks
    # Rows 2-3: V-neck lace neckline
    # Rows 4-6: Corset bodice with criss-cross laces & dual gold clasp buttons
    # Rows 7-8: Corset waist cinch with deep wine vertical seams
    # Rows 9-11: White frilled petticoat underlayer (Zero bare skin!)
    b_front_base = [
        [s,    hb,   s,      s,      s,      s,      hb,   s   ], # row 0: neck & chest hair curls
        [s,    hm,   s,      s,      s,      s,      hm,   s   ], # row 1: porcelain chest
        [w,    w,    w,      s,      s,      w,      w,    w   ], # row 2: white lace neckline
        [cp,   cp,   cp,     w,      w,      cp,     cp,   cp  ], # row 3: upper bodice edge
        [cp,   gold, cs,     cp,     cp,     cs,     gold, cp  ], # row 4: dual gold clasps & pink ribbon
        [cd,   cp,   cp,     cs,     cs,     cp,     cp,   cd  ], # row 5: criss-cross corset center
        [cd,   cp,   cs,     cd,     cd,     cs,     cp,   cd  ], # row 6: corset lace crossing
        [cd,   cd,   cp,     cs,     cs,     cp,     cd,   cd  ], # row 7: corset lower cinch
        [cd,   cd,   cd,     cp,     cp,     cd,     cd,   cd  ], # row 8: waist taper
        [w,    w,    w,      w,      w,      w,      w,    w   ], # row 9: lower hem lace
        [w,    ws,   w,      ws,     ws,     w,      ws,   w   ], # row 10: petticoat underlayer
        [ws,   w,    ws,     w,      w,      ws,     w,    ws  ], # row 11: petticoat ruffles
    ]
    builder.set_face("body.front", "base", b_front_base)

    # 4. Body Front (8x12) Outer - 3D Capelet, Floating Gold Clasps & Floating Hair Locks
    b_front_outer = [
        [t,      hb,     t,      t,      t,      t,      hb,     t     ], # row 0: 3D blonde curl
        [w,      hm,     t,      t,      t,      t,      hm,     w     ], # row 1: 3D capelet collar
        [w,      hb,     w,      t,      t,      w,      hb,     w     ], # row 2: capelet lace trim + hair lock
        [cp,     gold,   cp,     t,      t,      cp,     gold,   cp    ], # row 3: 3D floating capelet clasps!
        [cp,     gold_d, cp,     t,      t,      cp,     gold_d, cp    ], # row 4: button shadow
        [cp,     cp,     t,      t,      t,      t,      cp,     cp    ], # row 5: capelet sides
        [cd,     cp,     t,      t,      t,      t,      cp,     cd    ], # row 6: capelet drape
        [cd,     cd,     t,      t,      t,      t,      cd,     cd    ], # row 7: capelet lower edge
        [w,      w,      t,      t,      t,      t,      w,      w     ], # row 8: capelet bottom lace
        [t,      t,      t,      t,      t,      t,      t,      t     ], # row 9
        [t,      t,      t,      t,      t,      t,      t,      t     ], # row 10
        [t,      t,      t,      t,      t,      t,      t,      t     ], # row 11
    ]
    builder.set_face("body.front", "outer", b_front_outer)

    # 5. Body Back (8x12) Base - Back of Corset & Gown (Elegant Shading, Organic Drape)
    b_back_base = [
        [cp,  cp,  cd,  cd,  cd,  cd,  cp,  cp], # row 0: back neckline
        [cp,  cp,  cd,  cd,  cd,  cd,  cp,  cp], # row 1
        [cd,  cp,  cp,  cd,  cd,  cp,  cp,  cd], # row 2
        [cd,  cd,  cp,  cp,  cp,  cp,  cd,  cd], # row 3: back dress drape
        [cd,  cd,  cp,  cp,  cp,  cp,  cd,  cd], # row 4
        [cd,  cd,  cd,  cp,  cp,  cd,  cd,  cd], # row 5
        [cd,  cd,  cd,  cp,  cp,  cd,  cd,  cd], # row 6: waist
        [cd,  cd,  cd,  cd,  cd,  cd,  cd,  cd], # row 7
        [w,   ws,  w,   ws,  ws,  w,   ws,  w ], # row 8: delicate waist lace seam
        [cp,  cp,  cd,  cd,  cd,  cd,  cp,  cp], # row 9: upper skirt back
        [cd,  cp,  cp,  cd,  cd,  cp,  cp,  cd], # row 10
        [cd,  cd,  cd,  cd,  cd,  cd,  cd,  cd], # row 11
    ]
    builder.set_face("body.back", "base", b_back_base)

    # 6. Body Back (8x12) Outer - Floating Capelet Mantle Drape with Flowing Scalloped Hem
    b_back_outer = [
        [w,   w,   w,   w,   w,   w,   w,   w ], # row 0: capelet top lace
        [cp,  cp,  cp,  cp,  cp,  cp,  cp,  cp], # row 1: capelet upper mantle
        [cp,  cp,  cs,  cs,  cs,  cs,  cp,  cp], # row 2: capelet highlight fold
        [cd,  cp,  cp,  cp,  cp,  cp,  cp,  cd], # row 3: capelet volume
        [cd,  cd,  cp,  cp,  cp,  cp,  cd,  cd], # row 4
        [w,   cd,  cd,  cp,  cp,  cd,  cd,  w ], # row 5: scalloped lace side wings
        [t,   w,   w,   w,   w,   w,   w,   t ], # row 6: scalloped center lace hem
        [t,   ws,  ws,  ws,  ws,  ws,  ws,  t ], # row 7: lace shadow edge
        [t,   t,   t,   t,   t,   t,   t,   t ], # row 8: skirt visible underneath
        [t,   t,   t,   t,   t,   t,   t,   t ], # row 9
        [t,   t,   t,   t,   t,   t,   t,   t ], # row 10
        [t,   t,   t,   t,   t,   t,   t,   t ], # row 11
    ]
    builder.set_face("body.back", "outer", b_back_outer)

    # 7. Body Sides (4x12) Base & Outer
    b_side_base = [
        [cp, cp, cd, cd],
        [cp, cp, cd, cd],
        [cp, cp, cp, cd],
        [cd, cp, cp, cd],
        [cd, cd, cp, cd],
        [cd, cd, cd, cd],
        [cd, cd, cd, cd],
        [cd, cd, cd, cd],
        [w,  w,  w,  w ],
        [cp, cp, cd, cd],
        [cd, cp, cp, cd],
        [cd, cd, cd, cd],
    ]
    b_side_outer = [
        [w,  w,  w,  w ],
        [cp, cp, cp, cp],
        [cp, cp, cp, cp],
        [cd, cp, cp, cd],
        [cd, cd, cp, cd],
        [w,  w,  w,  w ],
        [ws, ws, ws, ws],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
        [t,  t,  t,  t ],
    ]
    builder.set_face("body.right", "base", b_side_base)
    builder.set_face("body.right", "outer", b_side_outer)
    builder.set_face("body.left", "base", b_side_base)
    builder.set_face("body.left", "outer", b_side_outer)

    # 8. Body Bottom (8x4) Base - Under-skirt bloomers/petticoat
    builder.set_face("body.bottom", "base", [[w]*8 for _ in range(4)])
    builder.set_face("body.bottom", "outer", [[t]*8 for _ in range(4)])

    return builder
