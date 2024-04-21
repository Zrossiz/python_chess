class Cell:

    def __init__(self, board, x, y, color, figure):
        self.board = board
        self.x = x
        self.y = y
        self.color = color
        self.figure = figure or None

