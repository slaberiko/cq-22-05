#!/bin/zsh

alpha=$1 #0.1 or 1.0
pex=0.002 #0.02, 0.04, 0.06, 0.08, and 0.1
data=1

mkdir -p ../SB_exp3_pex_${pex}_alpha_${alpha}
mkdir -p ../SB_exp3_pex_${pex}_alpha_${alpha}/datasets
mkdir -p ../SB_exp3_pex_${pex}_alpha_${alpha}/datasets/graph

datadir="../SB_exp3_pex_${pex}_alpha_${alpha}/datasets/graph"

./SBM_exp3_pex_generator.py ${pex} ${alpha}

mv SB_0.25_${alpha}.txt SB_0.25_${alpha}_${data}.txt
mv SB_0.25_${alpha}_${data}.txt ${datadir}/
