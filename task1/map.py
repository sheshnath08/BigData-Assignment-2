#!/usr/bin/python

import sys

index = 3
key = None
value=""

for line in sys.stdin:
	if "medallion" in line:
		continue
	data = line.strip().split(",")	
	if len(data) is 14: 
		index = 5
		value = "T"
		
	else:
		index = 3
		value = "F"
        
	key= data[0]+","+data[1]+","+data[2]+","+data[index]
	for i in range(3,len(data)):
		if  i is index:
			continue
		else:
			value = value+","+data[i]
			
	print key+"\t"+value
	value=""

