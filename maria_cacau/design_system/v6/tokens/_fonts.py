from dataclasses import dataclass
from enum import Enum

from PyQt6.QtGui import QFontDatabase

from maria_cacau import asset


@dataclass(frozen=True)
class FontFamilyToken:
    name: str
    file: str | None  # None se a fonte for do sistema


class FontFamily(Enum):
    SANS = FontFamilyToken("Segoe UI Variable", asset("fonts/SegoeUIVariable.ttf"))
    MONO = FontFamilyToken("Cascadia Code",      asset("fonts/CascadiaCode.ttf"))
    ICON = FontFamilyToken("mc-icons",           asset("fonts/mc-icons.ttf"))


def load_fonts() -> None:
    """Registra as fontes customizadas do DS na aplicação. Chamar uma vez no boot."""
    [QFontDatabase.addApplicationFont(f.value.file) for f in FontFamily if f.value.file]
