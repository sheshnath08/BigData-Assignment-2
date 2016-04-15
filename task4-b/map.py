#!/usr/bin/python

import sys
import csv
import StringIO

for line in sys.stdin:
  csv_file = StringIO.StringIO(line)
  csv_reader = csv.reader(csv_file)
  for record in csv_reader:
              key = record[29]
              value = float(record[14]) + float(record[15])+float(record[17])
              print key+"\t",value
              value = 0