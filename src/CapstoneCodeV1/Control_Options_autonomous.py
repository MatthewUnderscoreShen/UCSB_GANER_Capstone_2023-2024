from Motor import Motor
from Motor_DTLever import Motor_DTLever
#from Arm_Class import Arm_Class
import Arm_Class
#import Controller as js
from ultrasonic_sensor_setup import distance

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


def latch_subroutine():

    # if latch_detected == True:

    arm.setPosition(1, 500, wait=False)
    arm.setPosition(2, 430, wait=False)
    arm.setPosition(3, 500, wait=False)
    arm.setPosition(4, 756, wait=False)
    arm.setPosition(5, 500, wait=False)
    arm.setPosition(6, 500, wait=False)

    movement('foward', 1)
    movement('right',1)
    movement('backward',1)

    arm_trasition_mode()

    movement('foward',1)
    

    

    



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

def KeyBoard_Control(motor):

    if kp.getKey('UP'):
        motor.move(0.6,0,0.1); ###print('Key UP was pressed')
    elif kp.getKey('DOWN'):
        motor.move(-0.6,0,0.1); ###print('Key DOWN was pressed')
    elif kp.getKey('LEFT'):
        motor.move(0.5,0.3,0.1); ###print('Key LEFT was presssed')
    elif kp.getKey('RIGHT'):
        motor.move(0.5,-0.3,0.1); ###print('Key RIGHT was pressed')
    else:
        motor.stop(0.1)


def Autonomous_Control(motor):
    arm_start_mode()

    while True:

        dist = distance()
        print(dist)

        if dist > 30 :
            motor.move(0.6,0,0.1); ###print('Key UP was pressed')
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
