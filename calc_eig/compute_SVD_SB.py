#!/usr/bin/env python
import numpy as np
import networkx as nx
from scipy.sparse.linalg import svds, eigsh
from scipy import sparse
from numpy import linalg as LA
from datasets import UCI_loader
from datasets import SBM_loader
from util import normal_util
import sys


'''
compute the eigenvalues for square laplacian matrix per time slice
input: list of networkx Graphs
output: list of 1d numpy array of diagonal entries computed from SVD
'''
def SVD_perSlice(G_times, directed=True, num_eigen=6, top=True, max_size=500):
    Temporal_eigenvalues = []
    activity_vecs = []  #eigenvector of the largest eigenvalue
    counter = 0

    for G in G_times:
        if (len(G) < max_size):
            for i in range(len(G), max_size):
                G.add_node(-1 * i)      #add empty node with no connectivity (zero padding)
        if (directed):
            L = nx.directed_laplacian_matrix(G)

        else:
            L = nx.laplacian_matrix(G)
            L = L.asfptype()

        if (top):
            which="LM"
        else:
            which="SM"

        u, s, vh = svds(L,k=num_eigen, which=which)
        # u, s, vh = randomized_svd(L, num_eigen)
        vals = s
        vecs = u

        max_index = list(vals).index(max(list(vals)))
        activity_vecs.append(np.asarray(vecs[max_index]))
        Temporal_eigenvalues.append(np.asarray(vals))

        print ("processing " + str(counter), end="\r")
        counter = counter + 1

    return (Temporal_eigenvalues, activity_vecs)


def compute_synthetic_SVD(d_name, f_name, data, num_eigen=499, top=True):

    #print(alpha)
    #edgefile = "datasets/SB_alpha_0.1/" + fname
    edgefile = str(d_name) + "/graph/" +str(f_name)

    '''
    careful
    '''
    max_nodes = 1000

    max_time = 151
    directed = False

    G_times = SBM_loader.load_temporarl_edgelist(edgefile)

    (Temporal_eigenvalues, activity_vecs) = SVD_perSlice(G_times, directed=directed, num_eigen=num_eigen, top=top, max_size=max_nodes)
    #normal_util.save_object(Temporal_eigenvalues, fname+ ".pkl")

    for i in range(len(G_times)):
        eig_file = str(d_name) + "/eig/"+ str(data) +"/t0_l10/eig_"+str(i)+".txt"
        #print(type(eig))
        f = open(eig_file, 'a')
        for j in range(499):
             f = open(eig_file, 'a')
             f.writelines(str(Temporal_eigenvalues[i][j])+ '\n')
        f.close()



def compute_legis_SVD(num_eigen=6, top=True):
    fname = "datasets/USLegis_processed/LegisEdgelist.txt"
    directed = False

    G_times = USLegis_loader.load_legis_temporarl_edgelist(fname)
    max_nodes = 102
    (Temporal_eigenvalues, activity_vecs) = SVD_perSlice(G_times, directed=directed, num_eigen=num_eigen, top=top, max_size=max_nodes)
    normal_util.save_object(Temporal_eigenvalues, "USLegis_L_singular.pkl")




def compute_canVote_SVD(num_eigen=338, top=True):
    fname = "datasets/canVote_processed/canVote_edgelist.txt"
    directed = True
    G_times = canVote_loader.load_canVote_temporarl_edgelist(fname)
    max_len = 0
    for G in G_times:
        if (len(G) > max_len):
            max_len = len(G)
    print (max_len)
    max_nodes = max_len
    (Temporal_eigenvalues, activity_vecs) = SVD_perSlice(G_times, directed=directed, num_eigen=num_eigen, top=top, max_size=max_nodes)
    normal_util.save_object(Temporal_eigenvalues, "canVote_L_singular.pkl")


def compute_UCI_SVD(num_eigen=1901, top=True):
    fname = "datasets/UCI/OCnodeslinks_chars.txt"
    max_nodes = 1901
    directed = True
    G_times = UCI_loader.load_temporarl_edgelist(fname, max_nodes=max_nodes)
    (Temporal_eigenvalues, activity_vecs) = SVD_perSlice(G_times, directed=directed, num_eigen=1900, top=top, max_size=max_nodes)
    for i in range(len(G_times)):
        eig_file = "datasets/UCI/eig/eig_"+str(i)+".txt"
        f = open(eig_file, 'a')
        for j in range(6):
             f = open(eig_file, 'a')
             f.writelines(str(Temporal_eigenvalues[i][j])+ '\n')
        f.close()

def main():
    #compute_UCI_SVD()
    args = sys.argv
    #print(args)
    d_name = args[1]
    f_name = args[2]
    data = args[3]
    compute_synthetic_SVD(d_name, f_name, data)

if __name__ == "__main__":
    main()
