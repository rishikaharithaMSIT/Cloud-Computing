#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

al = []
orders = []
lineItems = []
lineStr = ""

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	lineCopy = line.replace("\n","")
	if lineCopy != "" :    
		#print lineCopy
		line = line.replace("\n","")
		line = line.strip()
		line = line.strip("[")
		line = line.strip("]")
		data = line.split(",")
		if data[0].replace("\"","") == "order":
			orders.append(lineCopy)
		else :
			lineItems.append(lineCopy)
#print len(orders)
#print len(lineItems)
count = 0
for order in orders:	
	order = order.replace("\n","")
	order = order.strip()
	order = order.strip("[")
	order = order.strip("]")
	o = order
	data = order.split(",")
	#print data[1]
	for item in lineItems:		
		item = item.replace("\n","")
		item = item.strip()
		item = item.strip("[")
		item = item.strip("]")
		i = item
		data2 = item.split(",")
		#print data[1] +" "+data2[1]
		if data[1] == data2[1]:
			print "["+o+", " +i+"]"

		
		
 


