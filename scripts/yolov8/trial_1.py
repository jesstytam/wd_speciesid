from ultralytics import YOLO

# Load a model
yaml_path = '/home/jess2/wd_speciesid/scripts/yolov8/config/trial_1.yaml'

model = YOLO('yolov8n.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n.yaml'.load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data=yaml_path, epochs=30)

# Evaluate the model's performance on the validation set
results = model.val()

# Export the model to ONNX format
success = model.export(format='onnx')
