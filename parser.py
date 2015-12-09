#!/bin/env python

import sys

print sys.argv[1]
print sys.argv[1].split("[")
print sys.argv[1].split("[")[-1].split("]")[0]
