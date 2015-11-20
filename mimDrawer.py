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

X,Y = mirrorVert(*mirrorHor(*quartCircle(100)))

X = shift(X, 0.5)
Y = scale(Y, 1.5)


#x2 = [ -i for i in x]
#y2 = [ -i for i in y]

#x = x + x + x2 + x2
#y = y + y2 + y + y2

#x = map(lambda n: 0.5 * n, x)
#y = map(lambda n: 1 + n, y)


plot.scatter(X,Y)
plot.axis([-2,2,-2,2])
plot.savefig('plot.png')
