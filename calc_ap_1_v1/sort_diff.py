#!/usr/bin/env python

import sys

args = sys.argv
#alpha = str(args[1])
top_k = sys.argv[1]
dir_name = str(args[2])

mfile = "../" + dir_name +"/z_d.txt"
rfile = "../" + dir_name +"/ranking.txt"
hit_file = "../" + dir_name +"/Hit_at_n.txt"
# hit_file = "../" + dir_name +"/Hit_at_n_"+alpha+".txt"
#dfile = "../" + dir_name +"/diff.txt"

t_zscore = {}
diff = []
#change_point = [16, 31, 61, 76, 91, 106, 136]
change_point = [51]
hit = 0
n = len(change_point)

#ranking.txtを作成
f = open(rfile, 'w')
f.close()

#z_d.txtを読み取り
for line in open(mfile, 'r'):
    line = line.split()
    t = int(line[0])
    score = float(line[1])
    z = { t : score}
    t_zscore.update(z)


score_sorted = sorted(t_zscore.items(), key=lambda x:-x[1])#ソートしたZスコア

f = open(rfile, 'a')
f.writelines("ranking\n")
f.close()
#print("ranking")
for i in range(n):
    f = open(rfile, 'a')
    f.writelines(str(score_sorted[i][0])+" "+str(score_sorted[i][1])+"\n")
    f.close()
    #print(score_sorted[i][0], score_sorted[i][1])
    if score_sorted[i][0] in change_point:
        hit += 1

#f = open(hit_file, 'a')
#f.writelines("Hit at n\n")

#f.close()

f = open(hit_file, 'a')
f.writelines(top_k+" "+ str(hit/n)+"\n")
f.close()

f = open(rfile, 'a')
f.writelines("Hit_at_n"+" "+str(hit/n)+"\n")
f.close()

#print("Hit at n")
#print(hit/n)
#print('\n')

#ソートしたスコアを表示

sfile = "../" + dir_name + "/score_sorted.txt"
for i in range(len(score_sorted)):
    f = open(sfile, 'a')
    #f.writelines(str(score_sorted[i][0])+" "+str(score_sorted[i][1])+"\n")
    f.writelines(str(i+1) + " " + str(score_sorted[i][0]) +" "+ str(score_sorted[i][1])+"\n")
    f.close()
    #print(score_sorted[i][0], score_sorted[i][1])

#print('\n')
#for key i


"""
#Zscoreの差を計算して表示
for i in range(1, len(score_sorted)):
    d = score_sorted[i-1][1]-score_sorted[i][1]
    diff.append(d)

for i in range(len(diff)):

    print(i+1, i+2, diff[i])
"""

#7番目と8番目の差を計算して表示

# d = score_sorted[6][1]-score_sorted[7][1]
# f = open(dfile, 'a')
# f.writelines(top_k+" "+str(d)+"\n")
# f.close()
#print(d)
