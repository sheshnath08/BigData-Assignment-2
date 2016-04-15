#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2 :
		continue
    	count = count + 1

print count


