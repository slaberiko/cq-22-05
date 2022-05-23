#!/bin/zsh

dir_name=$1
data=1

lam_f_2_16_491_500_res=../${dir_name}/datasets/lambda/${data}/plot/lambda_k_2_16_491_500.res
lam_f_2_16_491_500_eps=../${dir_name}/datasets/lambda/${data}/plot/lambda_k_2_16_491_500.eps

lam_dir=../${dir_name}/datasets/lambda/${data}

cat <<EOF > $lam_f_2_16_491_500_res
xlabel: k
ylabel: Time average of {/Symbol l}_{t, k}
option: set style data points
option: set yrange [-5:50]
option: set xtics ('4' 4,'7' 7,'10' 10,'13' 13,'16' 16,'491' 19, '494' 22, '497' 25,'500' 28)
option: set key left top
EOF

echo "name: before anomaly" >> $lam_f_2_16_491_500_res
for i in `seq 2 16`;
do
    # t <= 50
    l=`head -n 51 ${lam_dir}/lambda_k_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${l}" >> $lam_f_2_16_491_500_res
done

for i in `seq 491 500`;
do
    # t <= 50
    l=`head -n 51 ${lam_dir}/lambda_k_$i.txt | awk '{print $2}'| stats -t avg`
    echo "$((i-472)) ${l}" >> $lam_f_2_16_491_500_res
done

echo "name: after anomaly" >> $lam_f_2_16_491_500_res
for i in `seq 2 16`;
do
    # t >= 51
    l=`tail -n 50 ${lam_dir}/lambda_k_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${l}" >> $lam_f_2_16_491_500_res
done

for i in `seq 491 500`;
do
    # t >= 51
    l=`tail -n 50 ${lam_dir}/lambda_k_$i.txt | awk '{print $2}'| stats -t avg`
    echo "$((i-472)) ${l}" >> $lam_f_2_16_491_500_res
done

xdoplot -te $lam_f_2_16_491_500_res | psfix-gnuplot > $lam_f_2_16_491_500_eps
epstopdf $lam_f_2_16_491_500_eps
