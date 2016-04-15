#!/usr/bin/python

import sys

oldKey = None
total_toll = 0
total_amount = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 3 :
		continue
	thisKey, thisAmount,thisToll = data_mapped
	if oldKey and oldKey != thisKey:
		print oldKey.strip()+"\t","%.2f"%total_amount+","+"%.2f"%total_toll
		total_toll = 0
		total_amount = 0
		oldKey = thisKey
	oldKey = thisKey
	total_toll += float(thisToll)
	total_amount += float(thisAmount) 
	
if oldKey != None:
    print oldKey.strip()+"\t","%.2f"%total_amount+","+"%.2f"%total_toll
