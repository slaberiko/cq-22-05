#!/bin/zsh
#sigmaの処理：実行すると固有値ごとの時系列に分けてくれる
dir_name=$1
max_data=1
dir_eig=t0_l10


for data in `seq 1 ${max_data}`;
do
    mkdir -p ../$dir_name/sigma
    mkdir -p ../$dir_name/sigma/$data
    mkdir -p ../$dir_name/sigma/$data/$dir_eig
    mkdir -p ../$dir_name/sigma/$data/$dir_eig/sigma_n

    mkdir -p ../$dir_name/sigma/$data/$dir_eig/diff_sigma_n

    mkdir -p ../$dir_name/sigma/$data/$dir_eig/diff_abs_sigma_n

    mkdir -p ../$dir_name/sigma/$data/$dir_eig/sort_diff_sigma_n

    ./sigma.py $dir_name $data $dir_eig
done

dir_eig=t10_l0

for data in `seq 1 ${max_data}`;
do
    mkdir -p ../$dir_name/sigma
    mkdir -p ../$dir_name/sigma/$data
    mkdir -p ../$dir_name/sigma/$data/$dir_eig
    mkdir -p ../$dir_name/sigma/$data/$dir_eig/sigma_n

    mkdir -p ../$dir_name/sigma/$data/$dir_eig/diff_sigma_n

    mkdir -p ../$dir_name/sigma/$data/$dir_eig/diff_abs_sigma_n

    mkdir -p ../$dir_name/sigma/$data/$dir_eig/sort_diff_sigma_n

    ./sigma.py $dir_name $data $dir_eig
done

dir_eig=t1_l9

for data in `seq 1 ${max_data}`;
do
    mkdir -p ../$dir_name/sigma
    mkdir -p ../$dir_name/sigma/$data
    mkdir -p ../$dir_name/sigma/$data/$dir_eig
    mkdir -p ../$dir_name/sigma/$data/$dir_eig/sigma_n

    mkdir -p ../$dir_name/sigma/$data/$dir_eig/diff_sigma_n

    mkdir -p ../$dir_name/sigma/$data/$dir_eig/diff_abs_sigma_n

    mkdir -p ../$dir_name/sigma/$data/$dir_eig/sort_diff_sigma_n

    ./sigma.py $dir_name $data $dir_eig
done
