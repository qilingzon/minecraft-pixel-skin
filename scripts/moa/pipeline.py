"""MoA Orchestration Pipeline (Gemini Architect/Critic + DeepSeek Coder)."""

from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from skin_builder import SkinBuilder
from moa.spec_schema import CharacterSpec, PaletteSpec
from moa.critic_protocol import CriticReview, CriticPatch
from prefabs import (
    apply_anime_eyes,
    apply_twintails,
    apply_lolita_skirt,
    apply_puff_sleeves,
    apply_ribbon_sash,
)

Color = Tuple[int, int, int, int]
TRANSPARENT: Color = (0, 0, 0, 0)

class MoAPipeline:
    """Orchestrates Gemini Architect/Critic and DeepSeek Coder collaboration."""

    def __init__(self, spec: Optional[CharacterSpec] = None):
        self.spec = spec or CharacterSpec()

    def assemble_base_skin(self) -> SkinBuilder:
        """DeepSeek Coder execution: assemble full multi-layer skin with zero-exposed-skin."""
        builder = SkinBuilder(self.spec.topology.model, self.spec.palette.skin)

        # 1. Multi-layer lolita dress & petticoat (establishes base torso & legs, prevents any bare skin)
        if self.spec.topology.has_lolita_skirt:
            apply_lolita_skirt(builder, self.spec.palette)

        # 2. Volumetric 3D puff sleeves (arms base & 3D outer layer)
        if getattr(self.spec.topology, "has_puff_sleeves", True):
            apply_puff_sleeves(builder, self.spec.palette)

        # 3. Sparkling anime eyes, facial features & bangs
        if self.spec.topology.eye_row:
            apply_anime_eyes(builder, self.spec.palette, self.spec.topology.eye_row)

        # 4. Stepped 45-degree 3D spiral twintails
        if self.spec.topology.has_twintails:
            apply_twintails(builder, self.spec.palette)

        # 5. Diagonal candy ribbon sash & gold-clasped capelet
        if getattr(self.spec.topology, "has_ribbon_sash", True):
            apply_ribbon_sash(builder, self.spec.palette)

        return builder

    def apply_patch(self, builder: SkinBuilder, patch: CriticPatch) -> SkinBuilder:
        """DeepSeek Coder execution: apply targeted aesthetic patch to SkinBuilder."""
        box = builder.faces[patch.face][patch.layer]
        bx, by, bw, bh = box

        rows = [patch.row] if patch.row is not None else list(range(bh))
        for r in rows:
            if not (0 <= r < bh):
                continue
            cols = range(patch.col_range[0], patch.col_range[1] + 1) if patch.col_range else range(bw)
            for c in cols:
                if 0 <= c < bw:
                    target_color = TRANSPARENT if patch.action == "clear" else (patch.color or self.spec.palette.skin)
                    builder.image.putpixel((bx + c, by + r), target_color)
        return builder

    def evaluate_aesthetic_rules(self, builder: SkinBuilder) -> CriticReview:
        """Gemini Critic evaluation: inspect skin against negative rules and quality checks."""
        patches: List[CriticPatch] = []
        box_hf = builder.faces["head.front"]["base"]
        s = self.spec.palette.skin

        # Negative Rule 1: no_mouth_on_chin_row (row 7 center must not have dark/beard pixels)
        if "no_mouth_on_chin_row" in self.spec.topology.negative_rules:
            for x in range(2, 6):
                px = builder.image.getpixel((box_hf[0] + x, box_hf[1] + 7))
                if px != s and px[3] > 0 and px != self.spec.palette.skin_blush:
                    patches.append(CriticPatch(
                        face="head.front", layer="base", row=7, col_range=(x, x),
                        action="replace", color=s, reason=f"Clean chin pixel at col {x} to avoid 3D beard artifact."
                    ))

        # Negative Rule 2: no_flat_tails_on_body_back
        if "no_flat_tails_on_body_back" in self.spec.topology.negative_rules:
            box_bb = builder.faces["body.back"]["outer"]
            hb = self.spec.palette.hair_base
            for r in range(4, 9):
                for c in range(2, 6):
                    px = builder.image.getpixel((box_bb[0] + c, box_bb[1] + r))
                    if px == hb:
                        patches.append(CriticPatch(
                            face="body.back", layer="outer", row=r, col_range=(c, c),
                            action="clear", reason=f"Remove flat hair tail from body.back center at row {r}, col {c}."
                        ))

        # Negative Rule 3: no_bare_skin_on_torso (rows 2-11 on body.front base must NOT be raw bare skin)
        if "no_bare_skin_on_torso" in self.spec.topology.negative_rules:
            box_bf = builder.faces["body.front"]["base"]
            petticoat_fill = (254, 250, 242, 255)
            for r in range(2, 12):
                for c in range(8):
                    px = builder.image.getpixel((box_bf[0] + c, box_bf[1] + r))
                    if px == s:
                        patches.append(CriticPatch(
                            face="body.front", layer="base", row=r, col_range=(c, c),
                            action="replace", color=petticoat_fill,
                            reason=f"Fill bare skin on body.front base at row {r}, col {c} with ivory petticoat frill."
                        ))

        # Negative Rule 4: must_have_puff_sleeves (rightArm.outer rows 0-3 must have volumetric pixels)
        if "must_have_puff_sleeves" in self.spec.topology.negative_rules:
            box_ra_o = builder.faces["rightArm.front"]["outer"]
            non_trans = 0
            for r in range(4):
                for c in range(3):
                    px = builder.image.getpixel((box_ra_o[0] + c, box_ra_o[1] + r))
                    if px[3] > 0:
                        non_trans += 1
            if non_trans < 6:
                patches.append(CriticPatch(
                    face="rightArm.front", layer="outer", row=1, col_range=(0, 2),
                    action="replace", color=self.spec.palette.cloth_primary,
                    reason="Restore 3D outer puff sleeve volume on rightArm."
                ))

        if patches:
            score = max(50, 100 - len(patches) * 5)
            return CriticReview(status="REVISE", score=score, summary=f"Found {len(patches)} aesthetic defects to patch.", patches=patches)
        return CriticReview(status="PASS", score=98, summary="All aesthetic criteria, negative rules, and zero-bare-skin constraints satisfied.")

    def run_pipeline(self, max_rounds: int = 3) -> Tuple[SkinBuilder, List[CriticReview]]:
        """Run complete MoA closed-loop iteration until PASS or max_rounds exhausted."""
        builder = self.assemble_base_skin()
        history: List[CriticReview] = []

        for rnd in range(1, max_rounds + 1):
            review = self.evaluate_aesthetic_rules(builder)
            history.append(review)
            if review.status == "PASS":
                break
            for patch in review.patches:
                self.apply_patch(builder, patch)

        return builder, history
