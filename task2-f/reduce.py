#!/usr/bin/python

import sys

oldKey = None
medallions = []
total_count = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2 :
		continue
    thisKey, thismedallion = data_mapped
    if oldKey and oldKey != thisKey:
		print oldKey.strip()+"\t", len(medallions)
		oldKey = thisKey;
		medallions = []

    oldKey = thisKey
	medallions.append(thismedallion) 

if oldKey != None:
    print oldKey.strip()+"\t",len(medallions)
    

