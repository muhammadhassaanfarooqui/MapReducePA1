#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
currentkey = None
countNY = 0
countRest = 0
for line in sys.stdin:
	key, amountDue = line.strip().split('\t')

	if(key == currentkey and currentkey == 'NY'):
		countNY = countNY + 1
	elif(key == currentkey and currentkey != 'NY'):
		countRest = countRest + 1
	else:
		if (currentkey and currentkey == 'NY'):
			print currentkey + '\t' + str(countNY)
		elif(currentkey):
			print currentkey + '\t' + str(countRest)			
		count = 1
		total = amountDue
		currentkey = key


if(key == currentkey and currentkey == 'NY'):
	print currentkey + '\t' + str(countNY)
elif(key == currentkey):
	print currentkey + '\t' + str(countRest)