#!/bin/zsh

tmax=${1:-100}
k=${2:-10}
s=${3:-5}
l=${4:-10}
dir_name=$5

#echo "$i"
./calc_LAD.py $tmax $k $s $l $dir_name > ../${dir_name}/Zscore.txt
