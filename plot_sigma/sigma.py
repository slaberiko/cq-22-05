#!/usr/bin/env python

import sys

args=sys.argv
dir_name = str(args[1])
data=str(args[2])
dir_eig=str(args[3])

s_1=[]
s_2=[]
s_3=[]
s_4=[]
s_5=[]
s_6=[]
s_7=[]
s_8=[]
s_9=[]
s_10=[]

sort_s_1={}
sort_s_2={}
sort_s_3={}
sort_s_4={}
sort_s_5={}
sort_s_6={}
sort_s_7={}
sort_s_8={}
sort_s_9={}
sort_s_10={}

sigma_f = "../{0}/sigma/{1}/{2}/sigma_{3}.txt".format(dir_name, data, dir_eig, dir_eig)

s_1_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_1.txt".format(dir_name, data, dir_eig)
s_2_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_2.txt".format(dir_name, data, dir_eig)
s_3_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_3.txt".format(dir_name, data, dir_eig)
s_4_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_4.txt".format(dir_name, data, dir_eig)
s_5_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_5.txt".format(dir_name, data, dir_eig)
s_6_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_6.txt".format(dir_name, data, dir_eig)
s_7_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_7.txt".format(dir_name, data, dir_eig)
s_8_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_8.txt".format(dir_name, data, dir_eig)
s_9_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_9.txt".format(dir_name, data, dir_eig)
s_10_f = "../{0}/sigma/{1}/{2}/sigma_n/sigma_10.txt".format(dir_name, data, dir_eig)

d_s_1_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_1.txt".format(dir_name, data, dir_eig)
d_s_2_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_2.txt".format(dir_name, data, dir_eig)
d_s_3_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_3.txt".format(dir_name, data, dir_eig)
d_s_4_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_4.txt".format(dir_name, data, dir_eig)
d_s_5_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_5.txt".format(dir_name, data, dir_eig)
d_s_6_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_6.txt".format(dir_name, data, dir_eig)
d_s_7_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_7.txt".format(dir_name, data, dir_eig)
d_s_8_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_8.txt".format(dir_name, data, dir_eig)
d_s_9_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_9.txt".format(dir_name, data, dir_eig)
d_s_10_f = "../{0}/sigma/{1}/{2}/diff_sigma_n/diff_sigma_10.txt".format(dir_name, data, dir_eig)

d_a_s_1_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_1.txt".format(dir_name, data, dir_eig)
d_a_s_2_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_2.txt".format(dir_name, data, dir_eig)
d_a_s_3_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_3.txt".format(dir_name, data, dir_eig)
d_a_s_4_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_4.txt".format(dir_name, data, dir_eig)
d_a_s_5_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_5.txt".format(dir_name, data, dir_eig)
d_a_s_6_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_6.txt".format(dir_name, data, dir_eig)
d_a_s_7_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_7.txt".format(dir_name, data, dir_eig)
d_a_s_8_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_8.txt".format(dir_name, data, dir_eig)
d_a_s_9_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_9.txt".format(dir_name, data, dir_eig)
d_a_s_10_f = "../{0}/sigma/{1}/{2}/diff_abs_sigma_n/diff_abs_sigma_10.txt".format(dir_name, data, dir_eig)


sort_s_1_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_1.txt".format(dir_name, data, dir_eig)
sort_s_2_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_2.txt".format(dir_name, data, dir_eig)
sort_s_3_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_3.txt".format(dir_name, data, dir_eig)
sort_s_4_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_4.txt".format(dir_name, data, dir_eig)
sort_s_5_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_5.txt".format(dir_name, data, dir_eig)
sort_s_6_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_6.txt".format(dir_name, data, dir_eig)
sort_s_7_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_7.txt".format(dir_name, data, dir_eig)
sort_s_8_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_8.txt".format(dir_name, data, dir_eig)
sort_s_9_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_9.txt".format(dir_name, data, dir_eig)
sort_s_10_f = "../{0}/sigma/{1}/{2}/sort_diff_sigma_n/sort_diff_sigma_10.txt".format(dir_name, data, dir_eig)



#read

for line in open(sigma_f, 'r'):
    #line = line.rstrip()
    line = line.split()

    n = line[0]
    s = float(line[1])

    if n == '1':
        s_1.append(s)
    elif n == '2':
        s_2.append(s)
    elif n == '3':
        s_3.append(s)
    elif n == '4':
        s_4.append(s)
    elif n == '5':
        s_5.append(s)
    elif n == '6':
        s_6.append(s)
    elif n == '7':
        s_7.append(s)
    elif n == '8':
        s_8.append(s)
    elif n == '9':
        s_9.append(s)
    elif n == '10':
        s_10.append(s)

