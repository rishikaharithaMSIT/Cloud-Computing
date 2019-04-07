#!/usr/bin/env python
"""mapper.py"""

import sys

orders = []
lineItems = []
lineStr = ""
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.replace("\n","")
    line = line.strip()
    print line
