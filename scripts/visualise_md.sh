#!/bin/bash

output_file_path = 'home/jess2/data/wild_deserts/processed/md_output.json'
visualisation_dir = 'home/jess2/data/wild_deserts/processed/md_output'
img_dir = 'home/jess2/data/wild_deserts/Beyond the Fence- Tagged'

for dir in 'home/jess2/data/wild_deserts/Beyond the Fence- Tagged/';
do
	images_dir = "$dir"
	python home/jess2/git/CameraTraps/visualization/visualize_detector_output.py "$output_file_path" "$visualisation_dir" --confidence 0.2 --images_dir "$images_dir"
done
