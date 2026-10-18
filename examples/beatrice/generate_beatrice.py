"""Generate Beatrice Minecraft Skin - Reference-Inspired High-Fidelity Revision."""
from PIL import Image
import sys
from pathlib import Path

sys.path.append(r'D:\deepseek\mc\minecraft-pixel-skin\scripts')
from skin_tools import uv_faces, blank_skin, validate_skin

# ==================== PALETTE DEFINITIONS ====================
# 1. Hair - Soft Warm Vanilla / Cream Champagne Blonde (Clean, smooth, vibrant)
HAIR_LIGHT = (255, 247, 195, 255)  # #FFF7C3 Luminous cream highlight
HAIR_BASE  = (252, 235, 168, 255)  # #FCEBA8 Warm vanilla blonde base
HAIR_MID   = (246, 218, 150, 255)  # #F6DA96 Gentle golden peach mid-tone
HAIR_SHADE = (235, 198, 130, 255)  # #EBC682 Warm honey shade
HAIR_DEEP  = (218, 178, 112, 255)  # #DAB270 Deep crease warmth

# 2. Porcelain Anime Skin
SKIN       = (254, 238, 228, 255)  # #FEEFE4 Pure porcelain
SKIN_S     = (248, 224, 212, 255)  # #F8E0D4 Gentle contour
SKIN_BLUSH = (252, 212, 204, 255)  # #FCD4CC Soft peach-pink blush

# 3. Reference Aqua Turquoise Eyes (Sparkling, crystal anime eyes)
LASH_D     = (42, 40, 50, 255)     # #2A2832 Deep espresso/charcoal lash
LASH_M     = (72, 65, 78, 255)     # #48414E Soft lash edge
EYE_W      = (255, 255, 255, 255)  # #FFFFFF Sclera / bright highlight
EYE_AQ_L   = (135, 222, 220, 255)  # #87DEDC Vibrant turquoise highlight
EYE_AQ_M   = (45, 172, 175, 255)   # #2DACAF Crystal turquoise iris
EYE_AQ_D   = (30, 120, 128, 255)   # #1E7880 Deep cyan depth

# 4. Bows & Ribbons (Candy Pink & White Stripes)
BOW_L      = (255, 218, 235, 255)  # #FFDAEB Soft light pink
BOW_M      = (250, 156, 196, 255)  # #FA9CC4 Classic Beatrice pink
BOW_S      = (220, 118, 162, 255)  # #DC76A2 Deep pink shade
BOW_D      = (185, 82, 126, 255)   # #B9527E Fold shadow
BOW_W      = (255, 255, 255, 255)  # Ribbon white accent

# 5. Victorian Dress - Crimson Rose & Wine Red
ROSE_H     = (238, 92, 128, 255)   # #EE5C80 Rose highlight
ROSE       = (208, 55, 95, 255)    # #D0375F Saturated Victorian rose red
ROSE_S     = (172, 38, 76, 255)    # #AC264C Velvet rose shadow
ROSE_D     = (130, 22, 56, 255)    # #821638 Deep wine crease

# 6. Corset & Lace
WHITE      = (255, 255, 255, 255)  # Pure crisp white lace
WHITE_S    = (236, 232, 240, 255)  # Lace soft shadow
WHITE_D    = (210, 205, 218, 255)  # Lace deep shadow
LACE_WHITE = (255, 255, 255, 255)  # Corset white lace
LACE_PINK  = (248, 168, 202, 255)  # Corset pink ribbon
LACE_PK    = (248, 168, 202, 255)  # Corset pink ribbon
CORSET_DK  = (112, 32, 66, 255)    # Corset deep wine border

# 7. Gold Ornaments (Back buttons, tiara)
GOLD_L     = (255, 238, 142, 255)
GOLD       = (246, 198, 62, 255)
GOLD_D     = (206, 152, 32, 255)
CR_RED     = (198, 35, 75, 255)    # Tiara ruby

# 8. Striped Stockings & Mary Jane Shoes
STK_P      = (80, 35, 75, 255)     # #50234B Deep purple-plum
STK_PS     = (62, 26, 58, 255)     # #3E1A3A Plum shadow
STK_L      = (244, 162, 196, 255)  # #F4A2C4 Candy pink stripe
STK_LS     = (218, 136, 170, 255)  # Pink stripe shadow
SHOE       = (192, 44, 82, 255)    # Mary Jane shoes
SHOE_D     = (140, 24, 58, 255)
SHOE_SOLE  = (88, 18, 42, 255)

TRANS      = (0, 0, 0, 0)

def set_face_pixels(img, box, grid):
    bx, by, bw, bh = box
    for y in range(bh):
        row = grid[y]
        for x in range(bw):
            c = row[x]
            if c is not None:
                img.putpixel((bx + x, by + y), c)

