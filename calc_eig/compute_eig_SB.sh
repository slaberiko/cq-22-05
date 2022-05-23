#!/bin/zsh

#current directry is version2/calc_eig/

d_name=$1 #e.g., SB_change_nc_10_alpha_1.0
f_name=$2 #e.g., change_0.002_0.25_1.0(../SB_change_nc_10_alpha_1.0/datasets/graph内)
data=$3 #e.g., data No (change_0.002_0.25_1.0_{data No}になっている)

dir="../${d_name}/datasets"
file="${f_name}_${data}.txt"

mkdir -p ${dir}/eig
mkdir -p ${dir}/eig/$data
mkdir -p ${dir}/eig/$data/t0_l10

./compute_SVD_SB.py ${dir} ${file} ${data}

echo "${data}"
