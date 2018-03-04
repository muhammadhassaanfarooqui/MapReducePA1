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
    liscType = lineArr[2].strip()
    dueAmount = lineArr[12].strip()
    print (liscType + '\t' + dueAmount)
        
