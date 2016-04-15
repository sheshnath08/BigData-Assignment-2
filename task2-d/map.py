#!/usr/bin/python

import sys

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	tempkey,value = data_mapped
	keys = tempkey.strip().split(",")
	datetimeKey = keys[3]
	finalkey = datetimeKey.split(" ")
	dateKey = finalkey[0]
	values = value.split(",")
	totalAmount = float(values[11])+float(values[12])+float(values[14])
	tollAmount = float(values[15])
	print dateKey,"\t",totalAmount,"\t",tollAmount

		
