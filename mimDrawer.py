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
    x = [ p1[0] + (1 - (float(t)/float(precision))) * (p2[0] - p1[0]) for t in
         range(precision + 1)]
    y = [ p1[1] + (1 - (float(t)/float(precision))) * (p2[1] - p1[1]) for t in
         range(precision + 1)]
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
headX, headY = quartCircle(100)[0], shift(quartCircle(100)[1], 0.8)
headX,headY = genericAppend((headX, headY),
                            (drawLine([1,0.8], [1,0], 100)[0][::-1],
                             drawLine([1,0.8], [1,0], 100)[1][::-1]))
headX,headY = mirrorVert(*mirrorHor(headX, headY))

head = headX, headY

### DRAW LEFT EYE ###

leftEyeX, leftEyeY = mirrorVert(*mirrorHor(*quartCircle(100)))
leftEyeX = scale(leftEyeX, 0.3)
leftEyeY = scale(leftEyeY, 0.3)
leftEyeX = shift(leftEyeX, -0.35)
leftEyeY = shift(leftEyeY, 0.55)

leftEye = leftEyeX, leftEyeY

### DRAW RIGHT EYE ###

rightEyeX, rightEyeY = mirrorVert(*mirrorHor(*quartCircle(100)))
rightEyeX = scale(rightEyeX, 0.3)
rightEyeY = scale(rightEyeY, 0.3)
rightEyeX = shift(rightEyeX, 0.4)
rightEyeY = shift(rightEyeY, 0.55)

rightEye = rightEyeX, rightEyeY

### DRAW HAIR ###

hair = [[-1,0], [-1.5,0.5], [-1,0.5], [-1.4,1], [-0.75,1], [-1.2,1.7],
        [-0.47,1.4], ]
#lineX, lineY = drawPath(hair, 10)


### DRAW MOUTH ###

mouth = quartCircle(100)
mouth = scale(mouth[0], 1.2), scale(mouth[1], 0.2)
mouth = shift(mouth[0], -0.5), shift(mouth[1], -0.8)

### DRAW DETAILS ###

## EYES ##
detail1 = quartCircle(100)[0], tuple(map(lambda n: -n, quartCircle(100)[1]))
detail1 = scale(detail1[0], 0.3), scale(detail1[1], 0.2)
detail1 = shift(detail1[0], -0.38), shift(detail1[1], 0.3)

detail2 = quartCircle(100)[0][::-1], tuple(map(lambda n: -n,
                                               quartCircle(100)[1]))
detail2 = scale(detail2[0], 0.3), scale(detail2[1], 0.2)
detail2 = shift(detail2[0], 0.16), shift(detail2[1], 0.3)

detail3 = drawPath([[-0.3, 0.55], [-0.3, 0.45], [-0.25, 0.5], [-0.35, 0.5]],
                   10)
detail4 = drawPath([[0.35, 0.6], [0.35, 0.5], [0.3, 0.55], [0.4, 0.55]], 10)


#fullX = headX + leftEyeX + rightEyeX + lineX
#fullY = headY + leftEyeY + rightEyeY + lineY

#plot.scatter(fullX,fullY)
plot.plot(*head)
plot.plot(*leftEye)
plot.plot(*rightEye)
plot.plot(*mouth)
plot.plot(*detail1)
plot.plot(*detail2)
plot.plot(*detail3)
plot.plot(*detail4)
plot.axis([-4,4,-4,4])
plot.axes().set_aspect('equal', 'datalim')
#plot.savefig('plot.png')
plot.show()
