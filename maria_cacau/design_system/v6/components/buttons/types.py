from enum import Enum


class DSButtonType(Enum):
    PRIMARY   = "primary"
    SECONDARY = "secondary"
    ICON      = "icon"

    @property
    def height(self) -> int:
        match self:
            case DSButtonType.PRIMARY | DSButtonType.SECONDARY:
                return 30
            case DSButtonType.ICON:
                return 30   # quadrado: height == width

    @property
    def is_square(self) -> bool:
        return self is DSButtonType.ICON

    @property
    def min_width(self) -> int | None:
        match self:
            case DSButtonType.ICON:
                return self.height
            case _:
                return 120   # mínimo recomendado pra botões de comando (Fluent/WinUI3)
