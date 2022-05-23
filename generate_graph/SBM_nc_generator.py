#! /usr/bin/env python3
'''
dataset generator for synthetic SBM dataset
'''
import numpy as np
import random
from networkx.utils import *
import re
import networkx as nx
from networkx import generators
import copy
import sys


'''
t u v w
'''
def to_edgelist(G_times, outfile):

    outfile = open(outfile,"w")
    tdx = 0
    for G in G_times:

        for (u,v) in G.edges:
            outfile.write(str(tdx) + "," + str(u) + "," + str(v) + "\n")
        tdx = tdx + 1
    outfile.close()
    print("write successful")


def SBM_snapshot(G_prev, alpha, sizes, probs):

    G_t = G_prev.copy()
    nodelist = list(range(0,sum(sizes)))
    G_new = nx.stochastic_block_model(sizes, probs, nodelist=nodelist)
    n = len(G_t)
    if (alpha == 1.0):
        return G_new

    for i in range(0,n):
        for j in range(i+1,n):
            #randomly decide if remain the same or resample
            #remain the same if prob > alpha
            prob = random.uniform(0, 1)
            if (prob <= alpha):
                if (G_new.has_edge(i,j) and not G_t.has_edge(i, j)):
                    G_t.add_edge(i,j)
                if (not G_new.has_edge(i,j) and G_t.has_edge(i, j)):
                    G_t.remove_edge(i,j)
    return G_t


'''
blocks is an array of sizes
inter is the inter community probability
intra is the intra community probability
'''
def construct_SBM_block(blocks, inter, intra):
    probs = []
    for i in range(len(blocks)):
        prob = [inter]*len(blocks)
        prob[i] = intra
        probs.append(prob)
    return probs

'''
generate just change points
inter_prob = p_{ex}
intra_prob = p_{in}
alpha = percent of connection resampled, alpha=0.0 means all edges are carried over
'''
def generate_change(inter_prob, intra_prob, alpha, nc):
    cps=[50]
    fname = "change_"+ str(inter_prob)+ "_"+ str(intra_prob) + "_" + str(alpha) + ".txt"

    cps_sizes = []
    cps_probs = []

    #let there be 500 nodes
    #sizes_1 = [100,100,100,100,100] #500 nodes total at all times
    sizes_1 = [83, 83, 83, 83, 84, 84]
    probs_1 = construct_SBM_block(sizes_1, inter_prob, intra_prob)

    if nc==2 or nc==4 or nc==10:
        sizes_2=[int(500/nc)]*nc
        #print(sizes_2)
    elif nc==6:
        sizes_2 = [83, 83, 83, 83, 84, 84]
    elif nc==8:
        sizes_2 = [62, 62, 62, 62, 63, 63, 63, 63]
    probs_2 = construct_SBM_block(sizes_2, inter_prob, intra_prob)

    sizes = sizes_1
    probs = probs_1
    maxt = 100
    G_0=nx.stochastic_block_model(sizes, probs)
    G_0 = nx.Graph(G_0)
    G_t = G_0
    G_times = []
    G_times.append(G_t)

    for t in range(maxt):
        if t < cps[0]:
            G_t = SBM_snapshot(G_t, alpha, sizes, probs)
            print(sizes)
            G_times.append(G_t)
            print ("generating " + str(t), end="\r")
        elif (t in cps):
            G_t = SBM_snapshot(G_t, 1.0, sizes_2, probs_2)
            print(sizes_2)
            G_times.append(G_t)
            print ("generating " + str(t), end="\r")

        else:
            G_t = SBM_snapshot(G_t, alpha, sizes_2, probs_2)
            print(sizes_2)
            G_times.append(G_t)
            print ("generating " + str(t), end="\r")

    #write the entire history of snapshots
    to_edgelist(G_times, fname)

'''
generate both change points and events
inter_prob = p_{ex}
intra_prob = p_{in}
increment specifies the incremental for p_{ex} during events
alpha = percent of connection resampled, alpha=0.0 means all edges are carried over
'''

def generate_event(inter_prob, intra_prob, alpha, nc):
    cps=[50]
    fname = "event_"+ str(inter_prob)+ "_"+ str(intra_prob) + "_" + str(alpha) + ".txt"

    cps_sizes = []
    cps_probs = []

    #sizes_1 = [100, 100, 100, 100, 100]
    sizes_1 = [83, 83, 83, 83, 84, 84]
    probs_1 = construct_SBM_block(sizes_1, inter_prob, intra_prob)

    if nc==2 or nc==4 or nc==10:
        sizes_2=[int(500/nc)]*nc
        print(sizes_2)
    elif nc==6:
        sizes_2 = [83, 83, 83, 83, 84, 84]
    elif nc==8:
        sizes_2 = [62, 62, 62, 62, 63, 63, 63, 63]

    probs_2 = construct_SBM_block(sizes_2, inter_prob, intra_prob)

    sizes = sizes_1
    probs = probs_1

    maxt = 100
    G_0=nx.stochastic_block_model(sizes, probs)
    G_0 = nx.Graph(G_0)
    G_t = G_0
    G_times = []
    G_times.append(G_t)

    for t in range(maxt):
        if (t in cps):
            G_t = SBM_snapshot(G_t, 1.0, sizes_2, probs_2)
            G_times.append(G_t)
            print ("generating " + str(t), end="\r")
        else:
            G_t = SBM_snapshot(G_t, alpha, sizes, probs)
            G_times.append(G_t)
            print ("generating " + str(t), end="\r")

    #write the entire history of snapshots
    to_edgelist(G_times, fname)

def main():

    args = sys.argv
    nc = int(args[1])
    alpha = float(args[2])
    anomarly=str(args[3])

    inter_prob = 0.002
    intra_prob = 0.25

    if anomarly=='event':
        generate_event(inter_prob, intra_prob, alpha, nc)
    else:
        generate_change(inter_prob, intra_prob, alpha, nc)

    #generate_pureSetting(inter_prob, intra_prob, alpha)
    #alpha = 0.1
    #generate_hybridSetting(inter_prob, intra_prob, alpha, increment)

    # inter_prob = 0.005
    # intra_prob = 0.03
    # increment = 0.10
    # alpha = 1.0
    # #generate_ChangePoint(inter_prob, intra_prob, alpha)
    # generate_event_change(inter_prob, intra_prob, alpha, increment)



if __name__ == "__main__":
    main()
