#!/usr/bin/python

import sys

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	tempkey,value = data_mapped
	keys = tempkey.strip().split(",")
	license = keys[1]
	medallion = keys[0]
	print license,"\t",medallion
	

		
