from dataclasses import dataclass

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QWidget


@dataclass(frozen=True)
class ShadowConfig:
    blur:  int
    x:     int
    y:     int
    color: QColor

    def apply(self, widget: QWidget) -> None:
        """Cria uma instância fresca do effect — Qt não permite compartilhar
        um QGraphicsEffect entre widgets (o segundo setGraphicsEffect rouba
        o effect do primeiro)."""
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(self.blur)
        effect.setOffset(self.x, self.y)
        effect.setColor(self.color)
        widget.setGraphicsEffect(effect)


class Shadows:
    sm = ShadowConfig(blur=6, x=0, y=1, color=QColor(0, 0, 0, 25))
