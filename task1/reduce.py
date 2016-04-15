#!/usr/bin/python

import sys

oldKey = None
value = ""
trips = []
fares = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
    	thisKey, thisValue = data_mapped
	values = thisValue.strip().split(",")
    	if oldKey and oldKey != thisKey:
		for trip in trips:
			for fare in fares:
				print oldKey+"\t",",".join(trip)+","+",".join(fare)
        	oldKey = thisKey;
		trips = []
		fares = []
	
	oldKey = thisKey
	if(values[0] == "T"):
		trips.append(values[1:])
	else:
		fares.append(values[1:])
    	

if oldKey != None:
    for trip in trips:
	for fare in fares:
		print oldKey+"\t",",".join(trip)+","+",".join(fare)
