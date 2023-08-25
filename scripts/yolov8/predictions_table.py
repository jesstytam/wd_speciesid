import json
import cv2

load_yolo = json.load(open('/home/jess2/wd_speciesid/scripts/yolov8/runs/detect/val2/predictions.json'))
yolo=[]
for prediction in load_yolo:
    if prediction['score']>0.05:
        good_prediction = prediction
        yolo.append(good_prediction)

coco = json.load(open('/home/jess2/wd_speciesid/data/processed/val_coco.json'))
new_yolo = '/home/jess2/wd_speciesid/scripts/yolov8/runs/detect/val2/updated_predictions.json'

def get_iou(yolo_bbox, coco_bbox):
            
    # Define two bounding boxes as (x, y, width, height)
    box1 = coco_bbox #ground truth
    box2 = yolo_bbox #prediction

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

gt_index = {}
for coco_annotation in coco['annotations']:
    coco_id = coco_annotation['image_id'][7:]
    coco_id = coco_id.replace('_', ' ', 3)
    gt_index[coco_id] = coco_annotation

# Iterate through predictions and add IOU and category correctness information
for prediction in yolo:
    coco_id = prediction['image_id']
    if coco_id in gt_index:
            coco_annotation = gt_index[coco_id]
            bbox_gt = coco_annotation['bbox']
            iou = get_iou(prediction['bbox'], bbox_gt)
            category_gt = coco_annotation['category_id']
            category_match = prediction['category_id'] == category_gt
            # Add IOU and category correctness to the prediction dictionary
            prediction['bbox_gt'] = bbox_gt
            prediction['iou'] = iou
            prediction['category_gt'] = category_gt
            prediction['category_match'] = category_match
            # write file
            with open(new_yolo, 'w') as file:
                json.dump(yolo, file, indent=4)
                print(yolo)
    else:
        pass

            