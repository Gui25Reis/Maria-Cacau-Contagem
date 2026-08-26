from dataclasses import dataclass

from PyQt6.QtGui import QFont

from ._fonts import FontFamily


@dataclass(frozen=True)
class TypographyToken:
    family:  FontFamily
    size_pt: int
    weight:  QFont.Weight
    tabular: bool = False   # OpenType tnum — dígitos de largura uniforme

    def to_qfont(self) -> QFont:
        font = QFont(self.family.value.name, self.size_pt)
        font.setWeight(self.weight)
        if self.tabular:
            font.setFeature(QFont.Tag.fromString("tnum"), 1)
        return font


class TypographyTokens:
    """Instâncias nomeadas de TypographyToken — um token por papel visual do moodboard."""

    # ── Sans — Segoe UI Variable ─────────────────────────────────────────────
    title          = TypographyToken(FontFamily.SANS, 20, QFont.Weight.DemiBold)
    numeric        = TypographyToken(FontFamily.SANS, 22, QFont.Weight.Bold, tabular=True)
    body           = TypographyToken(FontFamily.SANS, 13, QFont.Weight.Normal)
    body_strong    = TypographyToken(FontFamily.SANS, 13, QFont.Weight.DemiBold)
    body_muted     = TypographyToken(FontFamily.SANS, 13, QFont.Weight.Normal)
    caption        = TypographyToken(FontFamily.SANS, 12, QFont.Weight.Normal)
    caption_medium = TypographyToken(FontFamily.SANS, 12, QFont.Weight.Medium)
    caption_strong = TypographyToken(FontFamily.SANS, 12, QFont.Weight.DemiBold)
    caption_muted  = TypographyToken(FontFamily.SANS, 11, QFont.Weight.Normal)
    label          = TypographyToken(FontFamily.SANS, 11, QFont.Weight.Medium)
    overline       = TypographyToken(FontFamily.SANS, 11, QFont.Weight.DemiBold)
    overline_sm    = TypographyToken(FontFamily.SANS, 10, QFont.Weight.DemiBold)
    nav_title      = TypographyToken(FontFamily.SANS, 13, QFont.Weight.Medium)
    nav_name       = TypographyToken(FontFamily.SANS, 11, QFont.Weight.Bold)
    nav_item       = TypographyToken(FontFamily.SANS, 11, QFont.Weight.Normal)
    nav_group      = TypographyToken(FontFamily.SANS, 9,  QFont.Weight.Bold)

    # ── Mono — Cascadia Code ─────────────────────────────────────────────────
    mono_lg     = TypographyToken(FontFamily.MONO, 13, QFont.Weight.DemiBold)
    mono_bold   = TypographyToken(FontFamily.MONO, 12, QFont.Weight.Bold)
    mono        = TypographyToken(FontFamily.MONO, 12, QFont.Weight.Normal)
    mono_strong = TypographyToken(FontFamily.MONO, 12, QFont.Weight.DemiBold, tabular=True)
    mono_muted  = TypographyToken(FontFamily.MONO, 11, QFont.Weight.Normal)


TYPOGRAPHY = TypographyTokens()
