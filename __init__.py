import pygame
import sys

from models.Board import Board
from models.Colors import Colors

board_class = Board()
cells = board_class.draw_cells()

FRAME = 800
CELL_SIZE = 100
BLACK_COLOR = (172, 130, 0)
WHITE_COLOR = (129, 217, 255)

pygame.display.set_caption('Chess')
game_window = pygame.display.set_mode((FRAME, FRAME))

game_window.fill(WHITE_COLOR)

for i in range(0, 8):
    for j in range(0, 8):
        cur_cell = cells[i][j]
        if cur_cell.color == Colors.BLACK:
            pygame.draw.rect(game_window, BLACK_COLOR,
                             (cur_cell.x * CELL_SIZE, cur_cell.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                             )
        else:
            pygame.draw.rect(game_window, WHITE_COLOR,
                             (cur_cell.x * CELL_SIZE, cur_cell.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                             )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
