import pygame, sys
from game import *
from pygame.locals import *


def main():
    game = Game('Pong')
    # Main game loop
    while True:

        loops = 0
        while pygame.time.get_ticks() > game.nextGameTick and loops < game.MAX_FRAMESKIP:
            
            game.update()

            game.nextGameTick += game.SKIP_TICKS
            loops += 1

        interpolation = float(pygame.time.get_ticks() + game.SKIP_TICKS - game.nextGameTick) / float(game.SKIP_TICKS)

        
        game.render(interpolation)
    

    
if __name__ == "__main__":
    main()
