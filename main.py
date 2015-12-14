#!/usr/bin/env python2.7

import numpy as np
import subprocess
import sys

# custom imports
from mimLocator import *
from mimDrawer import *

def main():

    x,y,z = 0,0,0
    x = input("Get first coordinate?: ")

    scriptsPopen = subprocess.Popen(["python", "forward_kinematics.py"],
                                    stdout=subprocess.PIPE)
    scriptsPopen.wait()
    firstCoord = scriptsPopen.stdout.read().strip()

    y = input("Get second coordinate?: ")

    scriptsPopen = subprocess.Popen(["python", "forward_kinematics.py"],
                                    stdout=subprocess.PIPE)
    scriptsPopen.wait()
    secondCoord = scriptsPopen.stdout.read().strip()


    z = input("Get third coordinate?: ")

    scriptsPopen = subprocess.Popen(["python", "forward_kinematics.py"],
                                    stdout=subprocess.PIPE)
    scriptsPopen.wait()
    thirdCoord = scriptsPopen.stdout.read().strip()

    for l in firstCoord.split("\n"):
        if "X" in l:
            x = float(l.split(" ")[-1])
        if "Y" in l:
            y = float(l.split(" ")[-1])
        if "Z" in l:
            z = float(l.split(" ")[-1])

    firstCoord = [x,z,y]


    for l in secondCoord.split("\n"):
        if "X" in l:
            x = float(l.split(" ")[-1])
        if "Y" in l:
            y = float(l.split(" ")[-1])
        if "Z" in l:
            z = float(l.split(" ")[-1])

    secondCoord = [x,z,y]


    for l in thirdCoord.split("\n"):
        if "X" in l:
            x = float(l.split(" ")[-1])
        if "Y" in l:
            y = float(l.split(" ")[-1])
        if "Z" in l:
            z = float(l.split(" ")[-1])

    thirdCoord = [x,z,y]

    print firstCoord, secondCoord, thirdCoord
   # firstCoord = [0.623791890947, -0.012931432131, -0.0246224299732]
   # secondCoord = [0.744245444214, 0.0430351361199, -0.00974796572852]
   # thirdCoord = [0.631311941661, 0.0576380496228, -0.146248721335]

    l = Locator(firstCoord, secondCoord, thirdCoord)

    m = Drawer(firstCoord, secondCoord, thirdCoord)

    path = scale(quartCircle(10)[0], 0.1), scale(quartCircle(10)[1], 0.1)

    for i in range(len(path[0])):
        tp = l.planeToCartesian(path[0][i], path[1][i])
	print tp
        scriptsPopen = subprocess.Popen(["python", "inverse_kinematics.py", str(tp[0]), str(tp[1]), str(tp[2]), str(l.q[0]), str(l.q[1]), str(l.q[2]), str(l.q[3])])
	scriptsPopen.wait()


    #l = Locator([0.704303194185, -0.0689719359237, 0.0323706170901],[0.652674084377, -0.193660960182, 0.0901786136888],[0.839161903371, -0.0809407755815, 0.0937020338332])
    ##print l.planeToCartesian(1,1)
    #print l.planeToCartesian(float(sys.argv[1]), float(sys.argv[2]))

if __name__ == '__main__':
    main()
