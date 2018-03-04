#!/usr/bin/env python

import sys
import string
currentkey = None
count = 0
total = 0
ls = []
for line in sys.stdin:
	key, _ = line.strip().split('\t')
	
	firstval = key.strip().split(',')
	if(len(firstval[0]) <= 2):
		continue
	if(key == currentkey):
		count = count + 1
	else:
		if currentkey:
			ls.append((currentkey, count))
		count = 1
		currentkey = key
if(key == currentkey):
	ls.sort(key=lambda tup: tup[1])
	culprit = ls[-1:][0]
	print (culprit[0] + '\t' + str(culprit[1]))
