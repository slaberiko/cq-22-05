#!/bin/zsh

dir_name=${1:-SB_change_pex_0.01_alpha_1.0}
data=1

dir_eig=t10_l0

sigma_dir="../${dir_name}/sigma/${data}/${dir_eig}/sigma_n"

sigma_dir_name_1_10_res="${sigma_dir}/${dir_name}_sigma_${dir_eig}_1_10.res"
sigma_dir_name_1_10_eps="${sigma_dir}/${dir_name}_sigma_${dir_eig}_1_10.eps"

cat <<EOF > $sigma_dir_name_1_10_res
xlabel: k
ylabel: ~{{/Symbol s} (k)}{.9/Symbol \276}
option: set style data linespoints
option: set yrange [0.25:0.4]
EOF

echo "name: before anomaly" >> $sigma_dir_name_1_10_res
for i in  `seq 1 10`;
do
    # t <= 50
    s=`head -n 51 ${sigma_dir}/sigma_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${s}" >> $sigma_dir_name_1_10_res
done

echo "name: after anomaly" >> $sigma_dir_name_1_10_res
for i in `seq 1 10`;
do
    # t >= 51
    s=`tail -n 50 ${sigma_dir}/sigma_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${s}" >> $sigma_dir_name_1_10_res
done

xdoplot -te $sigma_dir_name_1_10_res | psfix-gnuplot > $sigma_dir_name_1_10_eps
epstopdf $sigma_dir_name_1_10_eps

#t0_l10
dir_eig=t0_l10
sigma_dir="../${dir_name}/sigma/${data}/${dir_eig}/sigma_n"

sigma_dir_name_1_10_res="${sigma_dir}/${dir_name}_sigma_${dir_eig}_1_10.res"
sigma_dir_name_1_10_eps="${sigma_dir}/${dir_name}_sigma_${dir_eig}_1_10.eps"

cat <<EOF > $sigma_dir_name_1_10_res
xlabel: k
ylabel: ~{{/Symbol s} (k)}{.9/Symbol \276}
option: set style data linespoints
option: set yrange [-0.01:0.55]
EOF
echo "name: before anomaly" >> $sigma_dir_name_1_10_res
for i in  `seq 1 10`;
do
    # t <= 50
    s=`head -n 51 ${sigma_dir}/sigma_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${s}" >> $sigma_dir_name_1_10_res
done

echo "name: after anomaly" >> $sigma_dir_name_1_10_res
for i in `seq 1 10`;
do
    # t >= 51
    s=`tail -n 50 ${sigma_dir}/sigma_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${s}" >> $sigma_dir_name_1_10_res
done

xdoplot -te $sigma_dir_name_1_10_res | psfix-gnuplot > $sigma_dir_name_1_10_eps
epstopdf $sigma_dir_name_1_10_eps

#t1_l9
dir_eig=t1_l9
sigma_dir="../${dir_name}/sigma/${data}/${dir_eig}/sigma_n"

sigma_dir_name_1_10_res="${sigma_dir}/${dir_name}_sigma_${dir_eig}_1_10.res"
sigma_dir_name_1_10_eps="${sigma_dir}/${dir_name}_sigma_${dir_eig}_1_10.eps"
cat <<EOF > $sigma_dir_name_1_10_res
xlabel: k
ylabel: ~{{/Symbol s} (k)}{.9/Symbol \276}
option: set style data linespoints
option: set yrange [-0.01:0.95]
EOF
echo "name: before anomaly" >> $sigma_dir_name_1_10_res
for i in  `seq 1 10`;
do
    # t <= 50
    s=`head -n 51 ${sigma_dir}/sigma_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${s}" >> $sigma_dir_name_1_10_res
done

echo "name: after anomaly" >> $sigma_dir_name_1_10_res
for i in `seq 1 10`;
do
    # t >= 51
    s=`tail -n 50 ${sigma_dir}/sigma_$i.txt | awk '{print $2}'| stats -t avg`
    echo "${i} ${s}" >> $sigma_dir_name_1_10_res
done

xdoplot -te $sigma_dir_name_1_10_res | psfix-gnuplot > $sigma_dir_name_1_10_eps
epstopdf $sigma_dir_name_1_10_eps
