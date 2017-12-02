# map.py
#
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Map building function
#

import numpy as np

NTILES = 20

def gen_map():
    Rmean = 5
    Rdiff = 0.25
    r = np.linspace(0,10,1001)
    R = np.exp(-(r-Rmean)**2/2/Rdiff**2)*0.01
    R /= np.sum(R)
    x = np.zeros(75)
    y = np.zeros(75)

    # Init map
    Map = np.zeros([NTILES,NTILES])

    # Create central room
    th = np.linspace(0,2*np.pi,75)
    for i in range(len(th)):
        rr = np.random.choice(r,p=R)
        print(rr)
        x[i] = rr*np.cos(th[i])+10
        y[i] = rr*np.sin(th[i])+10

    x = x.astype(int)
    y = y.astype(int)

    Map[x,y] = 1
    return Map
