#!/usr/bin/env python

import sys
import string
currentkey = None
countNY = 0
countRest = 0
for line in sys.stdin:
	key, amountDue = line.strip().split('\t')

	if(key == currentkey and 'NY' == currentkey):
		countNY = countNY + 1
	elif(key == currentkey and 'NY' != currentkey):
		countRest = countRest + 1
	else:
		if (currentkey and currentkey == 'NY'):
			countNY = countNY + 1
			print (currentkey + '\t' + str(countNY))
		elif(currentkey):
			countRest = countRest + 1
			print (currentkey + '\t' + str(countRest))			
		total = amountDue
		currentkey = key


if(key == currentkey and 'NY' == currentkey):
	countNY = countNY + 1
	print (currentkey + '\t' + str(countNY))
elif(key == currentkey):
	countRest = countRest + 1
	print (currentkey + '\t' + str(countRest))