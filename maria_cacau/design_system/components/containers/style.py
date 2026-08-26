from enum import Enum

from PyQt6.QtGui import QColor

from maria_cacau.design_system.tokens import COLORS


class DSContainerStyle(Enum):
    PLAIN = "plain"
    SOFT  = "soft"

    @property
    def background(self) -> QColor:
        match self:
            case DSContainerStyle.PLAIN:
                return COLORS.surface
            case DSContainerStyle.SOFT:
                return COLORS.surface_alt
