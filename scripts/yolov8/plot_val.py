# import json
# import os
# from PIL import Image
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

# # Load the YOLO results from the JSON file
# json_file = '/home/jess2/wd_speciesid/scripts/yolov8/runs/detect/val2/predictions.json'
# with open(json_file, 'r') as file:
#     yolo_results = json.load(file)

# # Load the image file paths from the TXT file
# txt_file = '/home/jess2/wd_speciesid/data/processed/yolo/validation/validation_jpg.txt'
# with open(txt_file, 'r') as file:
#     image_paths = file.read().splitlines()

# # Create a directory to save the images with bounding boxes
# output_dir = '/home/jess2/data/wild_deserts/processed/yolo_val_outputs'
# os.makedirs(output_dir, exist_ok=True)

# # Create a dictionary to map image IDs to their corresponding file paths
# image_id_to_path = {}
# for image_path in image_paths:
#     image_id = os.path.basename(image_path).replace('.JPG', '')
#     image_id_to_path[image_id] = image_path

# # Loop through YOLO results and plot bounding boxes on images
# for result in yolo_results:
#     image_id = result['image_id']
#     category_id = result['category_id']
#     bbox = result['bbox']

#     # Get the image path based on the image ID
#     image_path = image_id_to_path.get(image_id)
#     image_path_updated = image_path.replace('./', '/home/jess2/data/wild_deserts/Beyond the Fence- Tagged/')

#     if image_path_updated:
#         # Load the image
#         image = Image.open(image_path_updated)
#         image = image.convert("RGB")
        
#         # Create a figure and axis
#         fig, ax = plt.subplots(1)

#         # Display the image
#         ax.imshow(image)

#         # Create a rectangle patch for the bounding box
#         x, y, width, height = bbox
#         rect = patches.Rectangle(
#             (x, y), width, height, linewidth=1, edgecolor='r', facecolor='none'
#         )

#         # Add the rectangle patch to the axis
#         ax.add_patch(rect)

#         # Set title and axis limits
#         plt.title(f'Category ID: {category_id}')
#         plt.xlim(0, image.width)
#         plt.ylim(image.height, 0)

#         # Save the image with bounding box to the output directory
#         output_image_path = os.path.join(output_dir, f'{image_id}_bbox.jpg')
#         plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0)
#         plt.close()  # Close the plot

# print(f"Bounding boxes images saved in {output_dir}")


# coco_annotation_file = '/home/jess2/ct_classifier_wd/data/processed/' + dataset + '_coco.json'
# coco = json.load(open(coco_annotation_file))

# for annotation in coco['annotations']:

#     x = annotation['bbox'][0]
#     y = annotation['bbox'][1]
#     w = annotation['bbox'][2]
#     h = annotation['bbox'][3]

#     box = (x, y, x+w, y+h)

#     image_path = annotation['image_id'].replace('_', ' ', 4) + '.JPG'
#     image_path_updated = image_path.replace(' ', '/', 1)
#     image_path_full = '/home/jess2/data/wild_deserts/Beyond the Fence- Tagged/images/' + image_path_updated
#     outpath = '/home/jess2/data/wild_deserts/processed/crops/' + dataset + '/'

#     img = Image.open(image_path_full)
#     img2 = img.crop(box)
#     img2_path = outpath + annotation['image_id'] + '.JPG'
#     img2.save(img2_path, 'JPEG')

# print('Cropping done for ' + dataset + ' images.')



# import sys
# from PIL import Image, ImageDraw

# with Image.open("hopper.jpg") as im:

#     draw = ImageDraw.Draw(im)
#     draw.line((0, 0) + im.size, fill=128)
#     draw.line((0, im.size[1], im.size[0], 0), fill=128)

#     # write to stdout
#     im.save(sys.stdout, "PNG")


# Predict bounding boxes on validation set using trained YOLO model

from ultralytics import YOLO

# Load my pretrained YOLOv8n model
model = YOLO('/home/jess2/wd_speciesid/scripts/yolov8/runs/detect/train31/weights/best.pt')

# Read in image paths for validation images
with open('/home/jess2/wd_speciesid/data/processed/yolo/validation/validation_jpg.txt', 'r') as f:
  image_paths = f.read().splitlines()

# Iterate through images in val set and run inference
for image in image_paths:
  full_path = '/home/jess2/data/wild_deserts/processed/crops/val/predict/' + image
  model.predict(full_path, save=True, save_conf = True, imgsz=320, 
         conf=0.1, iou = 0.5) #keep default iou but set conf low bc I want to see bad ones too