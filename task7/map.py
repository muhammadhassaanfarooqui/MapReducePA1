#!/usr/bin/env python
 
import sys
import string

for line in sys.stdin:
    lineArr = line.strip().split(',')
    date = lineArr[1]
    vCode = lineArr[2]
    print vCode + '\t' + date