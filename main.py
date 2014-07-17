import pygame, sys
from pygame.locals import *


def main():
    init()
    while True:
        update()
        draw()
    


def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def draw():
    pygame.display.update()


def init():
    pygame.init()
    size = width, height = 400, 300
    screen = pygame.display.set_mode(size)
    
if __name__ == "__main__":
    main()