print("finish reading\n")
#sigma_n
f = open(s_1_f, 'w')
for i in range(len(s_1)):
    f.writelines(str(i)+ ' ' + str(s_1[i]) + '\n')
f.close()

f = open(s_2_f, 'w')
for i in range(len(s_2)):
    f.writelines(str(i)+ ' ' + str(s_2[i]) + '\n')
f.close()

f = open(s_3_f, 'w')
for i in range(len(s_3)):
    f.writelines(str(i)+ ' ' + str(s_3[i]) + '\n')
f.close()

f = open(s_4_f, 'w')
for i in range(len(s_4)):
    f.writelines(str(i)+ ' ' + str(s_4[i]) + '\n')
f.close()

f = open(s_5_f, 'w')
for i in range(len(s_5)):
    f.writelines(str(i)+ ' ' + str(s_5[i]) + '\n')
f.close()

f = open(s_6_f, 'w')
for i in range(len(s_6)):
    f.writelines(str(i)+ ' ' + str(s_6[i]) + '\n')
f.close()

f = open(s_7_f, 'w')
for i in range(len(s_7)):
    f.writelines(str(i)+ ' ' + str(s_7[i]) + '\n')
f.close()

f = open(s_8_f, 'w')
for i in range(len(s_8)):
    f.writelines(str(i)+ ' ' + str(s_8[i]) + '\n')
f.close()

f = open(s_9_f, 'w')
for i in range(len(s_9)):
    f.writelines(str(i)+ ' ' + str(s_9[i]) + '\n')
f.close()

f = open(s_10_f, 'w')
for i in range(len(s_10)):
    f.writelines(str(i)+ ' ' + str(s_10[i]) + '\n')
f.close()

#diff_sigma_n
f = open(d_s_1_f, 'w')
for i in range(len(s_1)-1):
    f.writelines(str(i+1)+ ' ' + str(s_1[i+1]-s_1[i]) + '\n')
f.close()

f = open(d_s_2_f, 'w')
for i in range(len(s_2)-1):
    f.writelines(str(i+1)+ ' ' + str(s_2[i+1]-s_2[i]) + '\n')
f.close()

f = open(d_s_3_f, 'w')
for i in range(len(s_3)-1):
    f.writelines(str(i+1)+ ' ' + str(s_3[i+1]-s_3[i]) + '\n')
f.close()

f = open(d_s_4_f, 'w')
for i in range(len(s_4)-1):
    f.writelines(str(i+1)+ ' ' + str(s_4[i+1]-s_4[i]) + '\n')
f.close()

f = open(d_s_5_f, 'w')
for i in range(len(s_5)-1):
    f.writelines(str(i+1)+ ' ' + str(s_5[i+1]-s_5[i]) + '\n')
f.close()

f = open(d_s_6_f, 'w')
for i in range(len(s_6)-1):
    f.writelines(str(i+1)+ ' ' + str(s_6[i+1]-s_6[i]) + '\n')
f.close()

f = open(d_s_7_f, 'w')
for i in range(len(s_7)-1):
    f.writelines(str(i+1)+ ' ' + str(s_7[i+1]-s_7[i]) + '\n')
f.close()

f = open(d_s_8_f, 'w')
for i in range(len(s_8)-1):
    f.writelines(str(i+1)+ ' ' + str(s_8[i+1]-s_8[i]) + '\n')
f.close()

f = open(d_s_9_f, 'w')
for i in range(len(s_9)-1):
    f.writelines(str(i+1)+ ' ' + str(s_9[i+1]-s_9[i]) + '\n')
f.close()

f = open(d_s_10_f, 'w')
for i in range(len(s_10)-1):
    f.writelines(str(i+1)+ ' ' + str(s_10[i+1]-s_10[i]) + '\n')
f.close()


#diff_abs_sigma_n, set_sort
f = open(d_a_s_1_f, 'w')
for i in range(len(s_1)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_1[i+1]-s_1[i])) + '\n')
    t_s = {i+1:abs(s_1[i+1]-s_1[i])}
    sort_s_1.update(t_s)
f.close()

f = open(d_a_s_2_f, 'w')
for i in range(len(s_2)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_2[i+1]-s_2[i])) + '\n')
    t_s = {i+1:abs(s_2[i+1]-s_2[i])}
    sort_s_2.update(t_s)
f.close()

