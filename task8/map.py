#!/usr/bin/env python
 
import sys
import string
import os

for line in sys.stdin:
    lineArr = line.strip().split(',')
    vColor = lineArr[19]
    vMake = lineArr[20]
    print 'ZColor' + ', ' + vColor + '\t' + '1'
    print 'AMake' + ', ' + vMake + '\t' + '1'
        
