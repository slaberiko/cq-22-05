#!/bin/zsh

dir_name=$1
num_eig=10
time=100
data=1
for top in 0 1 10;
do
    ./LAD_diff.sh $dir_name $data $num_eig $top $time
done
echo $data
