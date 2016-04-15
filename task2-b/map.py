#!/usr/bin/python

import sys

key = "1"
for line in sys.stdin:
	data = line.strip().split("\t")
	tempkey,value = data
	values = value.split(",")
	total_amount = float(values[16])
	if total_amount <= 10.0:
		print key,"\t",1