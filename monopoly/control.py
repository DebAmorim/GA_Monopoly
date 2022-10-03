import pygame
from .constants import GREEN_BG, DEFAULT_MARGIN, CONTROL_WIDTH, CONTROL_HEIGHT

class Control:
    def __init__(self):
        self.control = []

    def draw_panel(self, window):
        pygame.draw.rect(window, GREEN_BG, (800, DEFAULT_MARGIN, CONTROL_WIDTH, CONTROL_HEIGHT ), )
                