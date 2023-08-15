# Render bounding boxes on our images
visualisation_dir = '~/data/wild_deserts/processed/md_output'
output_file_path = 
!python /~/git/CameraTraps/visualisation/visualise_detector_output.py "$output_file_path" "$visualisation_dir" --confidence 0.2 --images_dir "$images_dir"
