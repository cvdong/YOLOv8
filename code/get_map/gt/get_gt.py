# @dong
# get gt txt 20230707

import os
from  tqdm import tqdm
import xml.etree.ElementTree as ET

map_out_path    = '../map_out'
VOCdevkit_path = "../../datasets/VOC/VOCdevkit"
classes_path    = 'voc_classes.txt'

def get_classes(classes_path):
    with open(classes_path, encoding='utf-8') as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names, len(class_names)

class_names, _ = get_classes(classes_path)

image_ids = open(os.path.join(VOCdevkit_path, 
                              "VOC2007/ImageSets/Main/test.txt")).read().strip().split()
if not os.path.exists(map_out_path):
    os.makedirs(map_out_path)
if not os.path.exists(os.path.join(map_out_path, 'ground-truth')):
    os.makedirs(os.path.join(map_out_path, 'ground-truth'))
    
for image_id in tqdm(image_ids):
    with open(os.path.join(map_out_path, "ground-truth/" + image_id+".txt"), "w") as f:
        root = ET.parse(os.path.join(VOCdevkit_path, "VOC2007/Annotations/"+image_id+".xml")).getroot()
        for obj in root.findall('object'):
            difficult_flag = False
            if obj.find('difficult')!=None:
                difficult = obj.find('difficult').text
                if int(difficult)==1:
                    difficult_flag = True
            obj_name = obj.find('name').text
            if obj_name not in class_names:
                continue
            bndbox  = obj.find('bndbox')
            left    = bndbox.find('xmin').text
            top     = bndbox.find('ymin').text
            right   = bndbox.find('xmax').text
            bottom  = bndbox.find('ymax').text

            if difficult_flag:
                f.write("%s %s %s %s %s difficult\n" % (obj_name, left, top, right, bottom))
            else:
                f.write("%s %s %s %s %s\n" % (obj_name, left, top, right, bottom))
                
print("Get ground truth result done.")