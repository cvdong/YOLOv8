## 测试模型精度

1. 获取gt
```
python get_gt.py 
```

2. 获取pre
```
python get_pre.py 
```

笔者用的自己封装的yolo infer接口，此动态库极大可能不适用你的硬件配置。

3. 得到map

```
python get_map.py 
```

具体看代码::

![](./map_out/results/map.png)

补充：

模型map也可用官方v8 repo val接口进行测试，无论pt、onnx和engine, 但是笔者发现int8 engine貌似有些bug :sweat_smile: