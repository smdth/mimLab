#!/usr/bin/env python2.7

import numpy

p1 = numpy.array([0,0,0])
p2 = numpy.array([2,0,0])
p3 = numpy.array([0,0,2])

def mimLocInit(x,y):
    v12 = p2 - p1
    v13 = p3 - p1

    planeNormal = numpy.cross(v12, v13)

    print v12, v13

    axisX = v12 / numpy.linalg.norm(v12)
    axisY = v13 / numpy.linalg.norm(v13)

    print numpy.linalg.norm(v12), numpy.linalg.norm(v13)
    print axisX, axisY, planeNormal

    point = (x * axisX) + (y * axisY)

    print point

