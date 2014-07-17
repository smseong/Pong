import pygame, sys
from pygame.locals import *

class Game:

    def __init__(self):
        pygame.init()
        self.MAXFPS = 60
        self.mainClock = pygame.time.Clock()
        self.size = self.width, self.height = 400, 300
        self.screen = pygame.display.set_mode(self.size)


    def update(self, dt):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    def render(self):
        pygame.display.update()
