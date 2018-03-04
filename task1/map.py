#!/usr/bin/env python
 
import sys
import string
import os
import re
#(os.environ['mapreduce_map_input_file'].contains("parking"))

for line in sys.stdin:
    if "\"" in line:
        lineArr = re.split(''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', line)
        lineArr = [s.replace('\"', '') for s in lineArr]
    else:
        lineArr = line.strip().split(',')
    
    sNum = lineArr[0]
    fname = os.getenv('mapreduce_map_input_file')
    if ('open' in fname):
    	print (sNum + '\t' + 'o')
    else:
    	precint = lineArr[-16].strip()
    	pid = lineArr[-8].strip()
    	code = lineArr[2].strip()
    	date = lineArr[1].strip()
    	print (sNum + '\t' + '%s, %s, %s, %s' % (pid, precint, code, date))
    	



        
