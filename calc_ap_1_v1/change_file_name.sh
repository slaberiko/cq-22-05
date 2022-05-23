#!/bin/zsh

#no=$1
data=$1
name=$2
dir_name=$3
#setting=alpha_0.3_

dir=../${dir_name}
dir_z_rank=$dir/zscore_rank
dir_sort=$dir/sort
dir_sigma=$dir/sigma

mv $dir/Zscore.txt $dir/zscore_$name.txt
mv $dir/ranking.txt $dir/ranking_$name.txt
mv $dir/score_sorted.txt $dir/score_sorted_$name.txt
mv $dir/z_d.txt $dir/z_d_$name.txt
mv $dir/sigma.txt $dir/sigma_$name.txt

# zscore_rank
mkdir -p $dir_z_rank
mkdir -p $dir_z_rank/$data
mkdir -p $dir_z_rank/$data/$name


# sort
mkdir -p $dir_sort
mkdir -p $dir_sort/$data
mkdir -p $dir_sort/$data/$name

#sigma
mkdir -p $dir_sigma
mkdir -p $dir_sigma/$data
mkdir -p $dir_sigma/$data/$name

mv $dir/zscore_$name.txt ${dir_z_rank}/$data/$name/
mv $dir/score_sorted_$name.txt ${dir_sort}/$data/$name/
mv $dir/ranking_$name.txt ${dir_z_rank}/$data/$name/
mv $dir/z_d_$name.txt ${dir_z_rank}/$data/$name/
mv $dir/sigma_$name.txt $dir_sigma/$data/$name
