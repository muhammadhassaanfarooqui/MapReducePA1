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
    if(len(lineArr) == 22):
	    regState = lineArr[16].strip()
	    if ('NY' in regState.upper()):
	    	print ('NY' + '\t' + '1')
	    else:
	    	print ('Other' + '\t' + '1')

