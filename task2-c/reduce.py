#!/usr/bin/python


import sys

oldKey = None
count = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2 :
		continue
	thisKey, thisCount = data_mapped
	if oldKey and oldKey != thisKey:
		print oldKey.strip()+"\t",count
		count = 0
		oldKey = thisKey
	oldKey = thisKey
	count = count + 1

if oldKey != None:
	print oldKey.strip()+"\t",count
