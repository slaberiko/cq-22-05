#!/usr/bin/env python

import sys

args = sys.argv
dir_name = args[1]

mfile = "../" + dir_name + "/Zscore.txt"
score_s = []
score_l = []

score_d= []
score_t = []

for line in open(mfile, 'r'):
    line = line.split()
    s_s = float(line[1])
    s_l = float(line[2])
    score_s.append(s_s)
    score_l.append(s_l)

#print(score)

score_d.append(0)
score_t.append(0)
for i in range(1, len(score_s)):
    d_s = score_s[i] - score_s[i-1]
    d_l = score_l[i] - score_l[i-1]
    #print(d)
    #print(i, max(0, d_s), max(0, d_l))
    score_d.append(max(d_s, d_l))
    score_t.append(max(0, score_d[i]))

t = 0
for z in score_t:
    print(t, score_t[t])
    t += 1
'''
for i in range(len(score_s)):
    score_t.append(max(score_s[i], score_l[i]))

for i in range(1, len(score_t)):
    print(i, max(0, score_t[i] - score_t[i-1])
'''
