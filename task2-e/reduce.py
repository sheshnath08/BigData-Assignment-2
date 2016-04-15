#!/usr/bin/python


import sys



oldKey = None
oldDate = None
day_count = 0
total_count = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2 :
		continue
    thisKey, thisdate = data_mapped
	if oldKey and oldKey != thisKey:
		print oldKey.strip()+"\t",str(total_count)+","+"%.2f"%float(float(total_count)/day_count)
		day_count = 0
		total_count = 0
		oldDate = None
		oldKey = thisKey
    oldKey = thisKey
	total_count += 1
    if thisdate != oldDate :
		day_count += 1
		oldDate = thisdate


if oldKey != None:
	print oldKey.strip()+"\t",str(total_count)+","+"%.2f"%float(float(total_count)/day_count)

