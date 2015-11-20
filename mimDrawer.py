#!/usr/bin/env python2.7

#import pylab
#from pylab import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plot
import numpy

def quartCircle(precision):
    unit = float(1) / float(precision)

    x = [unit * i for i in range(precision + 1)]
    y = [numpy.sqrt(1 - (unit * i)**2) for i in range(precision + 1)]
    #x,y = [(unit * i, numpy.sqrt(1 - (unit * i)**2)) for i in range(precision)]
    return x,y

def mirrorHor(x,y):
    x = x + x
    yTemp = [ -i for i in y ]
    y = y + yTemp
    return x,y

def mirrorVert(x,y):
    xTemp = [ -i for i in x ]
    x = x + xTemp
    y = y + y
    return x,y

def shift(x, c):
    x = map(lambda n: n + c, x)
    return x

def scale(x, c):
    x = map(lambda n: c * n, x)
    return x

def drawLine(p1, p2, precision):
    line = [ (1 - (float(1)/float(t))) * (p2 - p1) for t in range(precision + 1)]
    print line
    return line[0], line[1]

headX,headY = mirrorVert(*mirrorHor(*quartCircle(100)))
headY = scale(headY, 1.5)

leftEyeX, leftEyeY = mirrorVert(*mirrorHor(*quartCircle(100)))
leftEyeX = scale(leftEyeX, 0.25)
leftEyeY = scale(leftEyeY, 0.25)
leftEyeX = shift(leftEyeX, -0.35)
leftEyeY = shift(leftEyeY, 0.25)

rightEyeX, rightEyeY = mirrorVert(leftEyeX, leftEyeY)

lineX, lineY = drawLine(numpy.array([0,-1]), numpy.array([-1,-1]), 10)

fullX = headX + leftEyeX + rightEyeX + lineX
fullY = headY + leftEyeY + rightEyeY + lineY

plot.scatter(fullX,fullY)
plot.axis([-2,2,-2,2])
plot.savefig('plot.png')
