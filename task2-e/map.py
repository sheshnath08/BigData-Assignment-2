#!/usr/bin/python

import sys

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	tempkey = data_mapped[0]
	keys = tempkey.strip().split(",")
	medallion = keys[0]
	pickupdatetime = keys[3].split(" ")
	pickup_date = pickupdatetime[0]
	print medallion+"\t"+pickup_date,1
	
