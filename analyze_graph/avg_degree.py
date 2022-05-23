#! /usr/bin/env python

import sys

link_cnt=[0]*101
#link_avg=[0]*151

for line in sys.stdin:
    line = line.rstrip()
    elem = line.split(',')
    time = int(elem[0])
    link_cnt[time] += 2

t = 0
for link in link_cnt:
    print(t, link/500)
    t += 1
