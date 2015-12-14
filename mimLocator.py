#!/usr/bin/env python2.7

import numpy as np
import sys

class Locator:
    def __init__(self, p1, p2, p3):

        # initialize points
        self.p1 = np.array(p1)
        self.p2 = np.array(p2)
        self.p3 = np.array(p3)

        # set vectors form p1 to p2 and from p1 to p3
        self.v12 = self.p2 - self.p1
        self.v13 = self.p3 - self.p1

	self.v12 = self.v12 / np.linalg.norm(self.v12)
        # calculate the normal to v12 and v13
        self.n = np.cross(self.v12, self.v13)
        self.n = self.n / np.linalg.norm(self.n)

        # calculate corresponding axes of the plane, having p1 as base
        # axisX = v12 / |v12|
        self.axisX = self.v12 / np.linalg.norm(self.v12)
        self.axisY = np.cross(self.n, self.axisX)
        #self.axisY = self.axisY / np.linalg.norm(self.axisY)

        self.rot = np.matrix([np.array(self.axisX), np.array(self.axisY),
                              np.array(self.n)])

        self.q = [ 0,0,0,0 ]
        self.q[3] = np.sqrt(1 + self.rot[0,0] + self.rot[1,1] + self.rot[2,2]) \
                / 2
        self.q[0] = (self.rot[2,1] - self.rot[1,2]) / (4 * self.q[3])
        self.q[1] = (self.rot[0,2] - self.rot[2,0]) / (4 * self.q[3])
        self.q[2] = (self.rot[1,0] - self.rot[0,1]) / (4 * self.q[3])

	self.scale = np.linalg.norm(self.p2 - self.p1)

    def planeToCartesian(self, x, y):
        """Takes a point (x,y) on the plane the Locator was initialized for and
        transforms it into (x,y,z) coordinates located in cartesian space.
        """
        p = self.p1 + (x * self.scale * self.axisX) + (y * self.scale * self.axisY)
        return p

def main():
    l = Locator([float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])], [float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])], [float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9])])
    print l.planeToCartesian(sys.argv[10], sys.argv[11])

if __name__ == '__main__':
    main()
