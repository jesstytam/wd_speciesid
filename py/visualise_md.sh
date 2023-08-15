# Render bounding boxes on our images
output_file_path = '~/data/wild_deserts/processed/md_output.json'
visualisation_dir = '~/data/wild_deserts/processed/md_output'

for dir in '~/data/wild_deserts/Beyond the Fence- Tagged'
do
	images_dir = dir
	!python /~/git/CameraTraps/visualisation/visualise_detector_output.py "$output_file_path" "$visualisation_dir" --confidence 0.2 --images_dir "$images_dir"
done
