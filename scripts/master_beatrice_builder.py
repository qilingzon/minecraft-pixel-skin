"""
Master Level Handcrafted Pixel Art Builder for Beatrice (Re:Zero) Minecraft Skin
Designed strictly adhering to top-tier anime skin standards (Ying reference benchmark):
- Dual-layer UV sculpting (floating bangs, floating capelet, puff sleeves, 3D cuffs & skirt hem)
- Refined crystal turquoise anime eyes with upper lash contour, multi-tone pupil and catchlight
- Delicate porcelain anime complexion with soft blush undercheek
- Victorian Lolita open-V gown with tiered lace petticoat and violet-black striped stockings
- Spiral twin-drill hair volume with winding highlights and Lolita bows
"""

from PIL import Image
import os

# ==============================================================================
# COLOR PALETTE SPECIFICATION
# ==============================================================================
_ = (0, 0, 0, 0) # Transparent

# Skin Tones
SKIN_BASE   = (255, 250, 247, 255)  # Porcelain anime skin
SKIN_SHADOW = (242, 230, 224, 255)  # Soft shadow under hair / jaw
SKIN_DEEP   = (230, 212, 204, 255)  # Crease shadow
SKIN_BLUSH  = (255, 214, 222, 255)  # Soft pink blush
SKIN_BLUSH_D= (255, 185, 198, 255)  # Deeper accent blush

# Hair Tones (Creamy Vanilla Blonde)
HAIR_HL     = (255, 249, 218, 255)  # Soft sunny highlight
HAIR_BASE   = (252, 235, 168, 255)  # Classic vanilla blonde
HAIR_SHADOW = (226, 203, 133, 255)  # Warm shadow
HAIR_DEEP   = (194, 166, 92, 255)   # Depth crease shadow
HAIR_CORE   = (163, 136, 70, 255)   # Deepest ambient occlusion

# Eyes (Crystal Turquoise)
EYE_LASH    = (68, 52, 60, 255)     # Deep plum eyeliner / upper lash
EYE_SPARK   = (255, 255, 255, 255)  # Pure white sparkling catchlight
EYE_DARK    = (35, 115, 128, 255)   # Deep teal pupil core
EYE_AQUA    = (56, 191, 211, 255)   # Vibrant turquoise iris
EYE_MINT    = (157, 235, 245, 255)  # Soft luminous mint lower reflection

# Ribbons & Hair Bows
BOW_HL      = (248, 155, 178, 255)  # Light rose pink
BOW_BASE    = (230, 106, 135, 255)  # Medium Lolita pink
BOW_SHADOW  = (184, 58, 86, 255)    # Shadow rose
BOW_DARK    = (138, 32, 56, 255)    # Knot shadow

# Dress & Gown (Victorian Crimson / Rose / Gold)
GOWN_DEEP   = (128, 28, 48, 255)    # Deep velvet burgundy
GOWN_CRIMSON= (168, 43, 68, 255)    # Rich crimson bolero / capelet
GOWN_ROSE   = (214, 82, 110, 255)   # Rose dress base
GOWN_HL     = (238, 122, 148, 255)  # Fold highlight
SASH_PINK   = (242, 138, 162, 255)  # Diagonal ribbon sash
SASH_LIGHT  = (255, 176, 196, 255)  # Sash highlight

# Lace & Petticoat
LACE_WHITE  = (255, 248, 252, 255)  # Pure pristine white lace
LACE_SHADOW = (225, 218, 230, 255)  # Soft lilac-tinted shadow
LACE_DEEP   = (198, 188, 206, 255)  # Ruffle crease

# Gold Accents
GOLD_HL     = (255, 228, 122, 255)  # Gilded highlight
GOLD_BASE   = (232, 186, 67, 255)   # Pure gold button / clasp
GOLD_SHADOW = (176, 132, 32, 255)   # Antique gold shadow

# Striped Stockings & Shoes
STRIPE_DARK = (44, 30, 48, 255)     # Deep eggplant / purple-black
STRIPE_SHAD = (32, 20, 36, 255)     # Stocking side shadow
STRIPE_LILAC= (122, 72, 125, 255)   # Rich violet stripe
STRIPE_L_HL = (152, 98, 156, 255)   # Stripe light
SHOE_BASE   = (150, 32, 54, 255)    # Mary Jane crimson shoe
SHOE_SOLE   = (38, 24, 32, 255)     # Dark sole

