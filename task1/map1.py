#!/usr/bin/env python
 
import sys
import string
import os

#(os.environ['mapreduce_map_input_file'].contains("parking"))

for line in sys.stdin:
    lineArr = line.strip().split(',')
    
    sNum = lineArr[0]
    if (sNum[0] == 'O'):
    	print sNum[1:] + '\t' + 'o'
    else:
    	precint = lineArr[6]
    	pid = lineArr[14]
    	code = lineArr[2]
    	date = lineArr[1]
    	print sNum[1:] + '\t' + '%s, %s, %s, %s' % (pid, precint, code, date)
    	



        
