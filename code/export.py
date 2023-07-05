# @dong
# v8 export onnx 230703

from ultralytics import YOLO

# export
model = YOLO('workspace/weights/yolov8s-det.pt')
# sucess = model.export(format='onnx', simplify=True, dynamic=False)
sucess = model.export(format='onnx', simplify=True, dynamic=True)