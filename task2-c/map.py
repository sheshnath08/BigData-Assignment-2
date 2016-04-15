#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	tempkey,value = data
	values = value.split(",")
	pass_count = int(values[3])
	print pass_count,"\t",1
