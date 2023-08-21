# from ultralytics import YOLO

# # Load a model
# yaml_path = '/home/jess2/wd_speciesid/scripts/yolov8/config/trial_1.yaml'

# model = YOLO('yolov8n.yaml')  # build a new model from YAML
# model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml'.load('yolov8n.pt')  # build from YAML and transfer weights

# # Train the model
# results = model.train(data=yaml_path, epochs=30)

# # Evaluate the model's performance on the validation set
# results = model.val()

# # Export the model to ONNX format
# success = model.export(format='onnx')



# 1. Import necessary libraries
from ultralytics import YOLO # Here we import YOLO 
import yaml                  # for yaml files 
import torch
from PIL import Image
import os
import cv2
import time

# 2. Choose our yaml file
yaml_filename = 'config/trial_1_dataset.yaml' 

# 3. Create Yolo model
model = YOLO('yolov8n.yaml') # creates Yolo object from 'yolov8n.yaml' configuration file. 
model = YOLO('yolov8n.pt')   # Loads pretrained weights             
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# 4. Train the model
model.train(data='{}'.format(yaml_filename), epochs=30, patience=5, batch=8,  imgsz=640) 
