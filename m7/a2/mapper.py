#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.strip("[")
    line = line.strip("]")
    # split the line into words
    data = line.split(",")
    # increase counters
    print data[0].replace("\"","") +"\t"+"1"