def create_master_skin():
    skin = Image.new("RGBA", (64, 64), _)

    def paint_rect(x0, y0, matrix):
        h = len(matrix)
        w = len(matrix[0])
        for r in range(h):
            for c in range(w):
                color = matrix[r][c]
                if color[3] > 0:
                    skin.putpixel((x0 + c, y0 + r), color)

    # ==========================================================================
    # 1. HEAD (64x64 UV)
    # ==========================================================================
    # Front Base (8, 8, 8, 8)
    head_front_base = [
        [HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP],
        [HAIR_BASE,   HAIR_HL,     HAIR_HL,     HAIR_BASE,   HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW],
        [HAIR_SHADOW, HAIR_BASE,   SKIN_SHADOW, HAIR_BASE,   HAIR_HL,     SKIN_SHADOW, HAIR_BASE,   HAIR_SHADOW],
        [HAIR_SHADOW, HAIR_DEEP,   SKIN_SHADOW, SKIN_BASE,   SKIN_BASE,   SKIN_SHADOW, HAIR_DEEP,   HAIR_SHADOW],
        [SKIN_SHADOW, EYE_LASH,    EYE_LASH,    SKIN_BASE,   SKIN_BASE,   EYE_LASH,    EYE_LASH,    SKIN_SHADOW],
        [HAIR_SHADOW, EYE_SPARK,   EYE_DARK,    SKIN_BASE,   SKIN_BASE,   EYE_SPARK,   EYE_DARK,    HAIR_SHADOW],
        [HAIR_SHADOW, EYE_AQUA,    EYE_MINT,    SKIN_BASE,   SKIN_BASE,   EYE_AQUA,    EYE_MINT,    HAIR_SHADOW],
        [HAIR_SHADOW, SKIN_BLUSH,  SKIN_BASE,   SKIN_BASE,   SKIN_BASE,   SKIN_BASE,   SKIN_BLUSH,  HAIR_SHADOW],
    ]
    paint_rect(8, 8, head_front_base)

    # Front Outer (40, 8, 8, 8) - 3D Floating Bangs & Sidelocks
    head_front_outer = [
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           HAIR_HL,     HAIR_BASE,   _,           _,           HAIR_BASE,   HAIR_HL,     _          ],
        [_,           HAIR_BASE,   HAIR_SHADOW, _,           _,           HAIR_SHADOW, HAIR_BASE,   _          ],
        [HAIR_BASE,   _,           _,           _,           _,           _,           _,           HAIR_BASE  ],
        [HAIR_HL,     _,           _,           _,           _,           _,           _,           HAIR_HL    ],
        [BOW_BASE,    _,           _,           _,           _,           _,           _,           BOW_BASE   ],
        [HAIR_SHADOW, _,           _,           _,           _,           _,           _,           HAIR_SHADOW],
    ]
    paint_rect(40, 8, head_front_outer)

    # Head Right Base (0, 8, 8, 8)
    head_right_base = [
        [HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   HAIR_DEEP,   HAIR_SHADOW],
        [HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW],
        [HAIR_SHADOW, HAIR_BASE,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP],
        [HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   HAIR_CORE],
        [HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   HAIR_CORE,   HAIR_CORE],
        [HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE],
        [HAIR_SHADOW, HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE],
        [HAIR_DEEP,   HAIR_SHADOW, HAIR_DEEP,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE],
    ]
    paint_rect(0, 8, head_right_base)

    # Head Right Outer (32, 8, 8, 8) - Big Pink Lolita Ribbon & 3D Spiral Curl
    head_right_outer = [
        [_,           _,           BOW_SHADOW,  BOW_HL,      BOW_BASE,    BOW_SHADOW,  _,           _          ],
        [_,           BOW_SHADOW,  BOW_BASE,    BOW_HL,      BOW_BASE,    BOW_DARK,    BOW_SHADOW,  _          ],
        [_,           BOW_HL,      BOW_BASE,    BOW_DARK,    BOW_BASE,    BOW_HL,      _,           _          ],
        [_,           BOW_SHADOW,  BOW_DARK,    BOW_BASE,    BOW_DARK,    BOW_SHADOW,  _,           _          ],
        [_,           HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   _,           _,           _          ],
        [_,           HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, _,           _,           _          ],
        [_,           HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   _,           _,           _          ],
        [_,           HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     _,           _,           _          ],
    ]
    paint_rect(32, 8, head_right_outer)

    # Head Left Base (16, 8, 8, 8)
    head_left_base = [
        [HAIR_SHADOW, HAIR_DEEP,   HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW],
        [HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE  ],
        [HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_BASE,   HAIR_SHADOW],
        [HAIR_CORE,   HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP  ],
        [HAIR_CORE,   HAIR_CORE,   HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW],
        [HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE  ],
        [HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_SHADOW],
        [HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_DEEP,   HAIR_SHADOW, HAIR_DEEP  ],
    ]
    paint_rect(16, 8, head_left_base)

    # Head Left Outer (48, 8, 8, 8) - Left Bow & 3D Spiral Curl
    head_left_outer = [
        [_,           _,           BOW_SHADOW,  BOW_BASE,    BOW_HL,      BOW_SHADOW,  _,           _          ],
        [_,           BOW_SHADOW,  BOW_DARK,    BOW_BASE,    BOW_HL,      BOW_BASE,    BOW_SHADOW,  _          ],
        [_,           _,           BOW_HL,      BOW_BASE,    BOW_DARK,    BOW_BASE,    BOW_HL,      _          ],
        [_,           _,           BOW_SHADOW,  BOW_DARK,    BOW_BASE,    BOW_DARK,    BOW_SHADOW,  _          ],
        [_,           _,           _,           HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     _          ],
        [_,           _,           _,           HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   _          ],
        [_,           _,           _,           HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, _          ],
        [_,           _,           _,           HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   _          ],
    ]
    paint_rect(48, 8, head_left_outer)

    # Head Back Base (24, 8, 8, 8)
    head_back_base = [
        [HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP  ],
        [HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW],
        [HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP  ],
        [HAIR_CORE,   HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   HAIR_CORE  ],
        [HAIR_CORE,   HAIR_CORE,   HAIR_DEEP,   HAIR_SHADOW, HAIR_SHADOW, HAIR_DEEP,   HAIR_CORE,   HAIR_CORE  ],
        [HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_DEEP,   HAIR_DEEP,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE  ],
        [HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE  ],
        [HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE,   HAIR_CORE  ],
    ]
    paint_rect(24, 8, head_back_base)

    # Head Back Outer (56, 8, 8, 8) - Soft Hair Floating Strands
    head_back_outer = [
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           HAIR_HL,     HAIR_BASE,   _,           _,           HAIR_BASE,   HAIR_HL,     _          ],
        [_,           HAIR_BASE,   HAIR_SHADOW, _,           _,           HAIR_SHADOW, HAIR_BASE,   _          ],
        [_,           HAIR_SHADOW, HAIR_DEEP,   _,           _,           HAIR_DEEP,   HAIR_SHADOW, _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
    ]
    paint_rect(56, 8, head_back_outer)

    # Head Top Base (8, 0, 8, 8)
    head_top_base = [
        [HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW],
        [HAIR_BASE,   HAIR_HL,     HAIR_HL,     HAIR_BASE,   HAIR_BASE,   HAIR_HL,     HAIR_HL,     HAIR_BASE  ],
        [HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE  ],
        [HAIR_SHADOW, HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_SHADOW],
        [HAIR_SHADOW, HAIR_BASE,   HAIR_SHADOW, HAIR_DEEP,   HAIR_DEEP,   HAIR_SHADOW, HAIR_BASE,   HAIR_SHADOW],
        [HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW, HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE  ],
        [HAIR_BASE,   HAIR_HL,     HAIR_HL,     HAIR_BASE,   HAIR_BASE,   HAIR_HL,     HAIR_HL,     HAIR_BASE  ],
        [HAIR_SHADOW, HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_BASE,   HAIR_HL,     HAIR_BASE,   HAIR_SHADOW],
    ]
    paint_rect(8, 0, head_top_base)

    # Head Bottom Base (16, 0, 8, 8) - Neck Porcelain
    head_bottom_base = [[SKIN_SHADOW for _c in range(8)] for _r in range(8)]
    for r in range(2, 6):
        for c in range(2, 6):
            head_bottom_base[r][c] = SKIN_BASE
    paint_rect(16, 0, head_bottom_base)

    # ==========================================================================
    # 2. TORSO / BODY (20, 20, 8, 12 Base; 20, 36, 8, 12 Outer)
    # ==========================================================================
    # Front Base (20, 20, 8, 12)
    # y=0: White lace collar & neck skin
    # y=1: Burgundy bolero collar + gold brooch clasp
    # y=2: Bodice with pink ribbon sash starting top-right
    # y=3..6: Victorian corset with crossing pink sash & gold buttons
    # y=7..11: Inverted-V skirt showing tiered white lace petticoat at center!
    body_front_base = [
        [SKIN_SHADOW, LACE_WHITE,  LACE_WHITE,  SKIN_BASE,   SKIN_BASE,   LACE_WHITE,  LACE_WHITE,  SKIN_SHADOW],
        [GOWN_DEEP,   GOWN_CRIMSON,LACE_WHITE,  GOLD_HL,     GOLD_BASE,   LACE_WHITE,  GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   GOWN_ROSE,   SASH_LIGHT,  SASH_PINK,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   SASH_LIGHT,  SASH_PINK,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,SASH_LIGHT,  SASH_PINK,   GOLD_BASE,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   SASH_LIGHT,  SASH_PINK,   GOWN_ROSE,   GOWN_ROSE,   GOLD_BASE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        # Skirt inverted-V open:
        [GOWN_CRIMSON,GOWN_ROSE,   GOWN_ROSE,   LACE_WHITE,  LACE_WHITE,  GOWN_ROSE,   GOWN_ROSE,   GOWN_CRIMSON],
        [GOWN_CRIMSON,GOWN_ROSE,   LACE_SHADOW, LACE_WHITE,  LACE_WHITE,  LACE_SHADOW, GOWN_ROSE,   GOWN_CRIMSON],
        [GOWN_CRIMSON,GOWN_ROSE,   LACE_WHITE,  LACE_DEEP,   LACE_DEEP,   LACE_WHITE,  GOWN_ROSE,   GOWN_CRIMSON],
        [GOWN_DEEP,   GOWN_CRIMSON,LACE_SHADOW, LACE_WHITE,  LACE_WHITE,  LACE_SHADOW, GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_DEEP,   LACE_WHITE,  LACE_SHADOW, LACE_SHADOW, LACE_WHITE,  GOWN_DEEP,   GOWN_DEEP  ],
    ]
    paint_rect(20, 20, body_front_base)

    # Front Outer (20, 36, 8, 12) - 3D Floating Victorian Bolero & Floating Skirt Hem
    body_front_outer = [
        [_,           LACE_WHITE,  LACE_WHITE,  _,           _,           LACE_WHITE,  LACE_WHITE,  _          ],
        [GOWN_DEEP,   GOWN_CRIMSON,_,           GOLD_HL,     GOLD_BASE,   _,           GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,_,           _,           _,           _,           GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   _,           _,           _,           _,           _,           _,           GOWN_DEEP  ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [GOWN_CRIMSON,GOWN_ROSE,   _,           _,           _,           _,           GOWN_ROSE,   GOWN_CRIMSON],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   _,           _,           GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_DEEP,   LACE_WHITE,  LACE_WHITE,  LACE_WHITE,  LACE_WHITE,  GOWN_DEEP,   GOWN_DEEP  ],
    ]
    paint_rect(20, 36, body_front_outer)

    # Body Back Base (32, 20, 8, 12) - Elegant Bolero Drape with 2 Gold Buttons & Pleated Skirt
    body_back_base = [
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_CRIMSON,LACE_WHITE,  LACE_WHITE,  GOWN_CRIMSON,GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   GOLD_HL,     GOLD_BASE,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   GOLD_HL,     GOLD_BASE,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_CRIMSON,LACE_SHADOW, LACE_WHITE,  LACE_WHITE,  LACE_SHADOW, GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_CRIMSON,GOWN_ROSE,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_CRIMSON,GOWN_ROSE,   GOWN_ROSE,   GOWN_CRIMSON],
        [GOWN_CRIMSON,GOWN_ROSE,   GOWN_HL,     GOWN_ROSE,   GOWN_ROSE,   GOWN_HL,     GOWN_ROSE,   GOWN_CRIMSON],
        [GOWN_CRIMSON,GOWN_ROSE,   GOWN_HL,     GOWN_ROSE,   GOWN_ROSE,   GOWN_HL,     GOWN_ROSE,   GOWN_CRIMSON],
        [GOWN_DEEP,   GOWN_CRIMSON,GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_ROSE,   GOWN_CRIMSON,GOWN_DEEP  ],
        [GOWN_DEEP,   GOWN_DEEP,   GOWN_CRIMSON,GOWN_CRIMSON,GOWN_CRIMSON,GOWN_CRIMSON,GOWN_DEEP,   GOWN_DEEP  ],
    ]
    paint_rect(32, 20, body_back_base)

    # Body Back Outer (32, 36, 8, 12) - Floating Bolero Scallop & Skirt Hem
    body_back_outer = [
        [_,           _,           _,           LACE_WHITE,  LACE_WHITE,  _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [GOWN_DEEP,   GOWN_CRIMSON,LACE_SHADOW, LACE_WHITE,  LACE_WHITE,  LACE_SHADOW, GOWN_CRIMSON,GOWN_DEEP  ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [_,           _,           _,           _,           _,           _,           _,           _          ],
        [GOWN_CRIMSON,GOWN_ROSE,   _,           _,           _,           _,           GOWN_ROSE,   GOWN_CRIMSON],
        [GOWN_DEEP,   GOWN_DEEP,   LACE_WHITE,  LACE_WHITE,  LACE_WHITE,  LACE_WHITE,  GOWN_DEEP,   GOWN_DEEP  ],
    ]
    paint_rect(32, 36, body_back_outer)

    # Body Right & Left Sides Base & Outer (16..20 and 28..32)
    # Right Side Base (16, 20, 4, 12)
    body_side_base = [
        [GOWN_DEEP, GOWN_CRIMSON, GOWN_CRIMSON, GOWN_DEEP],
        [GOWN_DEEP, GOWN_ROSE,    GOWN_ROSE,    GOWN_DEEP],
        [GOWN_DEEP, GOWN_ROSE,    GOWN_ROSE,    GOWN_DEEP],
        [GOWN_DEEP, GOWN_ROSE,    GOWN_ROSE,    GOWN_DEEP],
        [GOWN_DEEP, GOWN_ROSE,    GOWN_ROSE,    GOWN_DEEP],
        [GOWN_DEEP, GOWN_ROSE,    GOWN_ROSE,    GOWN_DEEP],
        [GOWN_DEEP, GOWN_CRIMSON, GOWN_CRIMSON, GOWN_DEEP],
        [GOWN_CRIMSON, GOWN_ROSE, GOWN_ROSE, GOWN_CRIMSON],
        [GOWN_CRIMSON, GOWN_ROSE, GOWN_ROSE, GOWN_CRIMSON],
        [GOWN_CRIMSON, GOWN_ROSE, GOWN_ROSE, GOWN_CRIMSON],
        [GOWN_DEEP, GOWN_CRIMSON, GOWN_CRIMSON, GOWN_DEEP],
        [GOWN_DEEP, GOWN_DEEP,    GOWN_DEEP,    GOWN_DEEP],
    ]
    paint_rect(16, 20, body_side_base)

    body_side_outer = [
        [GOWN_DEEP, GOWN_CRIMSON, GOWN_CRIMSON, GOWN_DEEP],
        [_,         _,            _,            _        ],
        [_,         _,            _,            _        ],
        [_,         _,            _,            _        ],
        [_,         _,            _,            _        ],
        [_,         _,            _,            _        ],
        [GOWN_DEEP, GOWN_CRIMSON, GOWN_CRIMSON, GOWN_DEEP],
        [_,         _,            _,            _        ],
        [_,         _,            _,            _        ],
        [_,         _,            _,            _        ],
        [GOWN_CRIMSON, GOWN_ROSE, GOWN_ROSE, GOWN_CRIMSON],
        [GOWN_DEEP, LACE_WHITE,   LACE_WHITE,   GOWN_DEEP],
    ]
    paint_rect(16, 36, body_side_outer)

    # Left Side Base (28, 20, 4, 12)
    paint_rect(28, 20, body_side_base)
    # Left Side Outer (28, 36, 4, 12)
    paint_rect(28, 36, body_side_outer)

    # Body Top Base (20, 16, 8, 4) & Bottom Base (28, 16, 8, 4)
    paint_rect(20, 16, [[GOWN_CRIMSON for _c in range(8)] for _r in range(4)])
    paint_rect(28, 16, [[GOWN_DEEP for _c in range(8)] for _r in range(4)])

    # ==========================================================================
    # 3. ARMS - ALEX SLIM (3x12) WITH 3D PUFF SLEEVES & LACE CUFFS
    # ==========================================================================
    # Right Arm:
    # Base: Front (44, 20, 3, 12), Right (40, 20, 4, 12), Back (51, 20, 3, 12), Left (47, 20, 4, 12)
    # Outer: Front (44, 36, 3, 12), Right (40, 36, 4, 12), Back (51, 36, 3, 12), Left (47, 36, 4, 12)
    
    # Arm Base Front (44, 20, 3, 12)
    arm_front_base = [
        [GOWN_CRIMSON, GOWN_ROSE,   GOWN_DEEP  ],
        [GOWN_ROSE,    GOWN_HL,     GOWN_CRIMSON],
        [GOWN_ROSE,    GOWN_HL,     GOWN_CRIMSON],
        [GOWN_CRIMSON, GOWN_ROSE,   GOWN_DEEP  ],
        [LACE_WHITE,   LACE_WHITE,  LACE_SHADOW],
        [LACE_SHADOW,  LACE_WHITE,  LACE_SHADOW],
        [LACE_WHITE,   LACE_WHITE,  LACE_SHADOW],
        [LACE_SHADOW,  LACE_WHITE,  LACE_SHADOW],
        [BOW_BASE,     BOW_HL,      BOW_SHADOW ],
        [LACE_WHITE,   LACE_WHITE,  LACE_SHADOW],
        [SKIN_BASE,    SKIN_BASE,   SKIN_SHADOW],
        [SKIN_BASE,    SKIN_BASE,   SKIN_SHADOW],
    ]
    paint_rect(44, 20, arm_front_base)

    # Arm Outer Front (44, 36, 3, 12) - 3D Puff Sleeve (y=0..3) & 3D Lace Cuff (y=9)
    arm_front_outer = [
        [GOWN_CRIMSON, GOWN_ROSE,   GOWN_DEEP  ],
        [GOWN_ROSE,    GOWN_HL,     GOWN_CRIMSON],
        [GOWN_ROSE,    GOWN_HL,     GOWN_CRIMSON],
        [GOWN_CRIMSON, GOWN_ROSE,   GOWN_DEEP  ],
        [_,            _,           _          ],
        [_,            _,           _          ],
        [_,            _,           _          ],
        [_,            _,           _          ],
        [_,            _,           _          ],
        [LACE_WHITE,   LACE_WHITE,  LACE_SHADOW],
        [_,            _,           _          ],
        [_,            _,           _          ],
    ]
    paint_rect(44, 36, arm_front_outer)

    # Arm Right Base (40, 20, 4, 12) & Outer (40, 36, 4, 12)
    arm_side_base = [
        [GOWN_DEEP, GOWN_CRIMSON, GOWN_ROSE,   GOWN_DEEP],
        [GOWN_DEEP, GOWN_ROSE,    GOWN_HL,     GOWN_CRIMSON],
        [GOWN_DEEP, GOWN_ROSE,    GOWN_HL,     GOWN_CRIMSON],
        [GOWN_DEEP, GOWN_CRIMSON, GOWN_ROSE,   GOWN_DEEP],
        [LACE_SHADOW, LACE_WHITE, LACE_WHITE,  LACE_SHADOW],
        [LACE_SHADOW, LACE_WHITE, LACE_WHITE,  LACE_SHADOW],
        [LACE_SHADOW, LACE_WHITE, LACE_WHITE,  LACE_SHADOW],
        [LACE_SHADOW, LACE_WHITE, LACE_WHITE,  LACE_SHADOW],
        [BOW_SHADOW, BOW_BASE,    BOW_HL,      BOW_SHADOW],
        [LACE_SHADOW, LACE_WHITE, LACE_WHITE,  LACE_SHADOW],
        [SKIN_SHADOW, SKIN_BASE,  SKIN_BASE,   SKIN_SHADOW],
        [SKIN_SHADOW, SKIN_BASE,  SKIN_BASE,   SKIN_SHADOW],
    ]
    paint_rect(40, 20, arm_side_base)

    arm_side_outer = [
        [GOWN_DEEP, GOWN_CRIMSON, GOWN_ROSE,   GOWN_DEEP],
        [GOWN_DEEP, GOWN_ROSE,    GOWN_HL,     GOWN_CRIMSON],
        [GOWN_DEEP, GOWN_ROSE,    GOWN_HL,     GOWN_CRIMSON],
        [GOWN_DEEP, GOWN_CRIMSON, GOWN_ROSE,   GOWN_DEEP],
        [_,         _,            _,           _        ],
        [_,         _,            _,           _        ],
        [_,         _,            _,           _        ],
        [_,         _,            _,           _        ],
        [_,         _,            _,           _        ],
        [LACE_SHADOW, LACE_WHITE, LACE_WHITE,  LACE_SHADOW],
        [_,         _,            _,           _        ],
        [_,         _,            _,           _        ],
    ]
    paint_rect(40, 36, arm_side_outer)

    # Arm Back Base (51, 20, 3, 12) & Outer (51, 36, 3, 12)
    paint_rect(51, 20, arm_front_base)
    paint_rect(51, 36, arm_front_outer)

    # Arm Left Base (47, 20, 4, 12) & Outer (47, 36, 4, 12)
    paint_rect(47, 20, arm_side_base)
    paint_rect(47, 36, arm_side_outer)

    # Arm Top Base (44, 16, 3, 4) & Outer (44, 32, 3, 4)
    paint_rect(44, 16, [[GOWN_CRIMSON for _c in range(3)] for _r in range(4)])
    paint_rect(44, 32, [[GOWN_CRIMSON for _c in range(3)] for _r in range(4)])
    # Arm Bottom Base (47, 16, 3, 4)
    paint_rect(47, 16, [[SKIN_BASE for _c in range(3)] for _r in range(4)])

    # LEFT ARM (UV: base at x=32..48, y=48..64; outer at x=48..64, y=48..64)
    # Left Arm: Front Base (36, 52, 3, 12), Outer (52, 52, 3, 12)
    paint_rect(36, 52, arm_front_base)
    paint_rect(52, 52, arm_front_outer)
    # Left Arm: Right Base (32, 52, 4, 12), Outer (48, 52, 4, 12)
    paint_rect(32, 52, arm_side_base)
    paint_rect(48, 52, arm_side_outer)
    # Left Arm: Back Base (43, 52, 3, 12), Outer (59, 52, 3, 12)
    paint_rect(43, 52, arm_front_base)
    paint_rect(59, 52, arm_front_outer)
    # Left Arm: Left Base (39, 52, 4, 12), Outer (55, 52, 4, 12)
    paint_rect(39, 52, arm_side_base)
    paint_rect(55, 52, arm_side_outer)
    # Left Arm Top & Bottom
    paint_rect(36, 48, [[GOWN_CRIMSON for _c in range(3)] for _r in range(4)])
    paint_rect(52, 48, [[GOWN_CRIMSON for _c in range(3)] for _r in range(4)])
    paint_rect(39, 48, [[SKIN_BASE for _c in range(3)] for _r in range(4)])

    # ==========================================================================
    # 4. LEGS (4x12) - STRIPED STOCKINGS & MARY JANE SHOES
    # ==========================================================================
    # Right Leg: Base (0, 16, 16, 16 -> front is at 4, 20, 4, 12)
    # y=0: Porcelain thigh / shadow
    # y=1..2: Stocking top elastic band
    # y=3..10: Violet-black alternating stripes (2px bands)
    # y=11: Mary Jane crimson shoes
    leg_front_base = [
        [SKIN_SHADOW,  SKIN_BASE,   SKIN_BASE,   SKIN_SHADOW ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_LILAC,STRIPE_L_HL, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_LILAC,STRIPE_L_HL, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_LILAC,STRIPE_L_HL, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_LILAC,STRIPE_L_HL, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [SHOE_BASE,    SHOE_BASE,   GOLD_HL,     SHOE_BASE   ],
    ]
    paint_rect(4, 20, leg_front_base)

    # Leg Outer Front (4, 36, 4, 12) - 3D Skirt Hem Flare (y=0..1) & Mary Jane Ribbon (y=11)
    leg_front_outer = [
        [GOWN_DEEP,    LACE_WHITE,  LACE_WHITE,  GOWN_DEEP   ],
        [GOWN_CRIMSON, LACE_SHADOW, LACE_SHADOW, GOWN_CRIMSON],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [BOW_BASE,     _,           _,           BOW_BASE    ],
    ]
    paint_rect(4, 36, leg_front_outer)

    # Leg Side Base (0, 20, 4, 12) & (8, 20, 4, 12)
    leg_side_base = [
        [SKIN_SHADOW,  SKIN_BASE,   SKIN_BASE,   SKIN_SHADOW ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_LILAC,STRIPE_LILAC,STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_LILAC,STRIPE_LILAC,STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_LILAC,STRIPE_LILAC,STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_LILAC,STRIPE_LILAC,STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [STRIPE_SHAD,  STRIPE_DARK, STRIPE_DARK, STRIPE_SHAD ],
        [SHOE_BASE,    SHOE_BASE,   SHOE_BASE,   SHOE_BASE   ],
    ]
    paint_rect(0, 20, leg_side_base)
    paint_rect(8, 20, leg_side_base)

    leg_side_outer = [
        [GOWN_DEEP,    LACE_WHITE,  LACE_WHITE,  GOWN_DEEP   ],
        [GOWN_CRIMSON, _,           _,           GOWN_CRIMSON],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [_,            _,           _,           _           ],
        [SHOE_BASE,    _,           _,           SHOE_BASE   ],
    ]
    paint_rect(0, 36, leg_side_outer)
    paint_rect(8, 36, leg_side_outer)

    # Leg Back Base (12, 20, 4, 12) & Outer (12, 36, 4, 12)
    paint_rect(12, 20, leg_front_base)
    paint_rect(12, 36, leg_front_outer)

    # Leg Top Base (4, 16, 4, 4) & Bottom Base (8, 16, 4, 4)
    paint_rect(4, 16, [[SKIN_SHADOW for _c in range(4)] for _r in range(4)])
    paint_rect(8, 16, [[SHOE_SOLE for _c in range(4)] for _r in range(4)])

    # LEFT LEG (UV: base at x=16..32, y=48..64; outer at x=0..16, y=48..64)
    # Left Leg Front Base (20, 52, 4, 12), Outer (4, 52, 4, 12)
    paint_rect(20, 52, leg_front_base)
    paint_rect(4, 52, leg_front_outer)
    # Left Leg Right Base (16, 52, 4, 12), Outer (0, 52, 4, 12)
    paint_rect(16, 52, leg_side_base)
    paint_rect(0, 52, leg_side_outer)
    # Left Leg Back Base (28, 52, 4, 12), Outer (12, 52, 4, 12)
    paint_rect(28, 52, leg_front_base)
    paint_rect(12, 52, leg_front_outer)
    # Left Leg Left Base (24, 52, 4, 12), Outer (8, 52, 4, 12)
    paint_rect(24, 52, leg_side_base)
    paint_rect(8, 52, leg_side_outer)
    # Left Leg Top & Bottom
    paint_rect(20, 48, [[SKIN_SHADOW for _c in range(4)] for _r in range(4)])
    paint_rect(24, 48, [[SHOE_SOLE for _c in range(4)] for _r in range(4)])

    return skin

if __name__ == "__main__":
    out_skin = create_master_skin()
    p1 = r"D:\deepseek\mc\beatrice_skin.png"
    p2 = r"D:\deepseek\mc\beatrice_moa_skin.png"
    p3 = r"D:\deepseek\mc\minecraft-pixel-skin\examples\beatrice\beatrice_skin.png"
    out_skin.save(p1)
    out_skin.save(p2)
    out_skin.save(p3)
    print("Master skin generated and saved to:")
    print(" ", p1)
    print(" ", p2)
    print(" ", p3)
