from Motor import Motor
from Motor_DTLever import Motor_DTLever
#from Arm_Class import Arm_Class
import Arm_Class
#import Controller as js
from ultrasonic_sensor_setup import distance
from Latch_Detect import Detect_Object

from time import sleep
from os import environ
from os import system
import pygame
import pigpio
import xarm
import math
import time
import RPi.GPIO as GPIO
import time
import KeyPressModule as kp

from Inverse_kinematic import IK
import os
import numpy as np


GPIO.setmode(GPIO.BCM)

trig = 23
echo = 24

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig, False)
time.sleep(2)




arm = xarm.Controller('USB')

def arm_start_mode():

    arm.setPosition(1, 500, wait=False)
    arm.setPosition(2, 500, wait=False)
    arm.setPosition(3, 500, wait=False)
    arm.setPosition(4, 500, wait=False)
    arm.setPosition(5, 500, wait=False)
    arm.setPosition(6, 500, wait=False)

def arm_trasition_mode():

    arm.setPosition(1, 500, wait=False)
    arm.setPosition(2, 430, wait=False)
    arm.setPosition(3, 500, wait=False)
    arm.setPosition(4, 756, wait=False)
    arm.setPosition(5, 500, wait=False)
    arm.setPosition(6, 500, wait=False)


def arm_stair_mode():

    arm.setPosition(1, 500, wait=False)
    arm.setPosition(2, 500, wait=False)
    arm.setPosition(3, 600, wait=False)
    arm.setPosition(4, 500, wait=False)
    arm.setPosition(5, 1000, wait=False)
    arm.setPosition(6, 500, wait=False)


arm_start_mode()


def movement(motor, movement_type, time):
    ## motor.move(power, turn, time)
    ## Negative value is okay, goes backwards
    if movement_type == 'foward':
        motor.move(speed = 0,turn= -1, t=time)
    elif movement_type == 'backward':
        motor.move(speed = 0,turn = 1,t=time)
    elif movement_type == 'right':
        motor.move(0.8, 0, time)
    elif movement_type == 'left':
        motor.move(-0.8, 0, t=time)
    elif movement_type == 'stop':
        motor.stop(t =time)
    else:
        print("Unknown movement type")
    motor.move(0,0,0.1)

def KeyBoard_Control(motor):

    if kp.getKey('UP'):
        motor.move(-0.6,0,0.1);
    elif kp.getKey('DOWN'):
        motor.move(0.6,0.1,0.1); ###print('Key DOWN was pressed')
    elif kp.getKey('LEFT'):
        motor.move(0.5,-0.3,0.1); ###print('Key LEFT was presssed')
    elif kp.getKey('RIGHT'):
        movement(motor, 'right', 0.4)
    elif kp.getKey('q'):
        arm_trasition_mode()
    elif kp.getKey('e'):
        arm_stair_mode()
    elif kp.getKey('r'):
        arm_start_mode()
    else:
        motor.stop(0.1)

def rotate(motor,ang):
    if(ang > 0):
        motor.move(0.8, 0, ang/44)
    else:
        motor.move(-0.8, 0, -ang/38)
    
    motor.move(0,0,0.1)

