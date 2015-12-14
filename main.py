#!/usr/bin/env python2.7

import numpy as np
import subprocess
import sys

# custom imports
from mimLocator import *
import mimDrawer

def main():

    x = input("Get first coordinate?: ")

    scriptsPopen = subprocess.Popen(["python", "forward_kinematics.py"],
                                    stdout=subprocess.PIPE)
    scriptsPopen.wait()
    firstCoord = scriptsPopen.stdout.read().strip()

    y = input("Get first coordinate?: ")

    scriptsPopen = subprocess.Popen(["python", "forward_kinematics.py"],
                                    stdout=subprocess.PIPE)
    scriptsPopen.wait()
    secondCoord = scriptsPopen.stdout.read().strip()


    z = input("Get first coordinate?: ")

    scriptsPopen = subprocess.Popen(["python", "forward_kinematics.py"],
                                    stdout=subprocess.PIPE)
    scriptsPopen.wait()
    thirdCoord = scriptsPopen.stdout.read().strip()

    for l in firstCoord:
        if "X" in l:
            x = float(l.split(" ")[-1])
        if "Y" in l:
            y = float(l.split(" ")[-1])
        if "Z" in l:
            z = float(l.split(" ")[-1])

    firstCoord = [x,z,y]


    for l in secondCoord:
        if "X" in l:
            x = float(l.split(" ")[-1])
        if "Y" in l:
            y = float(l.split(" ")[-1])
        if "Z" in l:
            z = float(l.split(" ")[-1])

    secondCoord = [x,z,y]


    for l in thirdCoord:
        if "X" in l:
            x = float(l.split(" ")[-1])
        if "Y" in l:
            y = float(l.split(" ")[-1])
        if "Z" in l:
            z = float(l.split(" ")[-1])

    thirdCoord = [x,z,y]

    print firstCoord, secondCoord, thirdCoord

    l = Locator(firstCoord, secondCoord, thirdCoord)

    m = mimDrawer(firstCoord, secondCoord, thirdCoord)

    path = m.drawPath([[0,0],[1,0]])

    for p in path:
        tp = l.planeToCartesian(*p)
        scriptsPopen = subprocess.Popen(["python",
                                         "inverse_kinematics.py", tp[0],
                                         tp[1], tp[2], *l.q)


    #l = Locator([0.704303194185, -0.0689719359237, 0.0323706170901],[0.652674084377, -0.193660960182, 0.0901786136888],[0.839161903371, -0.0809407755815, 0.0937020338332])
    ##print l.planeToCartesian(1,1)
    #print l.planeToCartesian(float(sys.argv[1]), float(sys.argv[2]))

if __name__ == '__main__':
    main()
