import pygame
import sys
from models.Board import Board

board_class = Board()
cells = board_class.draw_cells()

FRAME = 800
CELL_SIZE = 100
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

pygame.display.set_caption('Chess')
game_window = pygame.display.set_mode((FRAME, FRAME))

game_window.fill(WHITE_COLOR)

for i in range(0, 8):
    for j in range(0, 8):
        if cells[i][j] == 'black':
            pygame.draw.rect(game_window, BLACK_COLOR,
                             (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                             )
        else:
            pygame.draw.rect(game_window, WHITE_COLOR,
                             (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                             )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()