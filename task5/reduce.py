#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
currentkey = None
count = 0
total = 0
ls = []
for line in sys.stdin:
	key, _ = line.strip().split('\t')
	
	if(key == currentkey):
		count = count + 1
	else:
		if currentkey:
			ls.append((key, count))
		count = 1
		currentkey = key
if(key == currentkey):
	ls.sort(key=lambda tup: tup[1])
	culprit = ls[-1:][0]
	print culprit[0] + '\t' + str(culprit[1])