#!/usr/bin/env python
 
import sys
import string
import os
import re

for line in sys.stdin:
    if "\"" in line:
        lineArr = re.split(''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', line)
        lineArr = [s.replace('\"', '') for s in lineArr]
    else:
        lineArr = line.strip().split(',')
    plateID = lineArr[14];
    regState = lineArr[16];
    print (plateID + ', ' + regState + '\t' + '1')
        
