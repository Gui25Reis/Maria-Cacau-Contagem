from dataclasses import dataclass


@dataclass(frozen=True)
class LayoutTokens:
    # ── Espaçamento (px) — escala 4pt ────────────────────────────────────────
    space4:  int = 4
    space8:  int = 8
    space12: int = 12
    space16: int = 16
    space20: int = 20
    space24: int = 24
    space32: int = 32

    # ── Border radius (px) ───────────────────────────────────────────────────
    radius4:    int = 4     # inputs, buttons, tags de modal
    radius8:    int = 8     # cards, tables, filter bar, tabs, nav items, notice, empty state
    radius12:   int = 12    # window chrome
    radiusPill: int = 9999  # badges — pill visual independente do tamanho


LAYOUT = LayoutTokens()
