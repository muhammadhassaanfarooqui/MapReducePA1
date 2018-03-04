#!/usr/bin/env python

import sys
import string

currentkey = None
total = 0
for line in sys.stdin:
	key, value = line.strip().split('\t')
	
	colorOrMake = key.strip().split(',')[1]
	if(len(colorOrMake) == 0):
		continue

	if(key == currentkey):
		total = total + 1
	else:
		if currentkey:
			str1, colorOrMake1 = currentkey.split(',', 1)
			print (str1[1:] + '\t' + colorOrMake1 + ', ' + str(total))
		total = 1
		currentkey = key

if(key == currentkey):
	str1, colorOrMake1 = currentkey.split(',', 1)
	print (str1[1:] + '\t' + colorOrMake1 + ', ' + str(total))