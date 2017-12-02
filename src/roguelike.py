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
import move
import itertools

XLIM = 600
YLIM = 600
NTILES = 15
dTILE = 40

Map = np.zeros([NTILES,NTILES])

Map[0,:] += 1
Map[-1,:] += 1
Map[1:-1,0] += 1
Map[1:-1,-1] += 1
Map[10,10] += 2

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
    brick_tile = pygame.image.load("../artlib/wall.png")
    brick_tile = pygame.transform.scale(brick_tile,(dTILE,dTILE))
    floor_tile = pygame.image.load("../artlib/floor.png")
    floor_tile = pygame.transform.scale(floor_tile,(dTILE,dTILE))
    charac_tile = pygame.image.load("../artlib/charac.png")
    charac_tile = pygame.transform.scale(charac_tile,(dTILE,dTILE))

    def tile_background():
        for x,y in itertools.product(range(0,XLIM,dTILE),range(0,YLIM,dTILE)):
            if(Map[int(x/dTILE),int(y/dTILE)] == 1):
                screen.blit(brick_tile,(x,y))
            else:
                screen.blit(floor_tile,(x,y))
    # Blit everything to screen
    
    def place_char():
        ii = np.where(Map == 2)
        screen.blit(charac_tile,(dTILE*ii[0],dTILE*ii[1]))
    
    screen.blit(background,(0,0))

    moved = 1
    angle = 90
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move.Move(Map,2)
                    dtheta = 0-angle
                    charac_tile = pygame.transform.rotate(charac_tile,dtheta)
                    angle = 0
                    moved = 1
                elif event.key == pygame.K_RIGHT:
                    move.Move(Map,3) 
                    dtheta = 180-angle
                    charac_tile = pygame.transform.rotate(charac_tile,dtheta)
                    angle = 180
                    moved = 1
                elif event.key == pygame.K_UP:
                    move.Move(Map,0) 
                    dtheta = 270-angle
                    charac_tile = pygame.transform.rotate(charac_tile,dtheta)
                    angle = 270
                    moved = 1
                elif event.key == pygame.K_DOWN:
                    move.Move(Map,1) 
                    dtheta = 90-angle
                    charac_tile = pygame.transform.rotate(charac_tile,dtheta)
                    angle = 90
                    moved = 1 
            if event.type == QUIT:
                return
        if(moved == 1):
            tile_background()
            place_char()
            pygame.display.flip()
            moved = 0
 

if __name__ == '__main__': main()
