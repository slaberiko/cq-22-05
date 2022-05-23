#!/bin/zsh

dir_name=$1
data=1
time=100

dir_eig=../${dir_name}/datasets/eig/${data}/t0_l10

mkdir -p ../${dir_name}/datasets/lambda/
mkdir -p ../${dir_name}/datasets/lambda/${data}
mkdir -p ../${dir_name}/datasets/lambda/${data}/plot

dir_lambda=../${dir_name}/datasets/lambda/${data}
#dir_lambda_plot=../${dir_name}/datasets/lambda/${data}/plot

#under
for i in `seq 2 16`;
do
    eig_file=${dir_eig}/eig_0.txt
    eig=`sed -n $((i-1))p ${eig_file}`
    echo 0 ${eig} > ${dir_lambda}/lambda_k_${i}.txt

    for j in `seq 1 ${time}`;
    do
	eig_file=${dir_eig}/eig_${j}.txt
	eig=`sed -n $((i-1))p ${eig_file}`
	echo ${j} ${eig} >> ${dir_lambda}/lambda_k_${i}.txt
    done
done

#top
for i in `seq 491 500`;
do
    eig_file=${dir_eig}/eig_0.txt
    eig=`sed -n $((i-1))p ${eig_file}`
    echo 0 ${eig} > ${dir_lambda}/lambda_k_${i}.txt

    for j in `seq 1 ${time}`;
    do
	eig_file=${dir_eig}/eig_${j}.txt
	eig=`sed -n $((i-1))p ${eig_file}`
	echo ${j} ${eig} >> ${dir_lambda}/lambda_k_${i}.txt
    done
done
