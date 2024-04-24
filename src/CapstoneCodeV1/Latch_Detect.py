from ultralytics import YOLO
from skimage import io
import numpy as np
import os

import Control_Options_autonomous as ctl
#import test_arm as ctl
import xarm
import math
import RPi.GPIO as GPIO

def Detect_Object():
    model = YOLO('best.pt') 
    os.system('raspistill -o image.jpg -h 640 -w 640 -t 10 -rot 0')
    results = model(['image.jpg'])  # return a list of Results objects
    xyxy = results[0].boxes.xyxy.numpy()
    print(xyxy)
    return xyxy

if __name__ == '__main__':
    try:
        xy = Detect_Object()
        while True:
            xy = Detect_Object()
            

    except KeyboardInterrupt:
        print('Execution Aborted By User')
        GPIO.cleanup()
    