f = open(d_a_s_3_f, 'w')
for i in range(len(s_3)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_3[i+1]-s_3[i])) + '\n')
    t_s = {i+1:abs(s_3[i+1]-s_3[i])}
    sort_s_3.update(t_s)
f.close()

f = open(d_a_s_4_f, 'w')
for i in range(len(s_4)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_4[i+1]-s_4[i])) + '\n')
    t_s = {i+1:abs(s_4[i+1]-s_4[i])}
    sort_s_4.update(t_s)
f.close()

f = open(d_a_s_5_f, 'w')
for i in range(len(s_5)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_5[i+1]-s_5[i])) + '\n')
    t_s = {i+1:abs(s_5[i+1]-s_5[i])}
    sort_s_5.update(t_s)
f.close()

f = open(d_a_s_6_f, 'w')
for i in range(len(s_6)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_6[i+1]-s_6[i])) + '\n')
    t_s = {i+1:abs(s_6[i+1]-s_6[i])}
    sort_s_6.update(t_s)
f.close()

f = open(d_a_s_7_f, 'w')
for i in range(len(s_7)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_7[i+1]-s_7[i])) + '\n')
    t_s = {i+1:abs(s_7[i+1]-s_7[i])}
    sort_s_7.update(t_s)
f.close()

f = open(d_a_s_8_f, 'w')
for i in range(len(s_8)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_8[i+1]-s_8[i])) + '\n')
    t_s = {i+1:abs(s_8[i+1]-s_8[i])}
    sort_s_8.update(t_s)
f.close()

f = open(d_a_s_9_f, 'w')
for i in range(len(s_9)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_9[i+1]-s_9[i])) + '\n')
    t_s = {i+1:abs(s_9[i+1]-s_9[i])}
    sort_s_9.update(t_s)
f.close()

f = open(d_a_s_10_f, 'w')
for i in range(len(s_10)-1):
    f.writelines(str(i+1)+ ' ' + str(abs(s_10[i+1]-s_10[i])) + '\n')
    t_s = {i+1:abs(s_10[i+1]-s_10[i])}
    sort_s_10.update(t_s)
f.close()

#sort
s_1_sorted = sorted(sort_s_1.items(), key=lambda x:-x[1])
s_2_sorted = sorted(sort_s_2.items(), key=lambda x:-x[1])
s_3_sorted = sorted(sort_s_3.items(), key=lambda x:-x[1])
s_4_sorted = sorted(sort_s_4.items(), key=lambda x:-x[1])
s_5_sorted = sorted(sort_s_5.items(), key=lambda x:-x[1])
s_6_sorted = sorted(sort_s_6.items(), key=lambda x:-x[1])
s_7_sorted = sorted(sort_s_7.items(), key=lambda x:-x[1])
s_8_sorted = sorted(sort_s_8.items(), key=lambda x:-x[1])
s_9_sorted = sorted(sort_s_9.items(), key=lambda x:-x[1])
s_10_sorted = sorted(sort_s_10.items(), key=lambda x:-x[1])

f = open(sort_s_1_f, 'w')
for i in range(len(s_1_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_1_sorted[i][0]), str(s_1_sorted[i][1])))
f.close()

f = open(sort_s_2_f, 'w')
for i in range(len(s_2_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_2_sorted[i][0]), str(s_2_sorted[i][1])))
f.close()

f = open(sort_s_3_f, 'w')
for i in range(len(s_1_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_3_sorted[i][0]), str(s_3_sorted[i][1])))
f.close()

f = open(sort_s_4_f, 'w')
for i in range(len(s_4_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_4_sorted[i][0]), str(s_4_sorted[i][1])))
f.close()

f = open(sort_s_5_f, 'w')
for i in range(len(s_5_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_5_sorted[i][0]), str(s_5_sorted[i][1])))
f.close()

f = open(sort_s_6_f, 'w')
for i in range(len(s_6_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_6_sorted[i][0]), str(s_6_sorted[i][1])))
f.close()

f = open(sort_s_7_f, 'w')
for i in range(len(s_7_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_7_sorted[i][0]), str(s_7_sorted[i][1])))
f.close()

f = open(sort_s_8_f, 'w')
for i in range(len(s_8_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_8_sorted[i][0]), str(s_8_sorted[i][1])))
f.close()

f = open(sort_s_9_f, 'w')
for i in range(len(s_9_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_9_sorted[i][0]), str(s_9_sorted[i][1])))
f.close()

f = open(sort_s_10_f, 'w')
for i in range(len(s_10_sorted)):
    f.writelines("{0} {1} {2}\n".format(str(i+1), str(s_10_sorted[i][0]), str(s_10_sorted[i][1])))
f.close()
