from enum import Enum


class FiguresNames(Enum):
    FIGURE = 'Фигура'
    KING = 'Король'
    KNIGHT = 'Конь'
    PAWN = 'Пешка'
    QUEEN = 'Ферзь'
    ROOK = 'Ладья'
    BISHOP = 'Слон'


class Figure:

    def __init__(self, color, cell):
        self.color = color
        self.cell = cell
        self.cell.figure = self
        self.logo = None
        self.name = FiguresNames.FIGURE


