#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
ls = []
currentkey = None
for line in sys.stdin:
	print (line)
	print ("\n\n\n!!!!!!!!!!!!!!!!!!!!!\n\n\n")
	key, value = line.strip().split('\t')
	arr = value.split(', ')
	c = '' 
	pid = '' 
	precinct = '' 
	vCode = '' 
	issueDate = ''
	if(len(arr) == 1):
		ls.append(arr[0])
	else:
		print arr
		c, pid, issueDate, vCode, precinct = arr
		ls.append(c)

	if (key == currentkey):
		if(len(ls) > 1):
			print (c + "\t" + "P, " + pid + ", " + precinct + ", " + vCode + ", " + issueDate)
			ls = []

	currentkey = key

	
	


