#!/usr/bin/python


import sys

count = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	key1 = data_mapped[0].split("$")
	key = key1[1]
	if oldKey and oldKey != key:
		print oldKey+"\t",count
		count = 0
		oldKey = key
		oldKey = key
		count = count + 1
if oldKey:
	print oldKey+"\t",count
