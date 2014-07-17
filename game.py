import pygame, sys
from pygame.locals import *

class Game:

    def __init__(self, title):
        # Initialize variables and whatnot
        pygame.init()

        # Game speed/render speed constants
        self.TICKS_PER_SECOND = 25 # game speed
        self.SKIP_TICKS = 1000/self.TICKS_PER_SECOND #
        self.MAX_FRAMESKIP = 5 #

        self.nextGameTick = pygame.time.get_ticks()

        
        self.size = self.width, self.height = 400, 300
        self.screen = pygame.display.set_mode(self.size)
        self.screen = pygame.display.set_caption(title)


    def update(self):
        # Handle events such as keypresses
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Physics/collision code goes here


    def render(self, interpolation):
        # Draw code goes here


        # TODO: Change this to update rectangles
        pygame.display.update()
