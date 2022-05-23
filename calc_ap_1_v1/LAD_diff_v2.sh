#!/bin/zsh

s=5
l=10

dir_name=$1
data=$2
num_eig=$3
top=$4
time=$5

mkdir -p ../${dir_name}/eig

for i in `seq 0 ${time}`;
do
    u=$((num_eig-top))
    if [ ${i} -lt 51 ]; then
	if [ $u = 0 ]; then
	    tail -n $top ../${dir_name}/datasets/eig/$data/t0_l10/eig_$i.txt > ../${dir_name}/eig/eig_$i.txt
	elif [ $top = 0 ]; then
	    head -n $u ../${dir_name}/datasets/eig/$data/t0_l10/eig_$i.txt > ../${dir_name}/eig/eig_$i.txt
	else
	    head -n $u ../${dir_name}/datasets/eig/$data/t0_l10/eig_$i.txt > ../${dir_name}/eig/eig_$i.txt
	    tail -n $top ../${dir_name}/datasets/eig/$data/t0_l10/eig_$i.txt >> ../${dir_name}/eig/eig_$i.txt
	fi
    else
	if [ $u = 0 ]; then
	    #echo 1
	    tail -n $top ../${dir_name}/datasets/eig/$data/t0_l10/eig_$i.txt > ../${dir_name}/eig/eig_$i.txt
	elif [ $top = 0 ]; then
	    tail -n 494 ../${dir_name}/datasets/eig/$data/t0_l10/eig_$i.txt | head -n ${u} > ../${dir_name}/eig/eig_$i.txt
	else
	    tail -n 494 ../${dir_name}/datasets/eig/$data/t0_l10/eig_$i.txt | head -n ${u}> ../${dir_name}/eig/eig_$i.txt
	    tail -n $top ../${dir_name}/datasets/eig/$data/t0_l10/eig_$i.txt >> ../${dir_name}/eig/eig_$i.txt
	fi
    fi
done


./LAD.sh $time $num_eig $s $l $dir_name

rm ../${dir_name}/eig/*.txt

./diff.py $dir_name > ../${dir_name}/z_d.txt
./sort_diff.py $top ${dir_name}

./change_file_name.sh $data "t${top}_l$((num_eig-top))" ${dir_name}
