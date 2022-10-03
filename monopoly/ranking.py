import pygame
from .constants import GREEN_BG, ROWS, BLACK, RANKING_WIDTH, RANKING_HEIGHT

class Ranking:
    def __init__(self):
        self.ranking = []

    def draw_ranking(self, window):
        pygame.draw.rect(window, GREEN_BG, (800, 300, RANKING_WIDTH, RANKING_HEIGHT ), )
                