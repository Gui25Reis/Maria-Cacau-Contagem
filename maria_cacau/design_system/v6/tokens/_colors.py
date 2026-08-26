from dataclasses import dataclass
from enum import StrEnum

from PyQt6.QtGui import QColor

# ── Nível 1 — Paleta (privado) ───────────────────────────────────────────────

class _Palette(StrEnum):
    """Hex crus. Uso interno — referenciado apenas por ColorTokens."""

    # Marrons (marca)
    BROWN_DARK = "#391B10"   # --choc
    BROWN_MID  = "#000000"   # --choc-mid   TODO: converter oklch(28% 0.08 45)

    # Laranjas (accent)
    ORANGE_LIGHT = "#F9A879"   # --peach
    ORANGE_DARK  = "#000000"   # --peach-dk   TODO: converter oklch(65% 0.13 45)

    # Neutros quentes — superfície
    WARM_50  = "#000000"   # --bg         TODO: converter oklch(97.5% 0.006 65)
    WARM_100 = "#000000"   # --surface    TODO: converter oklch(100% 0.003 65)
    WARM_200 = "#000000"   # --surface-2  TODO: converter oklch(96% 0.009 65)
    WARM_300 = "#000000"   # --border     TODO: converter oklch(87% 0.009 65)
    WARM_400 = "#000000"   # --border-lt  TODO: converter oklch(93% 0.005 65)

    # Neutros quentes — texto
    WARM_900 = "#000000"   # --fg         TODO: converter oklch(18% 0.04 45)
    WARM_700 = "#000000"   # --fg-2       TODO: converter oklch(46% 0.02 55)
    WARM_600 = "#000000"   # --fg-3       TODO: converter oklch(60% 0.012 60)
    WARM_500 = "#000000"   # --sb-muted   TODO: converter oklch(58% 0.012 45)
    WARM_150 = "#000000"   # --sb-text    TODO: converter oklch(91% 0.008 65)

    # Semânticas
    GREEN    = "#388E3C"
    GREEN_BG = "#E8F5E9"
    AMBER    = "#A07800"
    AMBER_BG = "#FFF8E1"
    RED      = "#D32F2F"
    RED_BG   = "#FFEBEE"
    BLUE     = "#1565C0"
    BLUE_BG  = "#E3F2FD"


# ── Nível 2 — Semântico (público) ────────────────────────────────────────────

@dataclass(frozen=True)
class ColorTokens:
    """
    Tokens semânticos como QColor. Único ponto de acesso a cores no app.
    Instanciado uma vez como COLORS — não instanciar diretamente.
    """

    # Marca
    brand:        QColor
    brand_mid:    QColor
    accent:       QColor
    accent_dark:  QColor

    # Superfície
    background:   QColor
    surface:      QColor
    surface_alt:  QColor
    border:       QColor
    border_light: QColor

    # Texto
    text:         QColor
    text_muted:   QColor
    text_subtle:  QColor

    # Sidebar
    sidebar_text:  QColor
    sidebar_muted: QColor

    # Semântica
    success:     QColor
    success_bg:  QColor
    warning:     QColor
    warning_bg:  QColor
    error:       QColor
    error_bg:    QColor
    info:        QColor
    info_bg:     QColor


# ── Instância única ───────────────────────────────────────────────────────────

COLORS = ColorTokens(
    brand        = QColor(_Palette.BROWN_DARK),
    brand_mid    = QColor(_Palette.BROWN_MID),
    accent       = QColor(_Palette.ORANGE_LIGHT),
    accent_dark  = QColor(_Palette.ORANGE_DARK),

    background   = QColor(_Palette.WARM_50),
    surface      = QColor(_Palette.WARM_100),
    surface_alt  = QColor(_Palette.WARM_200),
    border       = QColor(_Palette.WARM_300),
    border_light = QColor(_Palette.WARM_400),

    text         = QColor(_Palette.WARM_900),
    text_muted   = QColor(_Palette.WARM_700),
    text_subtle  = QColor(_Palette.WARM_600),

    sidebar_text  = QColor(_Palette.WARM_150),
    sidebar_muted = QColor(_Palette.WARM_500),

    success    = QColor(_Palette.GREEN),
    success_bg = QColor(_Palette.GREEN_BG),
    warning    = QColor(_Palette.AMBER),
    warning_bg = QColor(_Palette.AMBER_BG),
    error      = QColor(_Palette.RED),
    error_bg   = QColor(_Palette.RED_BG),
    info       = QColor(_Palette.BLUE),
    info_bg    = QColor(_Palette.BLUE_BG),
)
