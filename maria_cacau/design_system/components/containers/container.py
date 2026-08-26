from PyQt6.QtCore import QRectF, Qt
from PyQt6.QtGui import QPainterPath, QRegion, QResizeEvent
from PyQt6.QtWidgets import QFrame

from maria_cacau.design_system.tokens import COLORS, LAYOUT, Shadows

from .style import DSContainerStyle

_DEFAULT_PADDING = LAYOUT.space16


class DSContainer(QFrame):

    def __init__(
        self,
        style: DSContainerStyle = DSContainerStyle.PLAIN,
        shadow: bool = True,
        padding: int = _DEFAULT_PADDING,
        parent=None,
    ) -> None:
        super().__init__(parent)
        self._style = style
        self.padding = padding

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self._apply_style()

        if shadow:
            Shadows.sm.apply(self)

    # ── Estilo ───────────────────────────────────────────────────────────────

    def _apply_style(self) -> None:
        self.setStyleSheet(
            "QFrame {"
            f"  background-color: {self._style.background.name()};"
            f"  border: 1px solid {COLORS.border_light.name()};"
            f"  border-radius: {LAYOUT.radius8}px;"
            "}"
        )

    # ── Clip to bounds ───────────────────────────────────────────────────────

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self._update_mask()

    def _update_mask(self) -> None:
        # QSS border-radius arredonda o desenho do próprio QFrame, mas não
        # recorta widgets filhos — sem a máscara, algo colado numa borda (ex:
        # a barra de acento do stat card) vazaria pelos cantos arredondados.
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), LAYOUT.radius8, LAYOUT.radius8)
        self.setMask(QRegion(path.toFillPolygon().toPolygon()))
