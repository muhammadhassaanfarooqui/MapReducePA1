#!/usr/bin/env python

import sys
import string

def getAvg(total, num):
	return float(total)/float(num)


currentkey = None
weekendTotal = 0
weekDayTotal = 0
WEEKEND_DAYS = [5, 6, 12, 13, 19, 20, 26, 27]
NUM_WEEKDAYS = 23
NUM_WEEKENDDAYS = 8
for line in sys.stdin:
	
	key, value = line.strip().split('\t')
	_, month, day = value.split('-')
	try:
		month = int(month)
		day = int(day)
	except ValueError:
		continue
	
	if(key == currentkey):
		if(day in WEEKEND_DAYS):
			weekendTotal = weekendTotal + 1
		else:
			weekDayTotal = weekDayTotal + 1
	else:
		if currentkey:
			print (currentkey + '\t' + ("%.2f" % getAvg(weekendTotal, NUM_WEEKENDDAYS)) + ', ' + ("%.2f" % getAvg(weekDayTotal, NUM_WEEKDAYS))) 
		if(day in WEEKEND_DAYS):
			weekendTotal = 1
			weekDayTotal = 0
		else:
			weekDayTotal = 1
			weekendTotal = 0
		currentkey = key

if(key == currentkey):
	print (currentkey + '\t' + ("%.2f" % getAvg(weekendTotal, NUM_WEEKENDDAYS)) + ', ' + ("%.2f" % getAvg(weekDayTotal, NUM_WEEKDAYS)))