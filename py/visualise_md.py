# Render bounding boxes on our images
import subprocess

output_file_path = 'home/jess2/data/wild_deserts/processed/md_output.json'
visualisation_dir = 'home/jess2/data/wild_deserts/processed/md_output'
img_dir = 'home/jess2/data/wild_deserts/Beyond the Fence- Tagged'

for dir in img_dir:
    images_dir = dir
    command = [
            "python",
            "home/jess2/git/CameraTraps/visualization/visualize_detector_output.py",
            output_file_path,
            visualisation_dir,
            "--confidence",
            "0.2",
            "images_dir",
            images_dir
            ]
    subprocess.run(command, check=True)

#for dir in 'home/jess2/data/wild_deserts/Beyond the Fence- Tagged':
#	images_dir = dir
#	subprocess.check_output(command "$output_file_path" "$visualisation_dir" --confidence 0.2 --images_dir "$images_dir")

# Show the images with bounding boxes
import os
from PIL import Image

for vis_file_name in os.listdir(visualisation_dir):
      print(vis_file_name)
      im = Image.open(os.path.join(visualisation_dir, vis_file_name))
      display(im)
