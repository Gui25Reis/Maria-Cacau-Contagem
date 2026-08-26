from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor, QResizeEvent
from PyQt6.QtWidgets import QLabel

from maria_cacau.design_system.v6.tokens import LabelStyle

_DEFAULT_ALIGNMENT = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter


class DSLabel(QLabel):

    def __init__(
        self,
        text: str,
        style: LabelStyle = LabelStyle.body,
        number_of_lines: int = 1,
        parent=None,
    ) -> None:
        super().__init__(parent)
        self._full_text      = text
        self._style           = style
        self._number_of_lines = number_of_lines

        self.color: QColor | None = None

        self.setFont(style.text_style.token.to_qfont())
        self.setAlignment(_DEFAULT_ALIGNMENT)
        self._apply_color()
        self._update_text()

    # ── API pública ──────────────────────────────────────────────────────────

    def setText(self, text: str) -> None:
        self._full_text = text
        self._update_text()

    @property
    def alignment_flag(self) -> Qt.AlignmentFlag:
        return super().alignment()

    @alignment_flag.setter
    def alignment_flag(self, value: Qt.AlignmentFlag) -> None:
        self.setAlignment(value)

    # ── Interno ──────────────────────────────────────────────────────────────

    def _apply_color(self) -> None:
        color = self.color or self._style.text_style.color
        self.setStyleSheet(f"color: {color.name()};")

    def _update_text(self) -> None:
        if self._number_of_lines != 1:
            super().setText(self._full_text)   # multi-linha: elide ainda não implementado
            return
        metrics = self.fontMetrics()
        elided  = metrics.elidedText(self._full_text, Qt.TextElideMode.ElideRight, self.width())
        super().setText(elided)

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self._update_text()

    def minimumSizeHint(self) -> QSize:
        # QLabel calcula o sizeHint a partir do texto completo — sem isso, o
        # layout nunca aperta o widget o suficiente pra disparar o elide.
        if self._number_of_lines != 1:
            return super().minimumSizeHint()
        return QSize(0, self.fontMetrics().height())
