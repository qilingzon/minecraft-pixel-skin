"""Minecraft Pixel Skin Builder - Programmatic API and validation wrapper.

Provides a structured, high-level abstraction for constructing Minecraft 64x64
skins (Slim and Classic models) with automatic UV mapping, layer separation,
palette management, and validation.
"""

from typing import Dict, List, Optional, Tuple, Union
from pathlib import Path
from PIL import Image
import os
import subprocess
import base64

from skin_tools import uv_faces, blank_skin, validate_skin

Color = Tuple[int, int, int, int]
Grid = List[List[Optional[Color]]]


class SkinBuilder:
    """High-level builder for programmatically authoring Minecraft 64x64 skins."""

    def __init__(self, model: str = 'slim', base_color: Color = (254, 238, 228, 255)):
        if model not in ('slim', 'classic'):
            raise ValueError(f"Model must be 'slim' or 'classic', got: {model}")
        self.model = model
        self.image = blank_skin(model, color=base_color)
        self.faces = uv_faces(model)

    def set_face(self, face_name: str, layer: str, grid: Grid) -> "SkinBuilder":
        """Set pixel grid for a specific UV face.
        
        Args:
            face_name: e.g. 'head.front', 'body.back', 'rightArm.left', etc.
            layer: 'base' or 'outer'
            grid: 2D list of RGBA tuples matching the face dimensions (height x width).
        """
        if face_name not in self.faces:
            raise KeyError(f"Unknown face: '{face_name}'. Valid faces: {list(self.faces.keys())}")
        if layer not in ('base', 'outer'):
            raise ValueError(f"Layer must be 'base' or 'outer', got: '{layer}'")

        box = self.faces[face_name][layer]
        bx, by, bw, bh = box

        if len(grid) != bh:
            raise ValueError(f"Face '{face_name}' {layer} requires {bh} rows, got {len(grid)}")

        for y, row in enumerate(grid):
            if len(row) != bw:
                raise ValueError(
                    f"Face '{face_name}' {layer} row {y} requires {bw} pixels, got {len(row)}"
                )
            for x, c in enumerate(row):
                if c is not None:
                    self.image.putpixel((bx + x, by + y), c)

        return self

    def fill_face(self, face_name: str, layer: str, color: Color) -> "SkinBuilder":
        """Fill an entire UV face with a uniform color."""
        box = self.faces[face_name][layer]
        bx, by, bw, bh = box
        grid = [[color] * bw for _ in range(bh)]
        return self.set_face(face_name, layer, grid)

    def validate(self) -> Dict[str, Union[bool, str, int, list]]:
        """Validate the skin against official Minecraft UV and transparency rules."""
        return validate_skin(self.image, self.model)

    def save(self, file_path: Union[str, Path]) -> Path:
        """Save the skin PNG and verify it passes validation."""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.image.save(path)
        val = self.validate()
        if not val['passed']:
            raise ValueError(f"Saved skin failed validation: {val['errors']}")
        return path
