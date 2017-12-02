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
import itertools

XLIM = 1000
YLIM = 1000
NTILES = 10
dTILE = 100

Map = np.zeros([NTILES,NTILES])

Map[0,:] += 1
Map[-1,:] += 1
Map[1:-1,0] += 1
Map[1:-1,-1] += 1
Map[5,5] += 2

print(Map)

def main():
    """ Main program """
    # Base inits. Safe to do multiple times. If fail, fails quietly
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((XLIM,YLIM))
    pygame.display.set_caption("Basic Pygame game")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    # Colour's in RGB
    background.fill((250,250,250))
    #background = pygame.image.load("./artlib/bg.jpg")
    

    # Display text
    text.showtext(background,"Hello World!",XLIM/2,YLIM/2,50,[10,0,0]) 
   
    brick_tile = pygame.image.load("./artlib/wall.png")
    brick_tile = pygame.transform.scale(brick_tile,(dTILE,dTILE))
    floor_tile = pygame.image.load("./artlib/floor.png")
    floor_tile = pygame.transform.scale(floor_tile,(dTILE,dTILE))
    charac_tile = pygame.image.load("./artlib/charac.png")
    charac_tile = pygame.transform.scale(charac_tile,(dTILE,dTILE))

    def tile_background():
        for x,y in itertools.product(range(0,1000,dTILE),range(0,1000,dTILE)):
            if(Map[int(x/dTILE),int(y/dTILE)] == 1):
                screen.blit(brick_tile,(x,y))
            else:
                screen.blit(floor_tile,(x,y))
    # Blit everything to screen
    
    def place_char():
        ii = np.where(Map == 2)
        screen.blit(charac_tile,(100*ii[0],100*ii[1]))
    
    screen.blit(background,(0,0))

    move = 1
    while 1:
        if(move == 1):
            tile_background()
            place_char()
            pygame.display.flip()
            move = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                return


if __name__ == '__main__': main()
