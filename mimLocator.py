#!/usr/bin/env python2.7

import numpy as np

class Locator:
    def __init__(self, p1, p2, p3):

        # initialize points
        self.p1 = np.array(p1)
        self.p2 = np.array(p2)
        self.p3 = np.array(p3)

        # set vectors form p1 to p2 and from p1 to p3
        self.v12 = self.p2 - self.p1
        self.v13 = self.p3 - self.p1

        # calculate the normal to v12 and v13
        self.n = np.cross(self.v12, self.v13)
        self.n = self.n / np.linalg.norm(self.n)

        # calculate corresponding axes of the plane, having p1 as base
        # axisX = v12 / |v12|
        self.axisX = self.v12 / np.linalg.norm(self.v12)
        # axisY = (v12 x n) / |v12 x n|
#        self.axisY = (np.cross(self.v12, self.n)) / \
#                            np.linalg.norm(np.cross(self.v12, self.n))
        self.axisY = np.cross(self.n, self.axisX)
        self.axisY = self.axisY / np.linalg.norm(self.axisY)

        #self.rot = np.matrix(self.axisX, self.axisY, self.n)

    def planeToCartesian(self, x, y):
        """Takes a point (x,y) on the plane the Locator was initialized for and
        transforms it into (x,y,z) coordinates located in cartesian space.
        """
        p = (x * self.axisX) + (y * self.axisY)
        return p