def Terminal_Control(motor):
    try:
        checkpoint = 0
        user_input = input("get input, separate by space, first element is control mode\n mode = arm,move,rotate\n")

        elements = user_input.split(' ')
        mode = elements[0]
        if mode == "manual":
            parsed_elements = [float(element.strip()) for element in elements[1:]]
            print(parsed_elements)
            arm.setPosition(1, round(parsed_elements[0]), wait=False)
            arm.setPosition(2, round(parsed_elements[1]), wait=False)
            arm.setPosition(3, round(parsed_elements[2]), wait=False)
            arm.setPosition(4, round(parsed_elements[3]), wait=False)
            arm.setPosition(5, round(parsed_elements[4]), wait=False)
        if mode == "grip":
            parsed_elements = [float(element.strip()) for element in elements[1:]]
            print(parsed_elements)
            if(-0.1 < parsed_elements[0] < 1.1):
                arm.setPosition(1, round(500 + 500 * parsed_elements[0]), wait=False)
            arm.setPosition(2, round(400 + 800*(parsed_elements[1]/180)), wait=False)
            print("ang[0:1]:",round(500 + 500 * parsed_elements[0]),' ',round(400 + 800*(parsed_elements[1]/180)))
        if mode == 'arm':
            #arm 14 18.5 40
            L1 = 4.5
            L2 = 6.1
            L3 = 6.5
            parsed_elements = [float(element.strip()) for element in elements[1:]]
            print(parsed_elements)
            [Arm_Extend,Elbow,Wrist] = IK(parsed_elements[0],parsed_elements[1],L1=L1,L2=L2,L3=L3)
            checkpoint = 1
            
            arm.setPosition(3, round(500 - 700 * (Wrist/np.pi)), wait=False)
            arm.setPosition(4, round(450 - 600 * (Elbow/np.pi)), wait=False)
            arm.setPosition(5, round(800 - 600 * Arm_Extend/np.pi), wait=False)
            # rotate(motor,np.rad2deg(Base))
            # if(move > 0.1):
            #     movement(motor,'foward',move/5)
            # if(move < 0.1):
            #     movement(motor,'backward',-move/5)
            print("ang[2:4]:",round(470 - 700 * (Wrist/np.pi)),' ',round(450 - 600 * (Elbow/np.pi)),' ',round(800 - 600 * Arm_Extend/np.pi))
        elif mode == 'demo':
            [speed,turn,t] = [float(element.strip()) for element in elements[1:]]
            #turn right: t = 2 -> 90 degree
            #turn left: t =2 -> 90 degree
            #
            if(t < 0):
                print("time error")
                return 0
            motor.move(speed,turn,t)
            motor.move(0,0,0.1)

        elif mode == 'move':
            [speed,turn,t] = [float(element.strip()) for element in elements[1:]]
            #turn right: t = 2 -> 90 degree
            #turn left: t =2 -> 90 degree
            #
            if(t < 0):
                print("time error")
                return 0
            if(turn > 0.1):
                movement(motor,'right',t)
            elif(turn < -0.1):
                 movement(motor,'left',t)
            else:
                if(speed > 0.1):
                    movement(motor,'foward',t)
                elif(speed < 0.1):
                    movement(motor,'backward',t)
            motor.move(0,0,0.1)
        elif mode == 'rotate':
            ang = float(elements[1])
            rotate(motor,ang)
        elif mode == "h-move":
            #assume positive is right
            [inch] = [float(element.strip()) for element in elements[1:]]

        if mode == 'photo':
            [number] = [int(element.strip()) for element in elements[1:]]
            print(number)
            command = "raspistill -o data/"+ str(number) + ".jpg -h 640 -w 640 -t 10 -rot 0"
            print(command)
            os.system(command)
        if mode == 'detect':
            xyxy = Detect_Object()
            print(xyxy)
        if mode == "dis":
            print(distance())
        if mode == "scan":
            xyxy = Detect_Object()
            print(xyxy)
            conf = 0
            while conf < 2:
                if xyxy.size == 0:
                    print("warning, the box is not detected")
                    rotate(motor,30)
                    xyxy = Detect_Object()
                    conf = 0
                else:
                    conf += 1
                    print(xyxy)
                    if((xyxy[0][0]+xyxy[0][2])/2 > 340):
                        rotate(motor,5)
                    if((xyxy[0][0]+xyxy[0][2])/2 < 300):
                        rotate(motor,-5)
                    movement(motor,'stop',0.1)
                    xyxy = Detect_Object()



    
    except ValueError:
        print("input is not valid number")
        print(checkpoint)
    except IndexError:
        print("Input not enough, or the distance is not possible")
        
    except TypeError:
        print("try appropritate value")
        print(checkpoint)


def Autonomous_Control(motor):
    while True:

        dist = distance()
        print(dist)

        if dist > 30 :
            movement(motor,'foward',0.1)
            dist = distance()
        else :
            movement(motor, 'right', 0.4)
            dist = distance()

        
        


        


        



    
    

    

   

       
   



    

