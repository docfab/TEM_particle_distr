#!/bin/bash

path_to_image=$(pwd)

for i in *tiff
do 

	echo $i

	sed "s|image_path|${path_to_image}/${i}|g" particles_analysis.ijm > ~/.imagej/macros/particles_analysis.ijm

	sed -i "s|output_path|${path_to_image}/Results$i.csv|g" ~/.imagej/macros/particles_analysis.ijm 

	imagej -m particles_analysis.ijm 
	
done

rm ~/.imagej/macros/particles_analysis.ijm

sed -i '1d' *csv

cat *csv > combined.csv

python3 ./distr.py
