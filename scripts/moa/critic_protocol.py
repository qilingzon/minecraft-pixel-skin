"""Critic Review Protocol and Patch Schema (MoA Critic Protocol)."""

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Tuple, Any, Optional
import json

Color = Tuple[int, int, int, int]

@dataclass
class CriticPatch:
    face: str
    layer: str
    row: Optional[int] = None
    col_range: Optional[Tuple[int, int]] = None
    action: str = "replace"
    color: Optional[Color] = None
    reason: str = ""

@dataclass
class CriticReview:
    status: str = "PASS"
    score: int = 100
    summary: str = "Aesthetic quality standard met."
    patches: List[CriticPatch] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CriticReview":
        patches_data = data.get("patches", [])
        patches = []
        for p in patches_data:
            col_range = tuple(p["col_range"]) if p.get("col_range") is not None else None
            color = tuple(p["color"]) if p.get("color") is not None else None
            patches.append(CriticPatch(
                face=p["face"],
                layer=p["layer"],
                row=p.get("row"),
                col_range=col_range,
                action=p.get("action", "replace"),
                color=color,
                reason=p.get("reason", "")
            ))
        return cls(
            status=data.get("status", "PASS"),
            score=data.get("score", 100),
            summary=data.get("summary", ""),
            patches=patches
        )

    @classmethod
    def from_json(cls, json_str: str) -> "CriticReview":
        return cls.from_dict(json.loads(json_str))

