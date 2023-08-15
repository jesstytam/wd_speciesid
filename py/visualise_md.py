# Render bounding boxes on our images
visualisation_dir = 'home/jess2/data/wild_deserts/Beyond the Fence- Tagged/PCAM01'
#!python ~/git/CameraTraps/visualization/visualize_detector_output.py "$output_file_path" "$visualisation_dir" --confidence 0.2 --images_dir "$images_dir"

# Show the images with bounding boxes
import os
from PIL import Image

for vis_file_name in os.listdir(visualisation_dir):
      print(vis_file_name)
      im = Image.open(os.path.join(visualisation_dir, vis_file_name))
      display(im)
