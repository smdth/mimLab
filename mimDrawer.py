#!/usr/bin/env python2.7

#import pylab
#from pylab import *
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import operator

def quartCircle(precision):
    unit = float(1) / float(precision)

    x = [unit * i for i in range(precision + 1)]
    y = [np.sqrt(1 - (unit * i)**2) for i in range(precision + 1)]
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
    return x[::-1],y[::-1]

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

class Drawer:
    def __init__(self, p1, p2, p3):

        # get height and width of window
        self.scale = min(np.linalg.norm(np.array(p1) - np.array(p2)),
                         np.linalg.norm(np.array(p1) - np.array(p3))) / 5
        self.shiftX = 1
        self.shiftY = 1
        print self.scale

    def normalize(self, x, y):
        x = scale(x, self.scale)
        y = scale(y, self.scale)
        x = shift(x, self.shiftX)
        y = shift(y, self.shiftY)
        return x,y


    def drawHead(self):
        headX, headY = quartCircle(100)[0], shift(quartCircle(100)[1], 0.8)
        headX,headY = genericAppend((headX, headY),
                                    (drawLine([1,0.8], [1,0], 100)[0],
                                     drawLine([1,0.8], [1,0], 100)[1]))
        headX,headY = mirrorVert(*mirrorHor(headX, headY))

        head = headX, headY

        return self.normalize(*head)

    def drawLeftEye(self):
        leftEyeX, leftEyeY = mirrorVert(*mirrorHor(*quartCircle(100)))
        leftEyeX = scale(leftEyeX, 0.3)
        leftEyeY = scale(leftEyeY, 0.3)
        leftEyeX = shift(leftEyeX, -0.35)
        leftEyeY = shift(leftEyeY, 0.55)

        leftEye = leftEyeX, leftEyeY
        return self.normalize(*leftEye)

    def drawRightEye(self):
        rightEyeX, rightEyeY = mirrorVert(*mirrorHor(*quartCircle(100)))
        rightEyeX = scale(rightEyeX, 0.3)
        rightEyeY = scale(rightEyeY, 0.3)
        rightEyeX = shift(rightEyeX, 0.4)
        rightEyeY = shift(rightEyeY, 0.55)

        rightEye = rightEyeX, rightEyeY
        return self.normalize(*rightEye)

    def drawMouth(self):
        mouth = quartCircle(100)
        mouth = scale(mouth[0], 1.2), scale(mouth[1], 0.2)
        mouth = shift(mouth[0], -0.5), shift(mouth[1], -0.8)
        return self.normalize(*mouth)

    def drawLeftEyeDetail1(self):
        detail1 = quartCircle(100)[0], tuple(map(lambda n: -n, quartCircle(100)[1]))
        detail1 = scale(detail1[0], 0.3), scale(detail1[1], 0.2)
        detail1 = shift(detail1[0], -0.38), shift(detail1[1], 0.3)
        return self.normalize(*detail1)

    def drawRightEyeDetail1(self):
        detail2 = quartCircle(100)[0][::-1], tuple(map(lambda n: -n,
                                                       quartCircle(100)[1]))
        detail2 = scale(detail2[0], 0.3), scale(detail2[1], 0.2)
        detail2 = shift(detail2[0], 0.16), shift(detail2[1], 0.3)
        return self.normalize(*detail2)

    def drawLeftEyeDetail2(self):
        detail3 = drawPath([[-0.3, 0.55], [-0.3, 0.45], [-0.25, 0.5], [-0.35, 0.5]],
                           10)
        return self.normalize(*detail3)
    def drawRightEyeDetail2(self):
        detail4 = drawPath([[0.35, 0.6], [0.35, 0.5], [0.3, 0.55], [0.4, 0.55]], 10)
        return self.normalize(*detail4)

    def drawMouthDetail1(self):
        detail5 = quartCircle(100)[0][::-1], tuple(map(lambda n: -n,
                                                       quartCircle(100)[1]))
        detail5 = quartCircle(100)[0][::-1], quartCircle(100)[1]
        detail5 = scale(detail5[0], 0.05), scale(detail5[1], 0.2)
        detail5 = shift(detail5[0], -0.6), shift(detail5[1], -0.7)
        return self.normalize(*detail5)

    def drawMouthDetail2(self):
        detail6 = quartCircle(100)[0], tuple(map(lambda n: -n,
                                                 quartCircle(100)[1]))
        detail6 = scale(detail6[0], 0.06), scale(detail6[1], 0.2)
        detail6 = shift(detail6[0], 0.7), shift(detail6[1], -0.7)
        return self.normalize(*detail6)

    def drawNose1(self):
        detail7 = quartCircle(100)
        detail7 = scale(detail7[0], 0.2), scale(detail7[1], 0.4)
        detail7 = detail7[0], shift(detail7[1], -0.3)
        return self.normalize(*detail7)

    def drawNose2(self):
        detail8 = quartCircle(100)[0], tuple(map(lambda n: -n,
                                                       quartCircle(100)[1]))
        detail8 = scale(detail8[0], 0.2), scale(detail8[1], 0.1)
        detail8 = detail8[0], shift(detail8[1], -0.3)
        return self.normalize(*detail8)

    def drawHair(self):
        detail9 = drawPath([[-1,0],[-2,0.3], [-1, 0.8], [-1.9, 1.3], [-1, 1.6],
                                [-1.35, 2.25], [-0.5, 2], [0, 2.6]])
        return self.normalize(*mirrorVert(*detail9))

def main():
    d = Drawer([0,0], [1,0], [1,1])
    plt.plot(*d.drawHead())
    plt.plot(*d.drawHair())
    plt.plot(*d.drawLeftEye())
    plt.plot(*d.drawLeftEyeDetail1())
    plt.plot(*d.drawLeftEyeDetail2())
    plt.plot(*d.drawRightEye())
    plt.plot(*d.drawRightEyeDetail1())
    plt.plot(*d.drawRightEyeDetail2())
    plt.plot(*d.drawMouth())
    plt.plot(*d.drawMouthDetail1())
    plt.plot(*d.drawMouthDetail2())
    plt.plot(*d.drawNose1())
    plt.plot(*d.drawNose2())
    plt.axis([0,5,0,5])
    plt.axes().set_aspect('equal', 'datalim')
    #plot.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    main()
