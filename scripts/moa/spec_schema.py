"""Character Aesthetic Specification Schema (MoA Architect Spec)."""

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Tuple, Any, Optional
import json

Color = Tuple[int, int, int, int]

@dataclass
class PaletteSpec:
    skin: Color = (255, 238, 228, 255)
    skin_blush: Color = (255, 224, 222, 255)
    hair_base: Color = (252, 235, 168, 255)
    hair_shadow: Color = (235, 210, 140, 255)
    hair_highlight: Color = (255, 248, 205, 255)
    eye_iris_dark: Color = (45, 125, 145, 255)
    eye_iris_light: Color = (85, 205, 225, 255)
    eye_sclera: Color = (255, 255, 255, 255)
    eye_lash: Color = (55, 38, 48, 255)
    cloth_primary: Color = (195, 48, 92, 255)
    cloth_secondary: Color = (250, 185, 210, 255)
    cloth_accent: Color = (245, 205, 110, 255)
    cloth_shadow: Color = (145, 35, 70, 255)

@dataclass
class TopologySpec:
    model: str = "slim"
    eye_row: int = 4
    has_twintails: bool = True
    has_lolita_skirt: bool = True
    has_puff_sleeves: bool = True
    has_ribbon_sash: bool = True
    negative_rules: List[str] = field(default_factory=lambda: [
        "no_mouth_on_chin_row",
        "no_flat_tails_on_body_back",
        "no_dithering_on_face",
        "no_bare_skin_on_torso",
        "must_have_puff_sleeves"
    ])

@dataclass
class CharacterSpec:
    name: str = "custom_character"
    version: str = "1.0.0"
    description: str = ""
    palette: PaletteSpec = field(default_factory=PaletteSpec)
    topology: TopologySpec = field(default_factory=TopologySpec)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CharacterSpec":
        palette_data = data.get("palette", {})
        topology_data = data.get("topology", {})
        palette = PaletteSpec(**{k: tuple(v) if isinstance(v, list) else v for k, v in palette_data.items()})
        topology = TopologySpec(**topology_data)
        return cls(
            name=data.get("name", "custom_character"),
            version=data.get("version", "1.0.0"),
            description=data.get("description", ""),
            palette=palette,
            topology=topology,
        )

    @classmethod
    def from_json(cls, json_str: str) -> "CharacterSpec":
        return cls.from_dict(json.loads(json_str))