def JoyStick_Control(motor, motor_DTLever): #servo1_2, servo3
    global oldtheta1, oldtheta2, oldtheta3,y, z, outofrange,angle1,angle2,angle3,angle4,angle5,angle6, arm, kinematics, shutdown_started

    motor.move(-js.getJS()['axis2'],-js.getJS()['axis1']) #Negatives Adjust for direction
    motor_DTLever.move(js.getJS()['L2'],js.getJS()['R2'])

    if js.getJS()[but1] == 1:
        angle1 = SetAngle(1,js.getJS()[direction2], js.getJS()[direction1], js.getJS()[but1],angle1,inc1,minang1,maxang1)
    if js.getJS()[but2] == 1:
        angle2 = SetAngle(2,js.getJS()[direction2], js.getJS()[direction1], js.getJS()[but2],angle2,inc2,minang2,maxang2)
    if js.getJS()[but3] == 1:
        angle3 = SetAngle(3,js.getJS()[direction1], js.getJS()[direction2], js.getJS()[but3],angle3,inc3,minang3,maxang3)
    if js.getJS()[but4] == 1:
        angle4 = SetAngle(4,js.getJS()[direction1], js.getJS()[direction2], js.getJS()[but4],angle4,inc4,minang4,maxang4)
    if js.getJS()[but5] == 1:
         angle5 = SetAngle(5,js.getJS()[direction1], js.getJS()[direction2], js.getJS()[but5],angle5,inc5,minang5,maxang5)
    if js.getJS()[but6] == 1:
        angle6 = SetAngle(6,js.getJS()[direction1], js.getJS()[direction2], js.getJS()[but6],angle6,inc6,minang6,maxang6)


#     if js.getJS()[change_kin_ang_but_1] == 1 and js.getJS()[change_kin_ang_but_2] == 1:

#         ang5=angle5*math.pi/180.0
#         ang4=angle4*math.pi/180.0
#         if -90 < angle5 < 90 and -120 < angle4 < 120 and -90 < angle3 < 90:
#             y = l1*math.sin(ang5)+15*math.cos(math.pi/2-ang5-ang4)
#             z = l1*math.cos(ang5)+15*math.cos(math.pi/2-ang5-ang4)
#             kinematics = True
#             ###print(kinematics)

#     if kinematics == True:
    oldy = y; oldz = z;
    if js.getJS()[butYpos] == 1 or js.getJS()[butYneg] == 1 or js.getJS()[butZpos] == 1 or js.getJS()[butZneg] == 1:
        theta1,theta2,theta3,y,z = SetNewCoord(js.getJS()[butYpos], js.getJS()[butYneg], js.getJS()[butZpos],js.getJS()[butZneg],y, z)
        if 11**2 < y**2+z**2 < 26.2**2 and y > 0:
            if minang5 < theta1 < maxang5 and minang4 < theta2 < maxang4 and minang3 < theta3 < maxang3:
                arm.setPosition(3,theta3,waitTime, wait=True)
                arm.setPosition(4,theta2,waitTime, wait=True)
                arm.setPosition(5,theta1,waitTime, wait=True)
                #print(round(theta3),round(theta2),round(theta1))
#                 arm.setPosition([[3,theta3],[4,theta2],[5,theta1]], waitTime, wait=True)

                ##print('y ', y, 'z ', z,theta1,theta2,theta3)
                oldtheta1 = theta1; oldtheta2 = theta2; oldtheta3 = theta3;
#                 oldy = y; oldz = z;

            else:
#                 arm.setPosition(3,oldtheta3,waitTime, wait=True)
#                 arm.setPosition(4,oldtheta2,waitTime, wait=True)
#                 arm.setPosition(5,oldtheta1,waitTime, wait=True)
                y = oldy
                z = oldz
                ##print('oldy ', oldy, 'oldz ',oldz,angle3, angle4, angle5)
                ###print('Out of workspace angle')

        else:
            arm.setPosition(3,oldtheta3,waitTime, wait=True)
            arm.setPosition(4,oldtheta2,waitTime, wait=True)
            arm.setPosition(5,oldtheta1,waitTime, wait=True)
#             arm.setPosition([[3,oldtheta3],[4,oldtheta2],[5,oldtheta1]], waitTime, wait=True)

            y = oldy
            z = oldz
            ##print('oldy ', oldy, 'oldz ',oldz,angle3, angle4, angle5)
            ###print('Out of workspace coordinate')


