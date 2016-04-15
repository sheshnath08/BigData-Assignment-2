#!/usr/bin/python

import sys

key = None
value=""
for line in sys.stdin:
	if "medallion" in line:
		continue
	if ("\t" in line):
		data_mapped = line.strip().split("\t")
    	key, value = data_mapped
		keyDt = key.strip().split(",")
		value= "O,"+keyDt[1] +","+keyDt[2]+","+keyDt[3]+","+value
		print keyDt[0]+ "\t" ,value
        value=""
	else:
		data = line.strip().split(",")
        value = "V"
        for i in range(1,len(data)):
			value = value + "," +data[i]
		print data[0] + "\t" ,value
       	value = ""
