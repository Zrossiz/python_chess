class Board:

    def __int__(self):
        board = self.draw_cells()

    def draw_cells(self):
        cells = []
        for i in range(1, 9):
            row = []
            for j in range(1, 9):
                if i % 2 != 0:
                    if j % 2 != 0:
                        row.append('white')
                    else:
                        row.append('black')
                else:
                    if j % 2 != 0:
                        row.append('black')
                    else:
                        row.append('white')
            cells.append(row)
        return cells
