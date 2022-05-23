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

def SBM_snapshot_anomaly(G_prev, alpha, sizes, probs):
    G_t = G_prev.copy()
    nodelist = list(range(0,sum(sizes)))
    #print(nodelist)
    G_new = nx.stochastic_block_model(sizes, probs, nodelist=nodelist)
    n = len(G_t)
    #print(probs)
    #print(G_new.edges)
    if alpha==1.0:
        for i in range(0, 83):
            for j in range(83, 500):
                if G_new.has_edge(i, j):
                    G_new.remove_edge(i, j)
                elif G_new.has_edge(j, i):
                    G_new.remove_edge(j, i)
        for i in range(83, 166):
            for j in range(166, 500):
                if G_new.has_edge(i, j):
                    G_new.remove_edge(i, j)
                elif G_new.has_edge(j, i):
                    G_new.remove_edge(j, i)
        for i in range(166, 249):
            for j in range(249, 500):
                if G_new.has_edge(i, j):
                    G_new.remove_edge(i, j)
                elif G_new.has_edge(j, i):
                    G_new.remove_edge(j, i)
        for i in range(249, 332):
            for j in range(332, 500):
                if G_new.has_edge(i, j):
                    G_new.remove_edge(i, j)
                elif G_new.has_edge(j, i):
                    G_new.remove_edge(j, i)
        for i in range(332, 416):
            for j in range(416, 500):
                if G_new.has_edge(i, j):
                    G_new.remove_edge(i, j)
                elif G_new.has_edge(j, i):
                    G_new.remove_edge(j, i)
        G_t=G_new
    elif alpha==0:
        for i in range(0, 83):
            for j in range(83, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)
        for i in range(83, 166):
            for j in range(166, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)
        for i in range(166, 249):
            for j in range(249, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)
        for i in range(249, 332):
            for j in range(332, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)
        for i in range(332, 416):
            for j in range(416, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)
    else:
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
        for i in range(0, 83):
            for j in range(83, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)
        for i in range(83, 166):
            for j in range(166, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)
        for i in range(166, 249):
            for j in range(249, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)
        for i in range(249, 332):
            for j in range(332, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)
        for i in range(332, 416):
            for j in range(416, 500):
                if G_t.has_edge(i, j):
                    G_t.remove_edge(i, j)
                elif G_t.has_edge(j, i):
                    G_t.remove_edge(j, i)

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
def generate_change(p_ex, intra_prob, alpha):
    cps=[50]
    fname = "SB_"+ str(intra_prob) + "_" + str(alpha) + ".txt"

    cps_sizes = []
    cps_probs = []

    #let there be 500 nodes
    #sizes_1 = [100,100,100,100,100] #500 nodes total at all times
    sizes_1 = [83, 83, 83, 83, 84, 84]
    probs_1 = construct_SBM_block(sizes_1, p_ex, intra_prob)

    # sizes_2 = [100,100,100,100,100]

    sizes = sizes_1
    probs = probs_1
    maxt = 100
    G_0=nx.stochastic_block_model(sizes, probs)
    G_0 = nx.Graph(G_0)
    G_t = G_0
    G_times = []
    G_times.append(G_t)

    #anomaly point alpha=0
    alpha_a=0

    for t in range(maxt):
        if t < cps[0]:
            G_t = SBM_snapshot(G_t, alpha, sizes, probs)
            G_times.append(G_t)
            print ("generating " + str(t), end="\r")
        elif (t in cps):
            G_t = SBM_snapshot_anomaly(G_t, alpha_a, sizes, probs)
            G_times.append(G_t)
            print ("generating " + str(t), end="\r")

        else:
            G_t = SBM_snapshot_anomaly(G_t, alpha, sizes, probs)
            G_times.append(G_t)
            print ("generating " + str(t), end="\r")

    #write the entire history of snapshots
    to_edgelist(G_times, fname)

def main():

    args = sys.argv
    p_ex = float(args[1])
    alpha = float(args[2])

    intra_prob = 0.25

    generate_change(p_ex, intra_prob, alpha)

    #generate_pureSetting(p_ex, intra_prob, alpha)
    #alpha = 0.1
    #generate_hybridSetting(p_ex, intra_prob, alpha, increment)

    # p_ex = 0.005
    # intra_prob = 0.03
    # increment = 0.10
    # alpha = 1.0
    # #generate_ChangePoint(p_ex, intra_prob, alpha)
    # generate_event_change(p_ex, intra_prob, alpha, increment)

if __name__ == "__main__":
    main()
