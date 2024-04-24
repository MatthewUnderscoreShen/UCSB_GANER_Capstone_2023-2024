from ultralytics import YOLO
from skimage import io
import numpy as np
import os

from Control_Options_autonomous import Initialize_Objects
from Control_Options_autonomous import movement
#import test_arm as ctl
import math
import RPi.GPIO as GPIO
# Define Method of Control
#movement = 'JoyStick'
# movement = 'KeyBoard'
movement = 'Autonomous'

# motor, motor_DTLever, servo_motor, pixy2, dist1,dist2, servo1_2, servo3 = ctl.Initialize_Objects(movement)
motor, motor_DTLever = Initialize_Objects(movement)

# some prequisit from control option





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
            movement(motor,'right',0.1)
            

    except KeyboardInterrupt:
        print('Execution Aborted By User')
        GPIO.cleanup()
    
