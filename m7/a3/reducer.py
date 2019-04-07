#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

friends = []

# input comes from STDIN
for line in sys.stdin:
	data = line.split("\t")
	data[0] = data[0].strip()
	data[1] = data[1].strip()
	one  = data[0]+","+data[1]
	two = data[1]+","+data[0]
	if one not in friends:
		friends.append(one)
	else : 
		friends.remove(one)
	if two not in friends:
		friends.append(two)
	else : 
		friends.remove(two)
for friend in friends:
	print "["+friend+"]"
#print len(friends)
			
	
    
