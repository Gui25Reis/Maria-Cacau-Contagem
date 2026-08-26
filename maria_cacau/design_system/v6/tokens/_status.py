from enum import Enum

from PyQt6.QtGui import QColor

from ._colors import COLORS


class DSStatusType(Enum):
    SUCCESS = "success"
    WARNING = "warning"
    ERROR   = "error"
    INFO    = "info"

    @property
    def color(self) -> QColor:
        match self:
            case DSStatusType.SUCCESS:
                return COLORS.success
            case DSStatusType.WARNING:
                return COLORS.warning
            case DSStatusType.ERROR:
                return COLORS.error
            case DSStatusType.INFO:
                return COLORS.info

    @property
    def background(self) -> QColor:
        match self:
            case DSStatusType.SUCCESS:
                return COLORS.success_bg
            case DSStatusType.WARNING:
                return COLORS.warning_bg
            case DSStatusType.ERROR:
                return COLORS.error_bg
            case DSStatusType.INFO:
                return COLORS.info_bg
