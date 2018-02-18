#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values (if needed; your code goes here)
A = [None]*n;
B = [None]*n;


currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	#Remove leading and trailing whitespace
	line = line.strip()

	#Get key/value 
	key, value = line.split('\t',1)

	#Parse key/value input (your code goes here)

	
	mat, idx, val = value.split(' ') 
	val = float(val)
	idx = int(idx)
	
	#If we are still on the same key...
	if key==currentkey:
		if(mat == 'A'):
			A[idx] = val;
		else:
			B[idx] = val;
		#Process key/value pair (your code goes here)

	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:
			row, col = currentkey.split(' ')
			res = 0;
			for i in range(0, n):
				res = res + A[i]*B[i]
			#compute/output result to STDOUT (your code goes here)
			print('('+str(row)+',' +str(col)+')'+', '+ str(res))
		
		A = [None]*n
		B = [None]*n	
		currentkey = key
		
		#Process input for new key (your code goes here)
		if(mat == 'A'):
			A[idx] = val;
		else:
			B[idx] = val;


#Compute/output result for the last key (your code goes here)

res = 0;
row, col = currentkey.split(' ')
for i in range(0, n):
	res = res + A[i]*B[i]
#compute/output result to STDOUT (your code goes here)
print('('+str(row)+','+str(col)+')'+', '+str(res))

