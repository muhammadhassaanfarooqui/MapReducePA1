#!/usr/bin/env python

import sys
import string
currentkey = None
count = 0
total = 0
for line in sys.stdin:
	arr = line.strip().split('\t')
	if(len(arr) == 2):
		key, amountDue = arr
		
		try:
			amountDue = float(amountDue)
		except ValueError:
			amountDue = 0

		if(key == currentkey):
			total = total + amountDue
			count = count + 1
		else:
			if currentkey:
				print (currentkey + '\t' + ("%.2f" % total) + ', ' + ("%.2f" % (total/count)))
			count = 1
			total = amountDue
			currentkey = key

if(key == currentkey):
	print (currentkey + '\t' + ("%.2f" % total) + ', ' + ("%.2f" % (total/count)))