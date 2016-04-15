#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	value = data[1]
	values = value.split(",")
	fare_amount = float(values[11])
	if 0<= fare_amount <= 4.0:
		key = "a$0,4"
	elif 4.01 <= fare_amount <= 8.0:
		key = "b$4.01,8"
	elif 8.01 <= fare_amount <= 12.0:
		key = "c$8.01,12"
	elif 12.01 <= fare_amount <= 16.0:
		key = "d$12.01,16"
	elif 16.01 <= fare_amount <= 20.0:
		key = "e$16.01,20"
	elif 20.01 <= fare_amount <= 24.0:
		key = "f$20.01,24"
	elif 24.01 <= fare_amount <= 28.0:
		key = "g$24.01,28"
	elif 24.01 <= fare_amount <= 32.0:
		key = "h$28.01,32"
	elif 32.01 <= fare_amount <= 36.0:
		key = "i$32.01,36"
	elif 36.01 <= fare_amount <= 40.0:
		key = "j$36.01,40"
	elif 40.01 <= fare_amount <= 44.0:
		key = "k$40.01,44"
	elif 44.01 <= fare_amount <= 48.0:
		key = "l$44.01,48"
	elif 48.01 <= fare_amount :
		key = "m$48.01,infinite"
	else:
		continue
	print key+"\t"+"a"

