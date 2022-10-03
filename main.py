import pygame
from monopoly.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from monopoly.board import Board
from monopoly.control import Control
from monopoly.ranking import Ranking

FPS = 60

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Genopoly')

def main():
        run = True
        clock = pygame.time.Clock()
        board = Board()
        control = Control()
        ranking = Ranking()

        while run:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False     
            
            board.draw_board(WINDOW)
            # control.draw_panel(WINDOW)
            # ranking.draw_ranking(WINDOW)
            pygame.display.update()

        pygame.quit()

main()