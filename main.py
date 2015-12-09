#!/usr/bin/env python2.7

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# custom imports
from mimLocator import *
import mimDrawer

def main():

    l = Locator([0.704303194185, -0.0689719359237, 0.0323706170901],[0.652674084377, -0.193660960182, 0.0901786136888],[0.839161903371, -0.0809407755815, 0.0937020338332])
    #print l.planeToCartesian(1,1)
    print l.planeToCartesian(float(sys.argv[1]), float(sys.argv[2]))

if __name__ == '__main__':
    main()
