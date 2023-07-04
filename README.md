# YOLOv8

repo install

[https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)

![img](../../images/banner-yolov8.png)

![img](../../images/yolo_task.png)

1. Clone the ultralytics repository

```
git clone https://github.com/ultralytics/ultralytics
```

2. Navigate to the cloned directory

```
cd ultralytics
```

3. Install the package in editable mode for development

```
pip install -e .
```

4. test env

```
python test.py
```

5. train

```
python train.py
```

6. export onnx

```
python export.py
```

![](../../images/yolov5s_det_onnx.png)

7. transpose

v8 + transpose 更改输出维度顺序 与v5保持一致 方便通用框架trt推理

```
python v8trans.py
```

![](../../images/yolov5s_det_trans_onnx.png)


8. change name
更改 v8 输出节点name  与v5保持一致 方便通用框架trt推理

```
python onnx_cg_ioname.py  ./workspace/weights/yolov8s-det.transd.onnx 
```

![](../../images/io_cg.jpg)