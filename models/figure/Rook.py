from models.Colors import Colors
from models.figure.Figure import Figure, FiguresNames


class Rook(Figure):

    def __init__(self, color, cell):
        super().__init__(color, cell)
        self.logo = '/assets/white-rook.png' if color == Colors.WHITE else '/assets/white-rook.png'
        self.name = FiguresNames.ROOK
