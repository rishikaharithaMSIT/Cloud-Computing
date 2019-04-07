#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    	# remove leading and trailing whitespace
	line = line.strip()
	line = line.replace(" ", "")
	if line != "":    
		line = line.strip("[")
		line = line.strip("]")
		data = line.split(",")
		print data[0].replace("\"","") +"\t"+data[1].replace("\"","")
