#!/usr/bin/env python3
from ultralytics import YOLO
from skimage import io
import os

class Camera(object):

    def Detect_Object(self):
        model = YOLO('best.pt') 
        os.system('raspistill -o image.jpg -h 640 -w 640 -t 10 -rot 0')
        results = model(['image.jpg'])  # return a list of Results objects
        xyxy = results[0].boxes.xyxy.numpy()
        return xyxy