#single-class detector

# 1. Import necessary libraries
from ultralytics import YOLO # Here we import YOLO 
import yaml                  # for yaml files 
from PIL import Image
import wandb

# 2. Choose our yaml file
yaml_filename = 'config/trial_1.yaml' 

# 3. Create Yolo model
model = YOLO('yolov8s.yaml') # creates Yolo object from 'yolov8n.yaml' configuration file. 
model = YOLO('yolov8s.pt')   # Loads pretrained weights             
model = YOLO('yolov8s.yaml').load('yolov8s.pt')  # build from YAML and transfer weights

# 4. Train the model
model.train(data='{}'.format(yaml_filename), epochs=100, patience=5, batch=16,  imgsz=640) 

# 5. wandb
config = {
    "project": "yolov8s-multi-class",
    "num_of_classes": 15
}
run = wandb.init(project = config["project"], config = config)
