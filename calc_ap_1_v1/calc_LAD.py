#!/usr/bin/env python
#Zスコアを計算
import sys
import numpy as np
from numpy import linalg as LA
from sklearn.preprocessing import normalize

def set_Matrix(t: int, k: int, size: int, dir_name: str):
    M = []
    #C = []
    #vec = np.zeros(k)
    #print(vec)

    for i in range(0, size):
        vec = np.zeros(k)
        mfile = "../" + str(dir_name) + "/eig/eig_"+str(t-(size-i))+".txt"
        j = 0
        for line in open(mfile, 'r'):
            dat = line.split()
            if j > k-1:
                break
            elif float(dat[0])==0.0:
                continue
            else:
                elem = float(dat[0])
                vec[j] = elem
                #if j == k-1:
                #print(i, vec)
                j += 1
        M.append(vec)
    M = np.asarray(M).real
    M_n = normalize(M, norm = 'l2')
    M_t = np.array(M_n).T

    return M_t

def set_vector(t: int, k: int, dir_name: str):
    # 現在の時刻 t の固有値k個からベクトルを構成する．
    vec = np.zeros(k)
    V = []
    mfile = "../" + str(dir_name) + "/eig/eig_"+str(t)+".txt"
    i = 0
    for line in open(mfile, 'r'):
        dat = line.split()
        if i > k-1:
            break
        elif float(dat[0])==0.0:
            continue
        else:
            elem = float(dat[0])
            vec[i] = elem
            i += 1

    V.append(vec)
    V = np.asarray(V).real
    V_n = normalize(V, norm = 'l2')
    vec_n = V_n[0]
    """
    vec_n = vec/np.linalg.norm(vec, ord=2)
    #vec_n = normalize(vec, norm='l1')
    vec_n.sort()
    #print(vec_n)
    """
    return vec_n

def calc_svd(M):
    u, s, v = LA.svd(M, full_matrices=False)
    return u[:,0]

def calc_Zscore(cur_vec, n_v):
    cosine_similarity = np.dot(cur_vec, n_v)/ LA.norm(cur_vec) / LA.norm(n_v)
    z =  1 - abs(cosine_similarity)

    return z


#main
args = sys.argv

tmax = int(args[1]) # current time
k = int(args[2]) #top k of eig
s = int(args[3]) #size of short sliding windows
l = int(args[4]) #size of long sliding windows
dir_name = str(args[5])

sigma_f = "../"+ dir_name +"/sigma.txt"

for t in range(0, tmax):
    if( t < l ):
        print(t, 0, 0, 0)
        cur_vec = set_vector(t, k, dir_name)

        f = open(sigma_f, 'a')
        for i in range(len(cur_vec)):
            f.writelines("{0} {1}\n".format(str(i+1), abs(cur_vec[i])))
        f.close()
    else:
        #current time vector
        cur_vec = set_vector(t, k, dir_name)

        f = open(sigma_f, 'a')
        for i in range(len(cur_vec)):
            f.writelines("{0} {1}\n".format(str(i+1), abs(cur_vec[i])))
        f.close()

        C_s = set_Matrix(t, k, s, dir_name)

        C_l = set_Matrix(t, k, l, dir_name)

        typ_vec_s = calc_svd(C_s)
        Z_s = calc_Zscore(cur_vec, typ_vec_s)


        typ_vec_l = calc_svd(C_l)
        Z_l = calc_Zscore(cur_vec, typ_vec_l)

        Z_t = max(Z_s, Z_l)
        print(t, Z_s, Z_l, Z_t)
