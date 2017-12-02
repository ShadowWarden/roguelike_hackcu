# move.py
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Player movement functions
#

import numpy as np
import pygame
from pygame.locals import *
import os

def Move(Map,Dir):
    ii = np.where(Map == 2)
    if(Dir == 0):
        Map[ii[0],ii[1]] = 0
        Map[ii[0],ii[1]-1] = 2
    elif(Dir == 1):
        Map[ii[0],ii[1]] = 0
        Map[ii[0],ii[1]+1] = 2
    elif(Dir == 2):
        Map[ii[0],ii[1]] = 0
        Map[ii[0]-1,ii[1]] = 2
    elif(Dir == 3):
        Map[ii[0],ii[1]] = 0
        Map[ii[0]+1,ii[1]] = 2
