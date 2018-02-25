#!/usr/bin/env python

import sys
import string
currentkey = None
total = 0
for line in sys.stdin:
	key, value = line.strip().split('\t')
	
	colorOrMake = key.split(', ')[1]
	if(len(colorOrMake) == 0):
		continue

	if(key == currentkey):
		total = total + 1
	else:
		if currentkey:
			print currentkey[1:] + '\t' + str(total)
		total = 1
		currentkey = key
if(key == currentkey):
	print currentkey[1:] + '\t' + str(total)