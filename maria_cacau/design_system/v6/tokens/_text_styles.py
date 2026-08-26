from dataclasses import dataclass
from enum import Enum

from PyQt6.QtGui import QColor

from ._colors import COLORS
from ._typography import TYPOGRAPHY, TypographyToken


@dataclass(frozen=True)
class TextStyle:
    token:          TypographyToken
    color:          QColor
    letter_spacing: float = 0.0   # em (ex: 0.06 = 6%)


# Um Enum cujo valor é o próprio TextStyle colide (alias) sempre que dois
# cases têm o mesmo token+cor+letter_spacing, apagando membros em silêncio.
# Resolver o TextStyle à parte, por uma chave string única, evita isso.
_TEXT_STYLES: dict[str, TextStyle] = {
    # ── Sans ──────────────────────────────────────────────────────────────
    "title":          TextStyle(TYPOGRAPHY.title,          COLORS.text,          -0.01),
    "numeric":        TextStyle(TYPOGRAPHY.numeric,        COLORS.text,          -0.02),
    "body":           TextStyle(TYPOGRAPHY.body,           COLORS.text),
    "body_strong":    TextStyle(TYPOGRAPHY.body_strong,    COLORS.text),
    "body_muted":     TextStyle(TYPOGRAPHY.body_muted,     COLORS.text_subtle),
    "caption":        TextStyle(TYPOGRAPHY.caption,        COLORS.text_muted),
    "caption_medium": TextStyle(TYPOGRAPHY.caption_medium, COLORS.text_muted),
    "caption_strong": TextStyle(TYPOGRAPHY.caption_strong, COLORS.text),
    "caption_muted":  TextStyle(TYPOGRAPHY.caption_muted,  COLORS.text_subtle),
    "label":          TextStyle(TYPOGRAPHY.label,          COLORS.text_muted,  0.01),
    "overline":       TextStyle(TYPOGRAPHY.overline,       COLORS.text_muted,  0.06),
    "overline_sm":    TextStyle(TYPOGRAPHY.overline_sm,    COLORS.text_muted,  0.06),
    "nav_title":      TextStyle(TYPOGRAPHY.nav_title,      COLORS.sidebar_text),
    "nav_name":       TextStyle(TYPOGRAPHY.nav_name,       COLORS.sidebar_text),
    "nav_item":       TextStyle(TYPOGRAPHY.nav_item,       COLORS.sidebar_text),
    "nav_group":      TextStyle(TYPOGRAPHY.nav_group,      COLORS.sidebar_muted, 0.07),

    # ── Mono ──────────────────────────────────────────────────────────────
    "mono_lg":     TextStyle(TYPOGRAPHY.mono_lg,     COLORS.text),
    "mono_bold":   TextStyle(TYPOGRAPHY.mono_bold,   COLORS.text),
    "mono":        TextStyle(TYPOGRAPHY.mono,        COLORS.text_muted),
    "mono_strong": TextStyle(TYPOGRAPHY.mono_strong, COLORS.text),
    "mono_muted":  TextStyle(TYPOGRAPHY.mono_muted,  COLORS.text_subtle),
}


class LabelStyle(Enum):
    """Casos semânticos do moodboard. O componente extrai o TextStyle via `.text_style`."""

    title          = "title"
    numeric        = "numeric"
    body           = "body"
    body_strong    = "body_strong"
    body_muted     = "body_muted"
    caption        = "caption"
    caption_medium = "caption_medium"
    caption_strong = "caption_strong"
    caption_muted  = "caption_muted"
    label          = "label"
    overline       = "overline"
    overline_sm    = "overline_sm"
    nav_title      = "nav_title"
    nav_name       = "nav_name"
    nav_item       = "nav_item"
    nav_group      = "nav_group"

    mono_lg     = "mono_lg"
    mono_bold   = "mono_bold"
    mono        = "mono"
    mono_strong = "mono_strong"
    mono_muted  = "mono_muted"

    @property
    def text_style(self) -> TextStyle:
        return _TEXT_STYLES[self.value]
