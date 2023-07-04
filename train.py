# @dong
# v8 train 230703

from ultralytics import YOLO

'''# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights
'''
# train det
model = YOLO("workspace/weights/yolov8s-det.pt")
# 
model.train(data='ultralytics/ultralytics/datasets/VOC.yaml', epochs=20, imgsz=640, batch=64)