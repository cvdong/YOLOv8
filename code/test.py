# @dong
# v8 test 230703

# v8 适配、分类、检测、分割、姿态和跟踪五种视觉任务

import cv2
from ultralytics import YOLO

# cls
# model = YOLO('workspace/weights/yolov8s-cls.pt')

# det
model = YOLO('workspace/weights/yolov8s-det.pt')

# seg
# model = YOLO('workspace/weights/yolov8s-seg.pt')

# pose
# model = YOLO('workspace/weights/yolov8s-pose.pt')


# infer
result = model.predict("workspace/test", save=False)
# track
# result = model.track("workspace/test_video/vtest.avi", save=False)

for i in range(len(result)):
    annotated_image = result[i].plot()

    cv2.imwrite("../workspace/result/result_det{}.jpg".format(i), annotated_image)
    
print(f'oooooooooooooooooooooooooooo')