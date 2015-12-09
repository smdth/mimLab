#!/usr/bin/env python2.7

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# custom imports
import mimLocator
#import mimDrawer

def main():
    p1 = [1,1,1]
    p2 = [0,2.5,0]
    p3 = [3,3,-0.5]


    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    p1 = [[1],[1],[1]]
    p2 = [[0,3],[2.5,3],[0,-0.5]]
    p3 = [[3],[3],[-0.5]]
    p2[0], p2[1] = np.meshgrid(p2[0],p2[1])
    ax.plot(*p1, label='asd', marker='o')
    ax.plot(*p2, label='asd', marker='o')
    ax.plot(*p3, label='asd', marker='o')
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()
