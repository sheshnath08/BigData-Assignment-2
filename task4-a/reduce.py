#!/usr/bin/python

import sys

oldKey = None
value = 0.0
count = 0
tip = 0.0
l = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	key, valueN = data_mapped
    amt , tips =valueN.split(",")
	if oldKey and oldKey != key:
		print oldKey + "\t" , str(count) + "," +str("%.2f" %value)+ "," +str("%.2f" %(tip/count*100))
        oldKey = key
		value = 0
        count = 0
        tip = 0
	oldKey = key
    count = count+1
	value = value + float(amt)
    tip = tip + float(tips)
if oldKey != None:
    print key + "\t" , str(count) + "," +str("%.2f" %value)+ "," +str("%.2f" %(tip/count*100))
