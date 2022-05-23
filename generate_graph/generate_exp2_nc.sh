#!/bin/zsh


alpha=$1 #0.1 or 1.0
data=$2
nc=10 #2, 4, 6, 8, and 10
anomarly=change #$3 #event or change

mkdir -p ../SB_${anomarly}_nc_${nc}_alpha_${alpha}
mkdir -p ../SB_${anomarly}_nc_${nc}_alpha_${alpha}/datasets
mkdir -p ../SB_${anomarly}_nc_${nc}_alpha_${alpha}/datasets/graph

datadir=../SB_${anomarly}_nc_${nc}_alpha_${alpha}/datasets/graph

./SBM_nc_generator.py ${nc} ${alpha} ${anomarly}

mv ${anomarly}_0.002_0.25_${alpha}.txt ${anomarly}_0.002_0.25_${alpha}_${data}.txt
mv ${anomarly}_0.002_0.25_${alpha}_${data}.txt ${datadir}/
