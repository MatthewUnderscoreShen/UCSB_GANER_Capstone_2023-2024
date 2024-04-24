from ultralytics import YOLO
from skimage import io
import numpy as np
import os

from Motor import Motor
from Motor_DTLever import Motor_DTLever
#import test_arm as ctl
import math
import RPi.GPIO as GPIO
# Define Method of Control
#movement = 'JoyStick'
# movement = 'KeyBoard'
def Initialize_Objects(movement):
#     global angle1,angle2,angle3,angle4,angle5,angle6
    # arm = xarm.Controller('USB')

    motor = Motor(17,27,22,10)
    motor_DTLever = Motor_DTLever(9,11)
    return motor, motor_DTLever
# motor, motor_DTLever, servo_motor, pixy2, dist1,dist2, servo1_2, servo3 = ctl.Initialize_Objects(movement)
motor, motor_DTLever = Initialize_Objects('Autonomous')
def movement(motor, movement_type, time):
    ## motor.move(power, turn, time)
    ## Negative value is okay, goes backwards
    if movement_type == 'foward':
        motor.move(speed = 0.5,turn= -1, t=time)
    elif movement_type == 'backward':
        motor.move(speed = 0.5,turn = 1,t=time)
    elif movement_type == 'right':
        motor.move(1, 0.5, time)
    elif movement_type == 'left':
        motor.move(1, -0.5, t=time)
    elif movement_type == 'stop':
        motor.stop(t =time)
    else:
        print("Unknown movement type")
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
        xyxy = Detect_Object()
        
        while True:
            if xyxy.size == 0:
                print("warning, the box is not detected")
                movement(motor, 'right', 0.4)
                xyxy = Detect_Object()
            else:
                print(xyxy)

                
            

    except KeyboardInterrupt:
        print('Execution Aborted By User')
        GPIO.cleanup()
    










