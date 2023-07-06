'''
version: v1.0
Author:  Dong
Time:    2023.7
'''

import yolo
import cv2

# infer
class yolo_infer():
    
    def __init__(self):
        pass
        
    @staticmethod
    def init_model_v8():
        init = yolo.Yolo("best_fp16.engine", yolo.YoloType.V8, 0, 0.001, 0.7)
        
        if not init.valid:
            print("invalid plan")
            exit(0)
            
        print("88888888")
            
        return init
                   
    # infer  
    def infer(self, infer, image):
        
        det_boxes = infer.commit(image).get()
        
        return det_boxes
    