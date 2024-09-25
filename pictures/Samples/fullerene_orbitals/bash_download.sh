#!/bin/bash
PP=-11
for NN in {169..184}
do
        wget "http://physikmdb.uni-graz.at/cubefiles/000213/C60_MO_$NN" -O "/home/kononov/Documents/PhD-Presentaion/revealJS/pictures/Samples/fullerene_orbitals/c60_homo$PP.cub"
        PP=$((PP+1))
done

# echo $PP
# for NN in {169..184}
# do
#     echo $NN
#     echo $PP
#     PP=$((PP+1))
# done
