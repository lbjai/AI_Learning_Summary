#! /usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    date, change = line.split(',')
    change = int(change)
    print('%s,%d' % (date, change))
