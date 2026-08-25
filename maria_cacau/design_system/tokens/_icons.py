from dataclasses import dataclass
from enum import IntEnum, StrEnum

from PyQt6.QtGui import QColor


class Icon(StrEnum):
    """
    Catálogo de glifos da fonte mc-icons. Valores unicode são placeholders
    sequenciais — serão substituídos pelos codepoints reais quando a
    mc-icons.ttf for gerada.
    """

    PRODUCTS = ""   # grid 4 quadrados — nav Produtos
    DELIVERY = ""   # caminhão        — nav Entregas
    SEARCH   = ""   # lupa            — botão Consultar
    SAVE     = ""   # disquete        — botão Salvar
    MONITOR  = ""   # tela            — empty state
    CHECK    = ""   # checkmark       — notice / sucesso
    CALENDAR = ""   # calendário      — date picker (filter bar)


class IconSize(IntEnum):
    SM = 13   # botões
    MD = 15   # nav items, notice, status
    LG = 36   # empty state


@dataclass(frozen=True)
class IconStyle:
    size:  int
    color: QColor | None = None   # None = herda cor do contexto (texto adjacente)
