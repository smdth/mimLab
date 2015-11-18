#!/usr/bin/env python2.7

import numpy

mimLocP1 = numpy.array([0,0,0])
mimLocP2 = numpy.array([2,0,0])
mimLocP3 = numpy.array([0,0,2])

def mimLocInit(x,y):
    mimLocV12 = mimLocP2 - mimLocP1
    mimLocV23 = mimLocP3 - mimLocP1

    mimLocNormal = numpy.cross(mimLocV12, mimLocV23)

    print mimLocV12, mimLocV23

    mimLocPlaneX = mimLocV12 / numpy.linalg.norm(mimLocV12)
    mimLocPlaneY = mimLocV23 / numpy.linalg.norm(mimLocV23)

    print numpy.linalg.norm(mimLocV12), numpy.linalg.norm(mimLocV23)
    print mimLocPlaneX, mimLocPlaneY, mimLocNormal

    mimLocPoint = (x * mimLocPlaneX) + (y * mimLocPlaneY)

    print mimLocPoint

