#!/usr/bin/python

import sys
import csv
import StringIO

for line in sys.stdin:
	csv_file = StringIO.StringIO(line)
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		try:
			key = row[25]
			value = float(row[14]) + float(row[15])+float(row[17])
		        #new_val = value,float(row[17])
			if(value != 0):
				print str(key)+"\t"+str(value)+","+str(float(row[17])/value)
			else:
				print str(key)+"\t"+str(value)+","+str(float(value))
				value = 0
		except ValueError:
			continue
