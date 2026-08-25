from collections.abc import Callable
from dataclasses import dataclass, replace

from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import QGraphicsOpacityEffect, QPushButton

from maria_cacau.design_system.handlers import DSLoadingHandler
from maria_cacau.design_system.tokens import COLORS, LAYOUT, FontFamily, TypographyToken

from .states import DSButtonState
from .types import DSButtonType

_DISABLED_OPACITY = 0.35

_BUTTON_FONT = TypographyToken(FontFamily.SANS, 13, QFont.Weight.Medium)

_WHITE = QColor("#FFFFFF")


@dataclass(frozen=True)
class _ButtonPalette:
    bg:       QColor
    bg_hover: QColor
    text:     QColor
    border:   QColor | None = None


class DSButton(QPushButton, DSLoadingHandler):

    def __init__(self, text: str, type: DSButtonType = DSButtonType.PRIMARY, parent=None) -> None:
        super().__init__(text, parent)
        self.setFont(_BUTTON_FONT.to_qfont())

        self._label = text
        self._type  = type
        self._state = DSButtonState.DEFAULT

        self.color:      QColor | None = None
        self.text_color: QColor | None = None

        self.setFixedHeight(type.height)
        if type.is_square:
            self.setFixedWidth(type.height)
        elif type.min_width is not None:
            self.setMinimumWidth(type.min_width)

        self._setup_loading()
        self._apply_style()

    # ── API pública ──────────────────────────────────────────────────────────

    def update_state(self, state: DSButtonState) -> None:
        self._state = state

        match state:
            case DSButtonState.DEFAULT:
                self._stop_loading()
                self.setText(self._label)
                self.setEnabled(True)
                self.setGraphicsEffect(None)

            case DSButtonState.DISABLED:
                self._stop_loading()
                self.setText(self._label)
                self.setEnabled(False)
                effect = QGraphicsOpacityEffect(self)
                effect.setOpacity(_DISABLED_OPACITY)
                self.setGraphicsEffect(effect)

            case DSButtonState.LOADING:
                self._start_loading()

    def set_action(self, callback: Callable[[], None]) -> None:
        self.clicked.connect(callback)

    def refresh_style(self) -> None:
        """Reaplica o QSS — chamar após mudar `color`/`text_color` manualmente."""
        self._apply_style()

    # ── Estilo ───────────────────────────────────────────────────────────────

    def _apply_style(self) -> None:
        palette = self._resolve_palette()

        border_css = f"1px solid {palette.border.name()}" if palette.border else "none"
        rules = [
            "QPushButton {"
            f"  background-color: {palette.bg.name()};"
            f"  color: {palette.text.name()};"
            f"  border-radius: {LAYOUT.radius4}px;"
            f"  border: {border_css};"
            f"  padding: 0 14px;"
            "}",
            f"QPushButton:hover {{ background-color: {palette.bg_hover.name()}; }}",
        ]
        self.setStyleSheet(" ".join(rules))

    def _resolve_palette(self) -> _ButtonPalette:
        match self._type:
            case DSButtonType.PRIMARY:
                palette = _ButtonPalette(bg=COLORS.brand, bg_hover=COLORS.brand_mid, text=_WHITE)
            case DSButtonType.SECONDARY:
                palette = _ButtonPalette(
                    bg=COLORS.surface_alt, bg_hover=COLORS.border_light,
                    text=COLORS.text, border=COLORS.border,
                )
            case DSButtonType.ICON:
                # TODO: paleta default ainda não definida
                palette = _ButtonPalette(bg=COLORS.surface, bg_hover=COLORS.surface_alt, text=COLORS.text_muted)

        if self.color is not None:
            palette = replace(palette, bg=self.color)
        if self.text_color is not None:
            palette = replace(palette, text=self.text_color)

        return palette

    # ── DSLoadingHandler ─────────────────────────────────────────────────────

    def _on_loading_tick(self, frame: str) -> None:
        self.setText(frame)

    # ── QPushButton ──────────────────────────────────────────────────────────

    def mousePressEvent(self, event) -> None:
        if self._state == DSButtonState.LOADING:
            return
        super().mousePressEvent(event)
