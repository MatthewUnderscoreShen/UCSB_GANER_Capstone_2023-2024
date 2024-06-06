from ultralytics import YOLO
from skimage import io
import numpy as np
import os

from Motor import Motor
from Motor_DTLever import Motor_DTLever
from time import sleep
#import test_arm as ctl
import math
import RPi.GPIO as GPIO
# Define Method of Control
#movement = 'JoyStick'
# movement = 'KeyBoard'
# def Initialize_Objects(movement):
# #     global angle1,angle2,angle3,angle4,angle5,angle6
#     # arm = xarm.Controller('USB')

#     motor = Motor(17,27,22,10)
#     motor_DTLever = Motor_DTLever(9,11)
#     return motor, motor_DTLever
# # motor, motor_DTLever, servo_motor, pixy2, dist1,dist2, servo1_2, servo3 = ctl.Initialize_Objects(movement)
# motor, motor_DTLever = Initialize_Objects('Autonomous')
# def movement(motor, movement_type, time):
#     ## motor.move(power, turn, time)
#     ## Negative value is okay, goes backwards
#     if movement_type == 'foward':
#         motor.move(speed = 0.5,turn= -1, t=time)
#     elif movement_type == 'backward':
#         motor.move(speed = 0.5,turn = 1,t=time)
#     elif movement_type == 'right':
#         motor.move(1, 0.5, time)
#     elif movement_type == 'left':
#         motor.move(1, -0.5, t=time)
#     elif movement_type == 'stop':
#         motor.stop(t =time)
#     else:
#         print("Unknown movement type")
# some prequisit from control option






# emergency button detect(if button model does not work)
# import cv2

# def Button_detect():
#     os.system('raspistill -o image.jpg -h 640 -w 640 -t 10 -rot 0')
#     image = cv2.imread('image.jpg')
    
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
#     lower_red1 = np.array([0, 120, 70])
#     upper_red1 = np.array([10, 255, 255])
#     lower_red2 = np.array([170, 120, 70])
#     upper_red2 = np.array([180, 255, 255])
    
#     # red mask
#     mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
#     mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
#     mask = mask1 + mask2
    
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     if contours:
#         largest_contour = max(contours, key=cv2.contourArea)
        
#         x, y, w, h = cv2.boundingRect(largest_contour)
        
#         return [x,y,x+w,y+h]
#     else:
#         return None



def Detect_Object(object = "default"):
    if(object == "Button"):
        model = YOLO('Button.pt')  
    elif (object == "Latch"):
        model = YOLO('Latch.pt')  
    else:
        model = YOLO('best.pt')  
    model.conf = 0.20
    os.system('raspistill -o image.jpg -h 640 -w 640 -t 10 -rot 0')
    results = model(['image.jpg'])  # return a list of Results objects
    xyxy = results[0].boxes.xyxy.numpy()
    return xyxy

if __name__ == '__main__':
    try:
         xyxy = Detect_Object()
         print(xyxy)
        
    #     while True:
    #         if xyxy.size == 0:
    #             print("warning, the box is not detected")
    #             movement(motor, 'right', 0.3)
    #             movement(motor,'stop',0.1)
    #             xyxy = Detect_Object()
    #         else:
    #             print(xyxy)
    #             if((xyxy[0][0]+xyxy[0][2])/2 > 340):
    #                 movement(motor, 'right', 0.1)
    #             if((xyxy[0][0]+xyxy[0][2])/2 < 300):
    #                 movement(motor, 'left', 0.1)
    #             movement(motor,'stop',0.1)
    #             xyxy = Detect_Object()

                
            

    except KeyboardInterrupt:
        print('Execution Aborted By User')
        GPIO.cleanup()
    










