#!/usr/bin/env python2.7

import mimLocator

loc = mimLocator.Locator([0,0,0],[1,0,0],[1,0,1])
print loc.axisX, loc.axisY
print loc.planeToCartesian(1,1)
