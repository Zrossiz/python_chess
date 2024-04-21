from .Colors import Colors


class Board:

    def draw_cells(self):
        cells = []
        for i in range(1, 9):
            row = []
            for j in range(1, 9):
                if i % 2 != 0:
                    if j % 2 != 0:
                        row.append(Colors.WHITE)
                    else:
                        row.append(Colors.BLACK)
                else:
                    if j % 2 != 0:
                        row.append(Colors.BLACK)
                    else:
                        row.append(Colors.WHITE)
            cells.append(row)
        return cells
