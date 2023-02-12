#! /usr/bin/python

import sys

stat = {}
for line in sys.stdin:
    line = line.strip()
    date, change = line.split(',')
    change = int(change)
    if change not in stat:
        stat[change] = 0
    stat[change] += 1
for k, v in sorted(stat.items()):
    if k >= 0:
        print('+++ %d%%-%d%% for %d days' % (k, k + 1, v))
    else:
        print('--- %d%%-%d%% for %d days' % (-k, -(k - 1), v))
