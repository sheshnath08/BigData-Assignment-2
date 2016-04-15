#!/usr/bin/python
import sys

oldKey = None
value = ""
outputDt = []
vehDt = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	thisKey, thisValue = data_mapped
	values = thisValue.strip().split(",")
    if oldKey and oldKey != thisKey:
		for op in outputDt:
			for veh in vehDt:
				print oldKey+"\t", ",".join(op) + "," + ",".join(veh)
        oldKey = thisKey;
		outputDt = []
		vehDt = []
	oldKey = thisKey
	if(values[0] == "O"):
		outputDt.append(values[1:])
	else:
		vehDt.append(values[1:])
   

if oldKey != None:
    for op in outputDt:
		for veh in vehDt:
			print oldKey+"\t", ",".join(op) + "," + ",".join(veh)