#         ###print(theta1,' ', theta2,' ', theta3, ' ', y , ' ' ,z)
#         if -90 < theta1 < 90 and -120 < theta2 < 120 and -90 < theta3 < 90:
#             pass
    #         arm.setPosition([[3,theta3],[4,theta2],[5,theta1]],waitTime,wait=True)
#             angle5 = theta1; angle4 = theta2; angle3 = theta3;
#         else:
#             ###print('Angle Out of Workspace')
#             theta1 = angle5; theta2 = angle4; theta3 = angle3;
#             outofrange +=1
#             if outofrange > 50:
#                 y = 3
#                 z = 15
#                 outofrange = 0



#     if js.getJS()[change_to_ang_but_1] == 1 and js.getJS()[change_to_ang_but_2] == 1 and js.getJS()[change_to_ang_but_3] == 1 and js.getJS()[change_to_ang_but_4] == 1:
#         kinematics = False
#         ###print(kinematics)

    if js.getJS()['L1'] == 1 and js.getJS()['L2'] == 1 and js.getJS()['R1'] == 1 and js.getJS()['R2'] == 1 and shutdown_started == False:
        shutdown_started = True
        system('shutdown now -h')


    sleep(0.01)

def Initialize_Objects(movement):
#     global angle1,angle2,angle3,angle4,angle5,angle6
    # arm = xarm.Controller('USB')

    motor = Motor(17,27,22,10)
    motor_DTLever = Motor_DTLever(9,11)

#     arm = xarm.Controller('USB')
#     servo1 = xarm.Servo(1,0.0)
#     servo2 = xarm.Servo(2,0.0)
#     servo3 = xarm.Servo(3,0.0)
#     servo4 = xarm.Servo(4,0.0)
#     servo5 = xarm.Servo(5,0.0)
#     servo6 = xarm.Servo(6,0.0)
#     sleep(1)
#     angle1 = arm.getPosition(1,True);angle2 = arm.getPosition(2,True);angle3 = arm.getPosition(3,True);angle4 = arm.getPosition(4,True);angle5 = arm.getPosition(5,True);angle6 = arm.getPosition(6,True);

#     arm.setPosition(1,0.0,wait=True)
#     arm.setPosition(2,0.0,wait=True)
#     arm.setPosition(3,0.0,wait=True)
#     arm.setPosition(4,0.0,wait=True)
#     arm.setPosition(5,0.0,wait=True)
#     arm.setPosition(6,0.0,wait=True)

#     arm.setPosition([[1,0.0],[2,0.0],[3,0.0],[4, 0.0],[5,0.0],[6,0.0]], 100, wait=True)

    # Define Method of Control
    # movement = 'JoyStick' #['KeyBoard','Joystick','Autonomous']
    # movement = 'KeyBoard'
#     movement = 'Autonomous'

    if movement == 'JoyStick':
        environ['DISPLAY'] = ':0'
        pygame.display.init()
#     elif movement == 'KeyBoard':
#         kp.init()
#     elif movement == 'Autonomous':
#         psuedo_var = 1
#         Establish camera object
#         serial_port = '/dev/ttyACM0'
#         ########serial_port = '/dev/ttyACM1'
#         pixy2 = Pixy2_Camera(serial_port)


    # Establish distance sensor objects # Set trigger and echo pins

#         trigL = 15;echoL = 14;trigR = 5;echoR = 6
#         dist1 = d#         trig1 = 26; echo1 = 6; trig2 = 20; echo2 = 21#; trig3 = ; echo3 =ist_sensor(trig1,echo1);dist2 = dist_sensor(trig2,echo2);
#         distL = distance_sensor(trigL,echoL);distR = distance_sensor(trigR,echoR)

        # Blue Arm
        # pin1 =  # pin control of servo
        # pin2 =
        # servo1 = Blue_Arm_Class(pin1)
        # servo2 = Blue_Arm_Class(pin2)
        # ser#     minangle = -100.0
#     maxangle = 100.0

