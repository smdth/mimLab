#!/usr/bin/env python2.7

#import pylab
from pylab import *
import numpy

def circle(precision):
    unit = float(1) / float(precision)

    x = [unit * i for i in range(precision)]
    y = [numpy.sqrt(1 - (unit * i)**2) for i in range(precision)]
    #x,y = [(unit * i, numpy.sqrt(1 - (unit * i)**2)) for i in range(precision)]

    return x,y

x,y = circle(10)

print x
print y

figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15,30,45, 10]

explode=(0, 0.05, 0, 0)
pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
savefig('foo.png')
