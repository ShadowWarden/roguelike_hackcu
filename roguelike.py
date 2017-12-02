# init.py
# 
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Pygame init
#

import pygame
from pygame.locals import *
import os
import numpy as np
import image
import text

XLIM = 1024
YLIM = 768

def main():
    """ Main program """
    # Base inits. Safe to do multiple times. If fail, fails quietly
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((XLIM,YLIM))
    pygame.display.set_caption("Basic Pygame game")

    # Fill background
    # background = pygame.Surface(screen.get_size())
    # background = background.convert()
    # Colour's in RGB
    background = pygame.image.load("./artlib/bg.jpg")
    

    # Display text
    text.showtext(background,"Hello World!",XLIM/2,YLIM/2,50,[10,0,0]) 
    
    # Blit everything to screen
    screen.blit(background,(0,0))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()
