#!/bin/zsh

dir_name=$1
data=1

lam_f_2_11_491_500_res=../${dir_name}/datasets/lambda/${data}/plot/lambda_k_2_11_491_500.res
lam_f_2_11_491_500_eps=../${dir_name}/datasets/lambda/${data}/plot/lambda_k_2_11_491_500.eps

lam_dir=../${dir_name}/datasets/lambda/${data}


#以下，研究会用
cat <<EOF > $lam_f_2_11_491_500_res
xlabel: k
ylabel: Time average of {/Symbol l}_{t, k}
option: set style data points
option: set yrange [-5:50]
option: set xtics ('3' 3,'5' 5,'7' 7,'9' 9,'11' 11, '491' 13, '493' 15, '495' 17, '497' 19, '499' 21)
option: set key left top
EOF

echo "name: before anomaly" >> $lam_f_2_11_491_500_res
for i in `seq 2 11`;
do
    # t <= 50
    l=`head -n 51 ${lam_dir}/lambda_k_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${l}" >> $lam_f_2_11_491_500_res
done

for i in `seq 491 500`;
do
    # t <= 50
    l=`head -n 51 ${lam_dir}/lambda_k_$i.txt | awk '{print $2}'| stats -t avg`
    echo "$((i-478)) ${l}" >> $lam_f_2_11_491_500_res
done

echo "name: after anomaly" >> $lam_f_2_11_491_500_res
for i in `seq 2 11`;
do
    # t >= 51
    l=`tail -n 50 ${lam_dir}/lambda_k_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${l}" >> $lam_f_2_11_491_500_res
done

for i in `seq 491 500`;
do
    # t >= 51
    l=`tail -n 50 ${lam_dir}/lambda_k_$i.txt | awk '{print $2}'| stats -t avg`
    echo "$((i-478)) ${l}" >> $lam_f_2_11_491_500_res
done

xdoplot -te $lam_f_2_11_491_500_res | psfix-gnuplot > $lam_f_2_11_491_500_eps
epstopdf $lam_f_2_11_491_500_eps
