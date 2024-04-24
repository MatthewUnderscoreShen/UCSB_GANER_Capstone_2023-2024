from ultralytics import YOLO
from skimage import io
import numpy as np
import os

def Detect_Object():
    model = YOLO('best.pt') 
    os.system('raspistill -o image.jpg -h 640 -w 640 -t 10 -rot 0')
    results = model(['image.jpg'])  # return a list of Results objects
    xyxy = results[0].boxes.xyxy.numpy()
    print(xyxy)

if __name__ == '__main__':
    Detect_Object()