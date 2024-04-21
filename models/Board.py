from models.Cell import Cell
from models.Colors import Colors


class Board:
    def __init__(self):
        self.board_cells = []

    def draw_cells(self):
        cells = []
        for i in range(1, 9):
            row = []
            for j in range(1, 9):
                if i % 2 != 0:
                    if j % 2 != 0:
                        row.append(
                            Cell(self, i - 1, j - 1, Colors.WHITE, None)
                        )
                    else:
                        row.append(
                            Cell(self, i - 1, j - 1, Colors.BLACK, None)
                        )
                else:
                    if j % 2 != 0:
                        row.append(
                            Cell(self, i - 1, j - 1, Colors.BLACK, None)
                        )
                    else:
                        row.append(
                            Cell(self, i - 1, j - 1, Colors.WHITE, None)
                        )
            cells.append(row)
        self.board_cells = cells
        return cells

    def get_cell(self, x, y):
        return self.board_cells[x][y]

