#!/bin/zsh

alpha=$1 #0.1 or 1.0
data=$2
pex=0.01 #0.05, 0.075, 0.1, 0.125, and 0.15
anomarly=change #$3 #event or change

mkdir -p ../SB_${anomarly}_pex_${pex}_alpha_${alpha}
mkdir -p ../SB_${anomarly}_pex_${pex}_alpha_${alpha}/datasets
mkdir -p ../SB_${anomarly}_pex_${pex}_alpha_${alpha}/datasets/graph

datadir="../SB_${anomarly}_pex_${pex}_alpha_${alpha}/datasets/graph"

./SBM_pex_generator.py ${pex} ${alpha} ${anomarly}

mv ${anomarly}_0.002_0.25_${alpha}.txt ${anomarly}_0.002_0.25_${alpha}_${data}.txt
mv ${anomarly}_0.002_0.25_${alpha}_${data}.txt ${datadir}/
