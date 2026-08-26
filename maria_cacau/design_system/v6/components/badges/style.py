from dataclasses import dataclass

from PyQt6.QtGui import QColor

from maria_cacau.design_system.v6.tokens import DSStatusType


@dataclass(frozen=True)
class DSBadgeStyle:
    color:      QColor
    background: QColor
    text:       str | None = None

    @classmethod
    def from_status(cls, status: DSStatusType, text: str | None = None) -> "DSBadgeStyle":
        return cls(color=status.color, background=status.background, text=text)
