#!/usr/bin/env python
 
import sys
import string
import os
import re

for line in sys.stdin:
    if "\"" in line:
        lineArr = re.split(''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', line.strip())
        lineArr = [s.replace('\"', '') for s in lineArr]
    else:
        lineArr = line.strip().split(',')

    vColor, vMake = lineArr[-3:-1]
    if vColor is '':
    	vColor = 'NONE'
    if vMake is '':
    	vMake = 'NONE'
    
    print ('Zvehicle_color' + ', ' + vColor + '\t' + '1')
    print ('Avehicle_make' + ', ' + vMake + '\t' + '1')
        
