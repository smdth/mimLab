#! /usr/bin/env python

# Baxter needs an orientation quaternion instead of a rotational matrix. This script will help you calculate that.

import math
import numpy

###########
# Data: remove this when implementing the script in your code

X = numpy.matrix([-0.35166069, 0.87973912, -0.31999036])
Y = numpy.matrix([-0.84929275, -0.15604792, 0.50433211])
Z = numpy.matrix([ 0.39374686, 0.44911927, 0.80203197])
###########


# Given 3 normalised vectors X Y Z (which are the column of the rotational matrix you should have found!) you can obtain the quaternion with the following calculation:
w = math.sqrt(1+X[0,0]+Y[0,1]+Z[0,2])/2
x = (Y[0,2] - Z[0,1])/(4*w)
y = (Z[0,0] - X[0,2])/(4*w)
z = (X[0,1] - Y[0,0])/(4*w)

# Then you can feed the x,y,z,w values to the inverse kinematics function.
print("Resulting quaternion should be something like [0.7 0 0 0.7].")
print("Calculated value:")
print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))
print("w: " + str(w))