def create_beatrice_skin():
    img = blank_skin('slim', color=SKIN)
    faces = uv_faces('slim')

    # ================================================================
    # 1. HEAD BASE (8x8)
    # ================================================================
    h_top = [
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_SHADE],
        [HAIR_MID,   HAIR_BASE,  HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_BASE,  HAIR_MID  ],
        [HAIR_BASE,  HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_BASE ],
        [HAIR_BASE,  HAIR_BASE,  HAIR_LIGHT, HAIR_BASE,  HAIR_BASE,  HAIR_LIGHT, HAIR_BASE,  HAIR_BASE ],
        [HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_MID  ],
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_MID,   HAIR_MID,   HAIR_BASE,  HAIR_MID,   HAIR_SHADE],
        [HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_SHADE, HAIR_SHADE],
        [HAIR_DEEP,  HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_MID,   HAIR_SHADE, HAIR_SHADE, HAIR_DEEP ],
    ]
    set_face_pixels(img, faces['head.top']['base'], h_top)

    h_bottom = [[SKIN_S]*8 for _ in range(8)]
    set_face_pixels(img, faces['head.bottom']['base'], h_bottom)

    # Reference-inspired anime face: high forehead bangs, crystal turquoise eyes, clean porcelain chin
    h_front = [
        [HAIR_MID,   HAIR_BASE,  HAIR_LIGHT, HAIR_BASE,  HAIR_BASE,  HAIR_LIGHT, HAIR_BASE,  HAIR_MID  ],
        [HAIR_BASE,  HAIR_BASE,  HAIR_SHADE, SKIN,       SKIN,       HAIR_SHADE, HAIR_BASE,  HAIR_BASE ],
        [HAIR_BASE,  HAIR_SHADE, SKIN,       SKIN,       SKIN,       SKIN,       HAIR_SHADE, HAIR_BASE ],
        [HAIR_SHADE, LASH_D,     LASH_D,     SKIN,       SKIN,       LASH_D,     LASH_D,     HAIR_SHADE],
        [HAIR_MID,   LASH_M,     EYE_AQ_M,   SKIN,       SKIN,       EYE_AQ_M,   LASH_M,     HAIR_MID  ],
        [HAIR_BASE,  EYE_W,      EYE_AQ_L,   SKIN,       SKIN,       EYE_AQ_L,   EYE_W,      HAIR_BASE ],
        [HAIR_MID,   SKIN_BLUSH, SKIN_BLUSH, SKIN,       SKIN,       SKIN_BLUSH, SKIN_BLUSH, HAIR_MID  ],
        [HAIR_SHADE, SKIN,       SKIN,       SKIN,       SKIN,       SKIN,       SKIN,       HAIR_SHADE],
    ]
    set_face_pixels(img, faces['head.front']['base'], h_front)

    h_right = [
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_SHADE],
        [HAIR_MID,   HAIR_BASE,  HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_BASE,  HAIR_MID  ],
        [HAIR_BASE,  HAIR_LIGHT, HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_LIGHT, HAIR_BASE ],
        [HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_MID,   HAIR_MID,   HAIR_MID,   HAIR_BASE,  HAIR_BASE ],
        [HAIR_MID,   HAIR_BASE,  HAIR_MID,   HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_MID  ],
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_SHADE, HAIR_SHADE, HAIR_BASE,  HAIR_MID,   HAIR_SHADE],
        [HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_SHADE, HAIR_SHADE],
        [HAIR_DEEP,  HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_MID,   HAIR_SHADE, HAIR_SHADE, HAIR_DEEP ],
    ]
    set_face_pixels(img, faces['head.right']['base'], h_right)

    h_left = [
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_SHADE],
        [HAIR_MID,   HAIR_BASE,  HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_BASE,  HAIR_MID  ],
        [HAIR_BASE,  HAIR_LIGHT, HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_LIGHT, HAIR_BASE ],
        [HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_MID,   HAIR_MID,   HAIR_MID,   HAIR_BASE,  HAIR_BASE ],
        [HAIR_MID,   HAIR_BASE,  HAIR_MID,   HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_MID  ],
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_SHADE, HAIR_SHADE, HAIR_BASE,  HAIR_MID,   HAIR_SHADE],
        [HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_SHADE, HAIR_SHADE],
        [HAIR_DEEP,  HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_MID,   HAIR_SHADE, HAIR_SHADE, HAIR_DEEP ],
    ]
    set_face_pixels(img, faces['head.left']['base'], h_left)

    h_back = [
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_SHADE],
        [HAIR_MID,   HAIR_BASE,  HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_LIGHT, HAIR_BASE,  HAIR_MID  ],
        [HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE ],
        [HAIR_BASE,  HAIR_MID,   HAIR_SHADE, HAIR_SHADE, HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_BASE ],
        [HAIR_MID,   HAIR_SHADE, HAIR_DEEP,  HAIR_DEEP,  HAIR_DEEP,  HAIR_DEEP,  HAIR_SHADE, HAIR_MID  ],
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_SHADE],
        [HAIR_SHADE, HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_MID,   HAIR_SHADE, HAIR_SHADE],
        [HAIR_DEEP,  HAIR_SHADE, HAIR_MID,   HAIR_MID,   HAIR_MID,   HAIR_MID,   HAIR_SHADE, HAIR_DEEP ],
    ]
    set_face_pixels(img, faces['head.back']['base'], h_back)

    # ================================================================
    # 2. HEAD OUTER (3D Layer: Bows, tiara, 3D curls & bangs)
    # ================================================================
    h_top_o = [
        [BOW_M,      BOW_M,      TRANS,      TRANS,      TRANS,      TRANS,      BOW_M,      BOW_M     ],
        [BOW_L,      BOW_W,      TRANS,      TRANS,      TRANS,      GOLD,       GOLD,       BOW_L     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      GOLD,       CR_RED,     GOLD_D    ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      GOLD_D,     TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
        [HAIR_BASE,  HAIR_MID,   TRANS,      TRANS,      TRANS,      TRANS,      HAIR_MID,   HAIR_BASE ],
        [HAIR_SHADE, HAIR_BASE,  TRANS,      TRANS,      TRANS,      TRANS,      HAIR_BASE,  HAIR_SHADE],
    ]
    set_face_pixels(img, faces['head.top']['outer'], h_top_o)

    h_front_o = [
        [BOW_M,      HAIR_BASE,  HAIR_LIGHT, HAIR_MID,   HAIR_MID,   HAIR_LIGHT, HAIR_BASE,  BOW_M     ],
        [BOW_L,      HAIR_BASE,  HAIR_MID,   TRANS,      TRANS,      HAIR_MID,   HAIR_BASE,  BOW_L     ],
        [HAIR_BASE,  HAIR_MID,   TRANS,      TRANS,      TRANS,      TRANS,      HAIR_MID,   HAIR_BASE ],
        [HAIR_MID,   TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      HAIR_MID  ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
    ]
    set_face_pixels(img, faces['head.front']['outer'], h_front_o)

    h_right_o = [
        [BOW_S,      BOW_M,      BOW_L,      BOW_W,      BOW_L,      BOW_M,      BOW_S,      TRANS     ],
        [BOW_M,      BOW_W,      BOW_M,      BOW_M,      BOW_M,      BOW_W,      BOW_M,      TRANS     ],
        [BOW_S,      BOW_M,      BOW_S,      HAIR_BASE,  HAIR_BASE,  BOW_M,      BOW_S,      TRANS     ],
        [TRANS,      HAIR_BASE,  HAIR_LIGHT, HAIR_MID,   HAIR_SHADE, HAIR_BASE,  TRANS,      TRANS     ],
        [TRANS,      HAIR_MID,   HAIR_SHADE, HAIR_DEEP,  HAIR_MID,   HAIR_BASE,  TRANS,      TRANS     ],
        [HAIR_BASE,  HAIR_SHADE, HAIR_DEEP,  HAIR_BASE,  HAIR_LIGHT, HAIR_MID,   TRANS,      TRANS     ],
        [HAIR_MID,   HAIR_BASE,  HAIR_LIGHT, HAIR_SHADE, HAIR_DEEP,  HAIR_SHADE, TRANS,      TRANS     ],
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_SHADE, HAIR_DEEP,  TRANS,      TRANS     ],
    ]
    set_face_pixels(img, faces['head.right']['outer'], h_right_o)

    h_left_o = [
        [TRANS,      BOW_S,      BOW_M,      BOW_L,      BOW_W,      BOW_L,      BOW_M,      BOW_S     ],
        [TRANS,      BOW_M,      BOW_W,      BOW_M,      BOW_M,      BOW_M,      BOW_W,      BOW_M     ],
        [TRANS,      BOW_S,      BOW_M,      HAIR_BASE,  HAIR_BASE,  BOW_S,      BOW_M,      BOW_S     ],
        [TRANS,      TRANS,      HAIR_BASE,  HAIR_LIGHT, HAIR_MID,   HAIR_SHADE, HAIR_BASE,  TRANS     ],
        [TRANS,      TRANS,      HAIR_MID,   HAIR_SHADE, HAIR_DEEP,  HAIR_MID,   HAIR_BASE,  TRANS     ],
        [TRANS,      TRANS,      HAIR_BASE,  HAIR_SHADE, HAIR_DEEP,  HAIR_BASE,  HAIR_LIGHT, HAIR_MID  ],
        [TRANS,      TRANS,      HAIR_MID,   HAIR_BASE,  HAIR_LIGHT, HAIR_SHADE, HAIR_DEEP,  HAIR_SHADE],
        [TRANS,      TRANS,      HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_BASE,  HAIR_SHADE, HAIR_DEEP ],
    ]
    set_face_pixels(img, faces['head.left']['outer'], h_left_o)

    h_back_o = [
        [BOW_M,      BOW_S,      TRANS,      TRANS,      TRANS,      TRANS,      BOW_S,      BOW_M     ],
        [BOW_L,      BOW_M,      TRANS,      TRANS,      TRANS,      TRANS,      BOW_M,      BOW_L     ],
        [HAIR_BASE,  HAIR_MID,   TRANS,      TRANS,      TRANS,      TRANS,      HAIR_MID,   HAIR_BASE ],
        [HAIR_MID,   HAIR_SHADE, HAIR_BASE,  TRANS,      TRANS,      HAIR_BASE,  HAIR_SHADE, HAIR_MID  ],
        [HAIR_SHADE, HAIR_DEEP,  HAIR_MID,   TRANS,      TRANS,      HAIR_MID,   HAIR_DEEP,  HAIR_SHADE],
        [HAIR_BASE,  HAIR_SHADE, HAIR_BASE,  HAIR_MID,   HAIR_MID,   HAIR_BASE,  HAIR_SHADE, HAIR_BASE ],
        [HAIR_MID,   HAIR_BASE,  HAIR_SHADE, HAIR_DEEP,  HAIR_DEEP,  HAIR_SHADE, HAIR_BASE,  HAIR_MID  ],
        [HAIR_SHADE, HAIR_MID,   HAIR_BASE,  HAIR_SHADE, HAIR_SHADE, HAIR_BASE,  HAIR_MID,   HAIR_SHADE],
    ]
    set_face_pixels(img, faces['head.back']['outer'], h_back_o)

    # ================================================================
    # 3. BODY BASE (8x12x4)
    # Reference-inspired: Front hair locks on chest, pink-white laced corset,
    # front V-split hem, full-length back gown with gold back clasps!
    # ================================================================
    b_top = [
        [WHITE,   WHITE_S, WHITE,   WHITE,   WHITE,   WHITE,   WHITE_S, WHITE  ],
        [WHITE_S, ROSE,    ROSE,    ROSE,    ROSE,    ROSE,    ROSE,    WHITE_S],
        [WHITE,   ROSE,    ROSE_S,  ROSE_S,  ROSE_S,  ROSE_S,  ROSE,    WHITE  ],
        [WHITE_S, ROSE_S,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_S,  WHITE_S],
    ]
    set_face_pixels(img, faces['body.top']['base'], b_top)

    b_bottom = [
        [STK_P,   STK_P,   STK_P,   STK_P,   STK_P,   STK_P,   STK_P,   STK_P  ],
        [STK_PS,  STK_PS,  STK_PS,  STK_PS,  STK_PS,  STK_PS,  STK_PS,  STK_PS ],
        [ROSE_S,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_S ],
        [ROSE_D,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_D,  ROSE_D ],
    ]
    set_face_pixels(img, faces['body.bottom']['base'], b_bottom)

    b_front = [
        # Row 0: White ruffle neckline
        [WHITE,      WHITE,      WHITE,      WHITE_S,    WHITE_S,    WHITE,      WHITE,      WHITE     ],
        # Row 1: Neckline and dress top
        [ROSE,       ROSE,       WHITE,      WHITE,      WHITE,      WHITE,      ROSE,       ROSE      ],
        # Row 2: Front blonde hair locks begin on shoulders (x=1 and x=6)
        [ROSE_S,     HAIR_BASE,  CORSET_DK,  LACE_WHITE, LACE_PINK,  CORSET_DK,  HAIR_BASE,  ROSE_S    ],
        # Row 3: Hair locks continue, corset lacing
        [ROSE,       HAIR_MID,   CORSET_DK,  LACE_PINK,  LACE_WHITE, CORSET_DK,  HAIR_MID,   ROSE      ],
        # Row 4: Hair locks continue, corset lacing
        [ROSE_S,     HAIR_SHADE, CORSET_DK,  LACE_WHITE, LACE_PINK,  CORSET_DK,  HAIR_SHADE, ROSE_S    ],
        # Row 5: Corset lacing
        [ROSE,       ROSE_S,     CORSET_DK,  LACE_PINK,  LACE_WHITE, CORSET_DK,  ROSE_S,     ROSE      ],
        # Row 6: Corset lacing bottom
        [ROSE_S,     ROSE_D,     CORSET_DK,  LACE_WHITE, LACE_PINK,  CORSET_DK,  ROSE_D,     ROSE_S    ],
        # Row 7: Waistband (White lace trim & pink ribbon belt)
        [WHITE,      WHITE,      WHITE,      WHITE_S,    WHITE_S,    WHITE,      BOW_M,      BOW_M     ],
        # Row 8: Front skirt split starts (Inverted V)
        [ROSE,       WHITE,      STK_P,      STK_PS,     STK_PS,     STK_P,      WHITE,      BOW_L     ],
        # Row 9: Skirt opens wider
        [ROSE_S,     WHITE,      STK_L,      STK_LS,     STK_LS,     STK_L,      WHITE,      BOW_M     ],
        # Row 10: Skirt sides & stocking
        [ROSE,       WHITE,      STK_P,      STK_PS,     STK_PS,     STK_P,      WHITE,      ROSE      ],
        # Row 11: Skirt edge
        [ROSE_D,     WHITE_S,    STK_L,      STK_LS,     STK_LS,     STK_L,      WHITE_S,    ROSE_D    ],
    ]
    set_face_pixels(img, faces['body.front']['base'], b_front)

    b_back = [
        # Row 0: Capelet top collar
        [WHITE,      WHITE,      WHITE_S,    WHITE_S,    WHITE_S,    WHITE_S,    WHITE,      WHITE     ],
        # Row 1: Capelet flap
        [ROSE,       ROSE,       ROSE_S,     ROSE_S,     ROSE_S,     ROSE_S,     ROSE,       ROSE      ],
        # Row 2: Mid-capelet with TWO GOLD CLASPS/BUTTONS in center (Reference detail!)
        [ROSE_S,     ROSE,       ROSE,       GOLD,       GOLD,       ROSE,       ROSE,       ROSE_S    ],
        # Row 3: Golden clasp shadows
        [ROSE,       ROSE_S,     ROSE_S,     GOLD_D,     GOLD_D,     ROSE_S,     ROSE_S,     ROSE      ],
        # Row 4: Capelet bottom edge
        [WHITE,      WHITE,      WHITE_S,    WHITE_S,    WHITE_S,    WHITE_S,    WHITE,      WHITE     ],
        # Row 5: Dress back
        [ROSE_S,     ROSE,       ROSE_S,     ROSE_S,     ROSE_S,     ROSE_S,     ROSE,       ROSE_S    ],
        # Row 6: White waistband belt
        [WHITE,      WHITE_S,    WHITE,      WHITE,      WHITE,      WHITE,      WHITE_S,    WHITE     ],
        # Rows 7-11: Full-length flowing rose gown in back!
        [ROSE,       ROSE_H,     ROSE,       ROSE_S,     ROSE_S,     ROSE,       ROSE_H,     ROSE      ],
        [ROSE_S,     ROSE,       ROSE_H,     ROSE,       ROSE,       ROSE_H,     ROSE,       ROSE_S    ],
        [ROSE_D,     ROSE_S,     ROSE,       ROSE_H,     ROSE_H,     ROSE,       ROSE_S,     ROSE_D    ],
        [ROSE,       ROSE_D,     ROSE_S,     ROSE,       ROSE,       ROSE_S,     ROSE_D,     ROSE      ],
        [ROSE_S,     ROSE,       ROSE_D,     ROSE_S,     ROSE_S,     ROSE_D,     ROSE,       ROSE_S    ],
    ]
    set_face_pixels(img, faces['body.back']['base'], b_back)

    b_right = [
        [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
        [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
        [ROSE_S,     ROSE,       ROSE,       ROSE_S    ],
        [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
        [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
        [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
        [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
        [ROSE,       ROSE_H,     ROSE,       ROSE_S    ],
        [ROSE_S,     ROSE,       ROSE_H,     ROSE_S    ],
        [ROSE_D,     ROSE_S,     ROSE,       ROSE_D    ],
        [ROSE,       ROSE_D,     ROSE_S,     ROSE      ],
        [ROSE_S,     ROSE,       ROSE_D,     ROSE_S    ],
    ]
    set_face_pixels(img, faces['body.right']['base'], b_right)

    b_left = [
        [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
        [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
        [ROSE_S,     ROSE,       ROSE,       ROSE_S    ],
        [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
        [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
        [BOW_S,      BOW_M,      BOW_M,      ROSE_D    ],
        [BOW_M,      BOW_L,      BOW_W,      ROSE_S    ],
        [BOW_S,      BOW_M,      BOW_L,      ROSE_S    ],
        [ROSE_D,     ROSE_S,     ROSE,       ROSE_D    ],
        [ROSE,       ROSE_D,     ROSE_S,     ROSE      ],
        [ROSE_S,     ROSE,       ROSE_D,     ROSE_S    ],
        [ROSE_D,     ROSE_S,     ROSE,       ROSE_D    ],
    ]
    set_face_pixels(img, faces['body.left']['base'], b_left)

    # ================================================================
    # 4. BODY OUTER (3D Layer: Capelet volume, 3D curls, bow sash)
    # ================================================================
    b_top_o = [
        [WHITE,   WHITE,   WHITE,   WHITE,   WHITE,   WHITE,   WHITE,   WHITE  ],
        [WHITE_S, TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   WHITE_S],
        [WHITE,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   TRANS,   WHITE  ],
        [WHITE_S, WHITE,   WHITE_S, WHITE_S, WHITE_S, WHITE_S, WHITE,   WHITE_S],
    ]
    set_face_pixels(img, faces['body.top']['outer'], b_top_o)

    b_front_o = [
        [WHITE,      WHITE,      WHITE,      WHITE,      WHITE,      WHITE,      WHITE,      WHITE     ],
        [ROSE_H,     ROSE,       WHITE,      WHITE,      WHITE,      WHITE,      ROSE,       ROSE_H    ],
        [TRANS,      HAIR_BASE,  TRANS,      TRANS,      TRANS,      TRANS,      HAIR_BASE,  TRANS     ],
        [TRANS,      HAIR_MID,   TRANS,      TRANS,      TRANS,      TRANS,      HAIR_MID,   TRANS     ],
        [TRANS,      HAIR_SHADE, TRANS,      TRANS,      BOW_S,      BOW_M,      BOW_L,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      BOW_M,      BOW_W,      BOW_M,      BOW_S     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      BOW_S,      BOW_M,      BOW_L,      BOW_W     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      BOW_S,      BOW_M,      BOW_L     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      BOW_S,      BOW_M     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
        [ROSE,       WHITE,      TRANS,      TRANS,      TRANS,      TRANS,      WHITE,      ROSE      ],
        [WHITE,      WHITE_S,    TRANS,      TRANS,      TRANS,      TRANS,      WHITE_S,    WHITE     ],
    ]
    set_face_pixels(img, faces['body.front']['outer'], b_front_o)

    b_back_o = [
        [WHITE,      WHITE,      WHITE,      WHITE,      WHITE,      WHITE,      WHITE,      WHITE     ],
        [ROSE_H,     ROSE,       ROSE,       ROSE,       ROSE,       ROSE,       ROSE,       ROSE_H    ],
        [ROSE,       ROSE_S,     TRANS,      TRANS,      TRANS,      TRANS,      ROSE_S,     ROSE      ],
        [ROSE_S,     TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      ROSE_S    ],
        [WHITE,      WHITE_S,    WHITE,      WHITE,      WHITE,      WHITE,      WHITE_S,    WHITE     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS     ],
        [ROSE,       TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      TRANS,      ROSE      ],
        [ROSE_S,     ROSE,       TRANS,      TRANS,      TRANS,      TRANS,      ROSE,       ROSE_S    ],
        [ROSE,       ROSE_S,     ROSE,       ROSE,       ROSE,       ROSE,       ROSE_S,     ROSE      ],
        [ROSE_S,     ROSE,       ROSE_S,     ROSE_S,     ROSE_S,     ROSE_S,     ROSE,       ROSE_S    ],
    ]
    set_face_pixels(img, faces['body.back']['outer'], b_back_o)

    b_left_o = [
        [WHITE,      WHITE,      WHITE,      WHITE     ],
        [ROSE_H,     ROSE,       ROSE,       ROSE_H    ],
        [TRANS,      TRANS,      TRANS,      TRANS     ],
        [BOW_S,      BOW_M,      BOW_L,      BOW_S     ],
        [BOW_M,      BOW_W,      BOW_M,      BOW_M     ],
        [BOW_L,      BOW_M,      BOW_W,      BOW_L     ],
        [BOW_S,      BOW_M,      BOW_L,      BOW_S     ],
        [TRANS,      BOW_S,      BOW_M,      BOW_M     ],
        [TRANS,      TRANS,      BOW_S,      BOW_S     ],
        [ROSE,       TRANS,      TRANS,      ROSE      ],
        [ROSE_S,     WHITE_S,    WHITE_S,    ROSE_S    ],
        [WHITE_S,    WHITE_D,    WHITE_D,    WHITE_S   ],
    ]
    set_face_pixels(img, faces['body.left']['outer'], b_left_o)

    b_right_o = [
        [WHITE,      WHITE,      WHITE,      WHITE     ],
        [ROSE_H,     ROSE,       ROSE,       ROSE_H    ],
        [HAIR_BASE,  HAIR_MID,   TRANS,      TRANS     ],
        [HAIR_MID,   HAIR_SHADE, TRANS,      TRANS     ],
        [HAIR_SHADE, HAIR_DEEP,  TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS     ],
        [TRANS,      TRANS,      TRANS,      TRANS     ],
        [ROSE,       TRANS,      TRANS,      ROSE      ],
        [ROSE_S,     WHITE_S,    WHITE_S,    ROSE_S    ],
        [WHITE_S,    WHITE_D,    WHITE_D,    WHITE_S   ],
    ]
    set_face_pixels(img, faces['body.right']['outer'], b_right_o)

    # ================================================================
    # 5. ARMS (Slim 3x12: Puffy sleeves, white lace armband, flared lace cuffs)
    # ================================================================
    for arm in ['rightArm', 'leftArm']:
        a_top = [
            [WHITE,   WHITE_S, WHITE  ],
            [ROSE_H,  ROSE,    ROSE_H ],
            [ROSE,    ROSE_S,  ROSE   ],
            [ROSE_S,  ROSE_D,  ROSE_S ],
        ]
        set_face_pixels(img, faces[f'{arm}.top']['base'], a_top)

        a_bottom = [
            [SKIN,    SKIN,    SKIN   ],
            [SKIN,    SKIN,    SKIN   ],
            [WHITE_S, WHITE,   WHITE_S],
            [WHITE_D, WHITE_S, WHITE_D],
        ]
        set_face_pixels(img, faces[f'{arm}.bottom']['base'], a_bottom)

        a_front = [
            [WHITE,      WHITE_S,    WHITE     ],
            [ROSE_H,     ROSE,       ROSE      ],
            [ROSE,       ROSE_S,     ROSE      ],
            [WHITE,      WHITE,      WHITE     ],  # White lace armband (Reference detail!)
            [ROSE_S,     ROSE,       ROSE_S    ],
            [ROSE,       ROSE_S,     ROSE      ],
            [ROSE_S,     ROSE,       ROSE_S    ],
            [ROSE,       ROSE_S,     ROSE_D    ],
            [ROSE_S,     ROSE_D,     ROSE_S    ],
            [WHITE,      WHITE,      WHITE     ],  # Flared lace cuff
            [WHITE_S,    WHITE_D,    WHITE_S   ],
            [SKIN,       SKIN,       SKIN      ],  # Dainty porcelain hand
        ]
        set_face_pixels(img, faces[f'{arm}.front']['base'], a_front)

        a_back = [
            [WHITE,      WHITE_S,    WHITE     ],
            [ROSE,       ROSE_S,     ROSE      ],
            [ROSE_S,     ROSE_D,     ROSE_S    ],
            [WHITE,      WHITE,      WHITE     ],  # White lace armband
            [ROSE_S,     ROSE,       ROSE_S    ],
            [ROSE,       ROSE_S,     ROSE      ],
            [ROSE_S,     ROSE_D,     ROSE_S    ],
            [ROSE_D,     ROSE_S,     ROSE_D    ],
            [ROSE_S,     ROSE,       ROSE_S    ],
            [WHITE,      WHITE,      WHITE     ],  # Flared lace cuff
            [WHITE_S,    WHITE_D,    WHITE_S   ],
            [SKIN_S,     SKIN,       SKIN_S    ],
        ]
        set_face_pixels(img, faces[f'{arm}.back']['base'], a_back)

        for side in ['right', 'left']:
            a_side = [
                [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
                [ROSE_H,     ROSE,       ROSE,       ROSE_H    ],
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [WHITE,      WHITE,      WHITE,      WHITE     ],  # Armband
                [ROSE_S,     ROSE,       ROSE,       ROSE_S    ],
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
                [WHITE,      WHITE,      WHITE,      WHITE     ],  # Cuff
                [WHITE_S,    WHITE_D,    WHITE_D,    WHITE_S   ],
                [SKIN,       SKIN,       SKIN,       SKIN      ],
            ]
            set_face_pixels(img, faces[f'{arm}.{side}']['base'], a_side)

        # 3D Outer sleeves
        a_front_o = [
            [WHITE,   WHITE,   WHITE  ],
            [TRANS,   TRANS,   TRANS  ],
            [TRANS,   TRANS,   TRANS  ],
            [WHITE,   WHITE,   WHITE  ],  # 3D armband
            [TRANS,   TRANS,   TRANS  ],
            [TRANS,   TRANS,   TRANS  ],
            [TRANS,   TRANS,   TRANS  ],
            [ROSE_H,  ROSE,    ROSE_H ],
            [ROSE,    ROSE_S,  ROSE   ],
            [WHITE,   WHITE,   WHITE  ],  # 3D cuff flare
            [WHITE_S, WHITE_S, WHITE_S],
            [TRANS,   TRANS,   TRANS  ],
        ]
        set_face_pixels(img, faces[f'{arm}.front']['outer'], a_front_o)

        a_back_o = [
            [WHITE,   WHITE,   WHITE  ],
            [TRANS,   TRANS,   TRANS  ],
            [TRANS,   TRANS,   TRANS  ],
            [WHITE,   WHITE,   WHITE  ],
            [TRANS,   TRANS,   TRANS  ],
            [TRANS,   TRANS,   TRANS  ],
            [TRANS,   TRANS,   TRANS  ],
            [ROSE,    ROSE_S,  ROSE   ],
            [ROSE_S,  ROSE_D,  ROSE_S ],
            [WHITE,   WHITE,   WHITE  ],
            [WHITE_S, WHITE_S, WHITE_S],
            [TRANS,   TRANS,   TRANS  ],
        ]
        set_face_pixels(img, faces[f'{arm}.back']['outer'], a_back_o)

        for side in ['right', 'left']:
            a_side_o = [
                [WHITE,   WHITE,   WHITE,   WHITE  ],
                [TRANS,   TRANS,   TRANS,   TRANS  ],
                [TRANS,   TRANS,   TRANS,   TRANS  ],
                [WHITE,   WHITE,   WHITE,   WHITE  ],
                [TRANS,   TRANS,   TRANS,   TRANS  ],
                [TRANS,   TRANS,   TRANS,   TRANS  ],
                [TRANS,   TRANS,   TRANS,   TRANS  ],
                [ROSE_H,  ROSE,    ROSE,    ROSE_H ],
                [ROSE,    ROSE_S,  ROSE_S,  ROSE   ],
                [WHITE,   WHITE,   WHITE,   WHITE  ],
                [WHITE_S, WHITE_S, WHITE_S, WHITE_S],
                [TRANS,   TRANS,   TRANS,   TRANS  ],
            ]
            set_face_pixels(img, faces[f'{arm}.{side}']['outer'], a_side_o)

    # ================================================================
    # 6. LEGS (4x12: Front V-split reveals stockings, back has full gown!)
    # ================================================================
    for leg in ['rightLeg', 'leftLeg']:
        l_top = [[STK_P, STK_PS, STK_PS, STK_P] for _ in range(4)]
        set_face_pixels(img, faces[f'{leg}.top']['base'], l_top)

        l_bottom = [[SHOE_SOLE]*4 for _ in range(4)]
        set_face_pixels(img, faces[f'{leg}.bottom']['base'], l_bottom)

        # Front: High-low opening revealing striped stockings and Mary Jane shoes
        l_front = [
            # Rows 0-1: Skirt split opening showing purple stockings
            [STK_P,      STK_PS,     STK_PS,     STK_P     ],
            [STK_P,      STK_PS,     STK_PS,     STK_P     ],
            # Rows 2-3: Pink stripe
            [STK_L,      STK_LS,     STK_LS,     STK_L     ],
            [STK_L,      STK_LS,     STK_LS,     STK_L     ],
            # Rows 4-5: Purple stripe
            [STK_P,      STK_PS,     STK_PS,     STK_P     ],
            [STK_P,      STK_PS,     STK_PS,     STK_P     ],
            # Rows 6-7: Pink stripe
            [STK_L,      STK_LS,     STK_LS,     STK_L     ],
            [STK_L,      STK_LS,     STK_LS,     STK_L     ],
            # Row 8: Purple stripe
            [STK_P,      STK_PS,     STK_PS,     STK_P     ],
            # Rows 9-11: Wine red shoes with pink bow accent
            [SHOE,       BOW_M,      BOW_M,      SHOE      ],
            [SHOE,       SHOE,       SHOE,       SHOE      ],
            [SHOE_D,     SHOE_D,     SHOE_D,     SHOE_D    ],
        ]
        set_face_pixels(img, faces[f'{leg}.front']['base'], l_front)

        # Back: Full-length floor gown covering down to shoes! (Reference feature)
        l_back = [
            [ROSE,       ROSE_H,     ROSE,       ROSE_S    ],
            [ROSE_S,     ROSE,       ROSE_H,     ROSE_S    ],
            [ROSE_D,     ROSE_S,     ROSE,       ROSE_D    ],
            [ROSE,       ROSE_D,     ROSE_S,     ROSE      ],
            [ROSE_S,     ROSE,       ROSE_H,     ROSE_S    ],
            [ROSE_D,     ROSE_S,     ROSE,       ROSE_D    ],
            [ROSE,       ROSE_D,     ROSE_S,     ROSE      ],
            [ROSE_S,     ROSE_S,     ROSE_D,     ROSE_D    ],
            # Rows 8-9: Scalloped white lace & pink hem
            [WHITE,      WHITE,      WHITE_S,    WHITE_S   ],
            [BOW_L,      BOW_M,      BOW_M,      BOW_L     ],
            # Rows 10-11: Shoes peeking out
            [SHOE,       SHOE,       SHOE,       SHOE      ],
            [SHOE_D,     SHOE_D,     SHOE_D,     SHOE_D    ],
        ]
        set_face_pixels(img, faces[f'{leg}.back']['base'], l_back)

        for side in ['right', 'left']:
            l_side = [
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [ROSE_S,     ROSE_S,     ROSE_D,     ROSE_D    ],
                [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
                [BOW_L,      BOW_M,      BOW_M,      BOW_L     ],
                [SHOE,       SHOE,       SHOE,       SHOE      ],
                [SHOE_D,     SHOE_D,     SHOE_D,     SHOE_D    ],
            ]
            set_face_pixels(img, faces[f'{leg}.{side}']['base'], l_side)

        # 3D Outer Leg Layers
        l_front_o = [
            [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
            [WHITE_S,    TRANS,      TRANS,      WHITE_S   ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
            [TRANS,      BOW_L,      BOW_L,      TRANS     ],
            [TRANS,      BOW_M,      BOW_M,      TRANS     ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
        ]
        set_face_pixels(img, faces[f'{leg}.front']['outer'], l_front_o)

        l_back_o = [
            [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
            [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
            [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
            [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
            [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
            [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
            [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
            [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
            [WHITE_S,    WHITE_D,    WHITE_D,    WHITE_S   ],
            [BOW_L,      BOW_M,      BOW_M,      BOW_L     ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
            [TRANS,      TRANS,      TRANS,      TRANS     ],
        ]
        set_face_pixels(img, faces[f'{leg}.back']['outer'], l_back_o)

        for side in ['right', 'left']:
            l_side_o = [
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [ROSE_S,     ROSE_D,     ROSE_D,     ROSE_S    ],
                [ROSE,       ROSE_S,     ROSE_S,     ROSE      ],
                [WHITE,      WHITE_S,    WHITE_S,    WHITE     ],
                [WHITE_S,    WHITE_D,    WHITE_D,    WHITE_S   ],
                [BOW_L,      BOW_M,      BOW_M,      BOW_L     ],
                [TRANS,      TRANS,      TRANS,      TRANS     ],
                [TRANS,      TRANS,      TRANS,      TRANS     ],
            ]
            set_face_pixels(img, faces[f'{leg}.{side}']['outer'], l_side_o)

    return img

if __name__ == '__main__':
    skin = create_beatrice_skin()
    out_path = Path(r'D:\deepseek\mc\beatrice_skin.png')
    skin.save(out_path)
    print(f'Skin successfully saved to {out_path}')

    val = validate_skin(skin, 'slim')
    print('Validation result:', val)
