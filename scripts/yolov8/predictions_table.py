import json
import cv2

yolo = json.load(open('/home/jess2/wd_speciesid/scripts/yolov8/runs/detect/val2/predictions.json'))
coco = json.load(open('/home/jess2/wd_speciesid/data/processed/val_coco.json'))

def get_iou(json, coco):
            
    # Define two bounding boxes as (x, y, width, height)
    box1 = coco['annotations']['bbox'] #ground truth
    box2 = json['bbox'] #prediction

    # Convert bounding box coordinates to the format (x1, y1, x2, y2)
    box1 = [box1[0], box1[1], box1[0] + box1[2], box1[1] + box1[3]]
    box2 = [box2[0], box2[1], box2[0] + box2[2], box2[1] + box2[3]]

    # Calculate the coordinates of the intersection rectangle
    x_intersection = max(box1[0], box2[0])
    y_intersection = max(box1[1], box2[1])
    w_intersection = min(box1[2], box2[2]) - x_intersection
    h_intersection = min(box1[3], box2[3]) - y_intersection

    # Calculate the area of intersection
    area_intersection = max(0, w_intersection) * max(0, h_intersection)

    # Calculate the area of the union
    area_box1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area_box2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    area_union = area_box1 + area_box2 - area_intersection

    # Calculate IoU
    iou = area_intersection / area_union
    return iou

updated_predictions = '/home/jess2/wd_speciesid/scripts/yolov8/runs/detect/val2/updated_predictions.json'

# Iterate through predictions and add IOU and category correctness information
for prediction in yolo:
    for coco_annotation in coco['annotations']:
        # print(prediction)
        # print(coco_annotation)
        coco_id = coco_annotation['file_name'].split('/')[1].split('.')[0]
        if prediction['image_id'] == coco_annotation['image_id']:
            iou = get_iou(prediction['bbox'], coco_annotation['bbox'])
            category_correct = prediction['category_id'] == coco_annotation['category_id']

            # Add IOU and category correctness to the prediction dictionary
            iou = prediction['iou']
            category_correct = prediction['category_correct']

            # write file
            with open(updated_predictions, 'w') as file:
                json.dump(yolo, file, indent=4)