#!/usr/bin/python

import sys

oldKey = None
value = 0
arr = []

for line in sys.stdin:
   data_mapped = line.strip().split("\t")
   key, valueN = data_mapped
   if oldKey and oldKey != key:
        arr.append([oldKey, value])
        oldKey = key;
        value = 0
   oldKey = key
   value = value + float(valueN)
if oldKey != None:
   arr.append([oldKey, value])
arr.sort(key=lambda x: x[1])
if(len(arr)<20):
   for i in range (len(arr)-1,-1, -1):
         op = arr[i]
         print op[0]+"\t","%.2f" %op[1]
else:
   for i in range (len(arr)-1,len(arr)-21, -1):
         op = arr[i]
         print op[0]+"\t","%.2f" %op[1]
