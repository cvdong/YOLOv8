# @Dong
# 更改 v8 节点name 230704

import onnx
import sys
import os

def main():

    if len(sys.argv) < 2:
        print("Usage:\n python xx.py yolov8s-det.onnx")
        return 1

    file = sys.argv[1]
    if not os.path.exists(file):
        print(f"Not exist path: {file}")
        return 1
    
    node_name =  "output0"
    new_name  =  "outputs"
    
    prefix, suffix = os.path.splitext(file)
    dst = prefix + ".cg" + suffix
    
    model = onnx.load(file)
    
    for i, model_input_name in enumerate(model.graph.input):
        if model_input_name.name == node_name:
            model.graph.input[i].name = new_name
            
    for i, model_output_name in enumerate(model.graph.output):
        if model_output_name.name == node_name:
            model.graph.output[i].name = new_name
            
    for node in model.graph.node:
        if node_name in node.input:
            i = list(node.input).index(node_name)
            node.input[i] = new_name
            
        if node_name in node.output:
            i = list(node.output).index(node_name)
            node.output[i] = new_name
            
    print(f"Model save to {dst}")
    onnx.checker.check_model(model)
    onnx.save(model, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())