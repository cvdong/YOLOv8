# @dong
# get pre txt 20230707

import os
import cv2
from tqdm import tqdm
from infer import yolo_infer

map_out_path    = '../map_out'
VOCdevkit_path = "../../datasets/VOC/VOCdevkit"

if not os.path.exists(os.path.join(map_out_path, 'detection-results')):
    os.makedirs(os.path.join(map_out_path, 'detection-results'))
if not os.path.exists(os.path.join(map_out_path, 'images-optional')):
        os.makedirs(os.path.join(map_out_path, 'images-optional'))

image_ids = open(os.path.join(VOCdevkit_path, 
                              "VOC2007/ImageSets/Main/test.txt")).read().strip().split()
classes_path    = 'voc_classes.txt'
# 可视化
map_vis = False

def get_classes(classes_path):
    with open(classes_path, encoding='utf-8') as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names, len(class_names)

class_names, _ = get_classes(classes_path)

# infer
infer = yolo_infer()
init = infer.init_model_v8()

for image_id in tqdm(image_ids):
    
    f = open(os.path.join(map_out_path, 
                          "detection-results/" + image_id + ".txt"), "w", encoding='utf-8')
    image_path  = os.path.join(VOCdevkit_path, "VOC2007/JPEGImages/" + image_id + ".jpg") 
    image = cv2.imread(image_path)
    if map_vis:
        cv2.imwrite(os.path.join(map_out_path, "images-optional/" + image_id + ".jpg"), image)
    det_boxes = infer.infer(init, image)
    for box in det_boxes:
        score = box.confidence
        left, top, right, bottom = map(int, [box.left, box.top, box.right, box.bottom])

        f.write("%s %s %s %s %s %s\n" % (class_names[int(box.class_label)], score, str(left), str(top), str(right),str(bottom)))
