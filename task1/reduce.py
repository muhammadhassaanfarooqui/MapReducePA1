#!/usr/bin/env python

import sys
import string
currentkey = None
currentVals = None
total = 0
for line in sys.stdin:
	key, value = line.strip().split('\t')

	if(key == currentkey):
		total = total + 1
	else:
		if currentkey and len(currentVals) != 1 and total == 1:
			print (currentkey + '\t' + currentVals)
		total = 1
		currentkey = key
		currentVals = value
