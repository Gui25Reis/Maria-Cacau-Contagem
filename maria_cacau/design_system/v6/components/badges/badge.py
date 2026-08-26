from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel

from maria_cacau.design_system.v6.tokens import (LAYOUT, FontFamily,
                                                 TypographyToken)

from .style import DSBadgeStyle

_DOT_SIZE  = 6
_PADDING_V = 2
_PADDING_H = LAYOUT.space8
_GAP       = 4

_BADGE_FONT = TypographyToken(FontFamily.SANS, 11, QFont.Weight.Medium)


class DSBadge(QFrame):

    def __init__(self, style: DSBadgeStyle, parent=None) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(_PADDING_H, _PADDING_V, _PADDING_H, _PADDING_V)
        layout.setSpacing(_GAP)

        self._dot = QFrame()
        self._dot.setFixedSize(_DOT_SIZE, _DOT_SIZE)

        self._label = QLabel()
        self._label.setFont(_BADGE_FONT.to_qfont())

        layout.addWidget(self._dot)
        layout.addWidget(self._label)

        self.apply(style)

    def apply(self, style: DSBadgeStyle) -> None:
        self._label.setText(style.text or "")
        self.setStyleSheet(
            "DSBadge {"
            f"  background-color: {style.background.name()};"
            f"  border-radius: {LAYOUT.radiusPill}px;"
            "  border: none;"
            "}"
        )
        self._dot.setStyleSheet(
            f"background-color: {style.color.name()}; border-radius: {LAYOUT.radiusPill}px;"
        )
        self._label.setStyleSheet(f"color: {style.color.name()};")
