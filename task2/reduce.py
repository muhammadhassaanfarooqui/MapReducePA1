#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
currentkey = None
total = 0
for line in sys.stdin:
	key, value = line.strip().split('\t')
	if(key == currentkey):
		total = total + 1
	else:
		if currentkey:
			print (currentkey + '\t' + str(total))
		total = 1
		currentkey = key
if(key == currentkey):
	print (currentkey + '\t' + str(total))