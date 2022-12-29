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

PROPERTIES = [
    (700,700), (600,700), (500,700), (400,700), (300,700), (200,700), (100,700), (0,700),
    (0,600), (0,500), (0,400), (0,300), (0,200), (0,100), (0,0),
    (0,0), (100,0), (200,0), (300,0), (400,0), (500,0), (600,0), (700,0),
    (700,100), (700,200), (700,300), (700,400), (700,500), (700,600), (700,700),
]

class Board:
    def __init__(self):
        self.board = [[6],[6]]
        self.turn = 0
        self.properties = []

    def draw_player(self, window, pos, player):
        if player == 'dog':
            dog = pygame.image.load('./GA_Monopoly/monopoly/assets/dog.png')
            dog.convert()
            window.blit(dog, pos)
        if player == 'car':
            car = pygame.image.load('./GA_Monopoly/monopoly/assets/car.png')
            car.convert()
            window.blit(car, pos)
        if player == 'hat':
            hat = pygame.image.load('./GA_Monopoly/monopoly/assets/hat.png')
            hat.convert()
            window.blit(hat, pos)
        if player == 'penguin':
            penguin = pygame.image.load('./GA_Monopoly/monopoly/assets/penguin.png')
            penguin.convert()
            window.blit(penguin, pos)

    def draw_board(self, window):
        window.fill(BACKGROUND)
        img = pygame.image.load('./GA_Monopoly/monopoly/assets/board.jpg')
        img.convert()
        window.blit(img, (0, 0))
        self.draw_player(window, PROPERTIES[4], 'dog')
        
