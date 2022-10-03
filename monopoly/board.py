import pygame
from .constants import GREEN_BG, DEFAULT_MARGIN, BOARD_SIZE, BLACK, WHITE, BACKGROUND

#properties colors
BROWN = (149, 84, 54)
SOFT_BLUE = (170, 224, 270)
PINK = (217, 58, 150)
ORANGE = (247, 148, 29)
RED = (237, 27, 36)
YELLOW = (254, 242, 0)
GREEN = (31, 178, 90)
DARK_BLUE = (0, 114, 187)

class Board:
    def __init__(self):
        self.board = [[6],[6]]
        self.turn = 0

    def draw_property(self, window):
        pygame.draw.rect(window, BLACK, (25, 25, 100, 100))
        pygame.draw.rect(window, GREEN_BG, (26, 26, 98, 98))
        pygame.draw.rect(window, RED, (26, 26, 98, 20))

        
        pygame.draw.rect(window, BLACK, (25, 25, 100, 100))
        pygame.draw.rect(window, GREEN_BG, (26, 26, 98, 98))
        pygame.draw.rect(window, RED, (26, 26, 98, 20))

        
        pygame.draw.rect(window, BLACK, (25, 25, 100, 100))
        pygame.draw.rect(window, GREEN_BG, (26, 26, 98, 98))
        pygame.draw.rect(window, RED, (26, 26, 98, 20))

    def draw_board(self, window):
        window.fill(BACKGROUND)
        img = pygame.image.load('board.jpg')
        img.convert()
        rect = img.get_rect()
        window.blit(img, (25, 25))
        # pygame.draw.rect(window, GREEN_BG, (DEFAULT_MARGIN, DEFAULT_MARGIN, BOARD_SIZE, BOARD_SIZE ), )
        # self.draw_property(window)
        




    
                