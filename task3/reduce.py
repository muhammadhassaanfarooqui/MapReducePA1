#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
currentkey = None
count = 0
total = 0
for line in sys.stdin:
	if(len(line) > 10):
		key, amountDue = line.strip().split('\t')
		
		try:
			amountDue = float(amountDue)
		except ValueError:
			continue

		if(key == currentkey):
			total = total + amountDue
			count = count + 1
		else:
			if currentkey:
				print currentkey + '\t' + str(total) + ', ' + ("%.2f" % (total/count))
			count = 1
			total = amountDue
			currentkey = key
if(key == currentkey):
	print currentkey + '\t' + str(total) + ', ' + ("%.2f" % (total/count))