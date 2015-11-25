#!/usr/bin/env python2.7

#import pylab
#from pylab import *
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plot
import numpy
import operator

def quartCircle(precision):
    unit = float(1) / float(precision)

    x = [unit * i for i in range(precision + 1)]
    y = [numpy.sqrt(1 - (unit * i)**2) for i in range(precision + 1)]
    #x,y = [(unit * i, numpy.sqrt(1 - (unit * i)**2)) for i in range(precision)]
    return x,y

def mirrorHor(x,y):
    x = x + x[::-1]
    yTemp = [ -i for i in reversed(y) ]
    y = y + yTemp
    return x,y

def mirrorVert(x,y):
    xTemp = [ -i for i in reversed(x) ]
    x = x + xTemp
    y = y + y[::-1]
    return x,y

def shift(x, c):
    x = map(lambda n: n + c, x)
    return x

def scale(x, c):
    x = map(lambda n: c * n, x)
    return x

def drawLine(p1, p2, precision):
    x = [ p1[0] + (1 - (float(t)/float(precision))) * (p2[0] - p1[0]) for t in range(precision + 1)]
    y = [ p1[1] + (1 - (float(t)/float(precision))) * (p2[1] - p1[1]) for t in range(precision + 1)]
    return x,y

def lineAppend(l, p1, p2, precision):
    l = tuple(map(operator.add, l, drawLine(p1, p2, precision)))
    return l

def genericAppend(p1, p2):
    p1 = tuple(map(operator.add, p1, p2))
    return p1

def drawPath(path, precision=10):
    p = [],[]
    for i in range(len(path)-1):
        p = lineAppend(p, path[i], path[i+1], precision)

    return p

### DRAW HEAD ###
headX, headY = drawLine([0.2,2], [0,2], 10)
headX, headY = genericAppend((headX, headY), (shift(quartCircle(10)[0], 0.2),
                                              shift(quartCircle(10)[1], 1)))
headX,headY = genericAppend((headX, headY),
                            (drawLine([1.2,1], [1.2,0], 10)[0][::-1],
                             drawLine([1.2,1], [1.2,0], 10)[1][::-1]))
headX,headY = mirrorVert(*mirrorHor(headX, headY))

head = headX, headY

### DRAW LEFT EYE ###

leftEyeX, leftEyeY = mirrorVert(*mirrorHor(*quartCircle(100)))
leftEyeX = scale(leftEyeX, 0.25)
leftEyeY = scale(leftEyeY, 0.25)
leftEyeX = shift(leftEyeX, -0.35)
leftEyeY = shift(leftEyeY, 0.25)

### DRAW RIGHT EYE ###

rightEyeX, rightEyeY = mirrorVert(leftEyeX, leftEyeY)

hair = [[-1,0], [-1.5,0.5], [-1,0.5], [-1.4,1], [-0.75,1], [-1.2,1.7],
        [-0.47,1.4], ]
#lineX, lineY = drawPath(hair, 10)

#fullX = headX + leftEyeX + rightEyeX + lineX
#fullY = headY + leftEyeY + rightEyeY + lineY

#plot.scatter(fullX,fullY)
plot.plot(*head)
plot.plot(leftEyeX, leftEyeY)
plot.axis([-4,4,-4,4])
plot.axes().set_aspect('equal', 'datalim')
#plot.savefig('plot.png')
plot.show()