#     if button3 == 1:
#         if button1 == 1 and button2 == 1:
#             pass vo1.moveto(angle1) # Move command
    return motor, motor_DTLever#, arm, servo1, servo2, servo3, servo4, servo5, servo6 #  servo_motor, pixy2, dist1,dist2, , servo3 #, servo4, servo5




def SetNewCoord(button1,button2,button3,button4,y,z):
    global angle3, angle4, angle5
    increment = 0.35
#     ###print('R1 ',js.getJS('R1'),'o ',js.getJS('o'),'L1 ',js.getJS('L1'),'x ',js.getJS('x'))
    #print(button1,button2,button3,button4)
#     ###print('Begin getAngle')


    if button1 == 1 and button2 == 0 and button3 == 0 and button4 == 0:
        if l1**2 < (y+increment)**2 + z**2 < (l1+l2)**2 and y > 0:
            y+=increment
        else:
            pass
            ###print('Out of Range y+')
        ###print('y is ',y)
    elif button1 == 0 and button2 == 1 and button3 == 0 and button4 == 0:
        if l1**2 < (y-increment)**2 + z**2 < (l1+l2)**2 and y > 0:
#             2-math.atan(z/y)-delta
            y-=increment
        else:
            pass
            ###print('Out of Range y-')
        ###print('y is ',y)
    elif button1 == 0 and button2 == 0 and button3 == 1 and button4 == 0:
        if l1**2 < (y)**2 + (z+increment)**2 < (l1+l2)**2:
            z+=increment
        else:
            pass
            ###print('Out of Range z+')
        ###print('z is ',z)
    elif button1 == 0 and button2 == 0 and button3 == 0 and button4 == 1:
        if l1**2 < (y)**2 + (z-increment)**2 < (l1+l2)**2:
            z-=increment
        else:
            pass
            ###print('Out of Range z-')
        ###print('z is ',z)




    ###print('acos() ', (l1**2+l2**2-y**2-z**2)/(2*l1*l2))
    if -1 <= (l1**2+l2**2-y**2-z**2)/(2*l1*l2) <= 1:
        gamma = math.acos((l1**2+l2**2-y**2-z**2)/(2*l1*l2))
        if -1 <= (l2*math.sin(gamma))/math.sqrt(y**2+z**2) <= 1:
#           (2-math.atan(z/y)-math.asin((l2*math.sin(gamma))/math.sqrt(y**2+z**2))) != 0
            theta2 = math.pi-gamma
            delta = math.asin((l2*math.sin(gamma))/math.sqrt(y**2+z**2))
            theta1 = math.pi/2-math.atan(z/y)-delta
            theta1 = theta1*180.0/math.pi
            theta2 = theta2*180.0/math.pi
            theta3 = theta1 + theta2 - 90.0 + 12 # 12 is offset for theta 3
#             theta3 = -(math.atan(z/y)+ delta+ gamma - math.pi)*180.0/math.pi+12.0
        else:
            theta1 = angle5; theta2 = angle4; theta3 = angle3;
            ###print(theta1, theta2, theta3)
            return
    else:
        theta1 = angle5; theta2 = angle4; theta3 = angle3;
        ###print(theta1, theta2, theta3)
        return



#     theta1 = 0.0
#     theta2 = 0.0
#     theta3 = 0.0

#     ###print("theta1 is", theta1)
#     ###print("theta2 is", theta2)
#     ###print('theta3 is ', theta3)
#     sleep(0.25)
    return theta1, theta2, theta3, y, z





def SetAngle(numservo,button1,button2,button3,angle,increment,minangle=-100,maxangle=100):

#     increment = 5
#     minangle = -100.0
#     maxangle = 100.0
    #print(button1,button2,button3)

    if button3 == 1:
        if button1 == 1 and button2 == 1:
            pass
        elif button1== 1 and button2 == 0:
            angle += increment
#             ###print(angle)
            if angle >= maxangle:
                angle = maxangle
            elif angle <= minangle:
                angle = minangle
        elif button1 == 0 and button2 == 1:
            angle -= increment
#             ###print(angle)
            if angle >= maxangle:
                angle = maxangle
            elif angle <= minangle:
                angle = minangle

    arm.setPosition(numservo,round(float(angle),2),waitTime, wait=True)
    ###print(angle)

    return round(float(angle),2)
