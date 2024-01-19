from MotorModule_High_Current import Motor
from MotorModule_DTLever_High_Current import Motor_DTLever
import new_controller as js
from time import sleep
from os import environ
from os import system
import pygame
import xarm
import math
import time 

#set up button mappings for directional buttons, PS4 controller
butYpos = 'Dpad up'
butYneg = 'Dpad down'
butZpos = 'Dpad left'
butZneg = 'Dpad right'

# Min and max angle values for each joint
xarmmin = -125.0
xarmmax = 125.0
minang1 = -11
maxang1 = 32
minang2 = xarmmin
maxang2 = xarmmax
minang3 = xarmmin
maxang3 = xarmmax
minang4 = xarmmin
maxang4 = xarmmax
minang5 = -78.0
maxang5 = 91.0

# initialization values for the robot arm 
oldtheta3 = -20.0
oldtheta2 = 100.0
oldtheta1 = -45.0
# prepare new theta value in 'for' loop
theta1 = 0.0
theta2 = 0.0
theta3 = 0.0
y = 3
z = 15

# set Initial mode 
kinematics = False
shutdown_started = False

# Lengths of links in the arm 
l1 = 11
l2 = 15.2

# time to wait between commands 
waitTime = 1
outofrange = 0

# Initialize xArm and servos 
arm = xarm.Controller('USB')
servo1 = xarm.Servo(1,0.0)
servo2 = xarm.Servo(2,0.0)
servo3 = xarm.Servo(3,0.0)
servo4 = xarm.Servo(4,0.0)
servo5 = xarm.Servo(5,0.0)
servo6 = xarm.Servo(6,0.0)
sleep(1)

# Initialize angles for each joint
#    Notice: In xarm, the position paramter may be an int to indicate a unit position (0 to 1000)
#    or a float to indicate an angle in degrees (-125.0 to 125.0).
angle1 = 0.0
angle2 = 0.0
angle3 = -21.0
#angle4 = 118.0
angle4 = 75.0
angle5 = -62.0

# set the initial arm position:
angleList_init = [angle1, angle2, angle3, angle4, angle5]
angleList_climing = [0.0,0.0,0.0,50.0,0.0]
for i in range(5):
    arm.setPosition(5-i, angleList_init[5-i-1], 800, wait=True)

def JoyStick_Control(motor, motor_DTLever):
    """
    Function: Run motors based on JoyStick control, including chassis motors, tail motor, arm motors
    
    Input variables:
        1. motor: object from the "motor" class; use for controlling chassis motor
        2. motor_DTLever: object from the "motor_DTLever" class; use for controlling tail motor
    Global Variable:
        Variables that are subjected to change globally, including
        "oldtheta1, oldtheta2, oldtheta3,y, z, outofrange,angle1,angle2,angle3,angle4,angle5,angle6, arm, kinematics, shutdown_started"
    """
    global oldtheta1, oldtheta2, oldtheta3,y, z, outofrange,angle1,angle2,angle3,angle4,angle5,angle6, arm, kinematics, shutdown_started

    ## Move the chassis motor based on the left joystick input
    motor.move(-js.getJS()['axis2'],-js.getJS()['axis1']) #Negatives Adjust for direction
    ## Move the tail motor based on the "L2" and "R2" control
    motor_DTLever.move(js.getJS()['L2'],js.getJS()['R2'])

    print(js.getJS())
    ## Two default positions:
    # set initial servo position: (number of servo, angle_desired, time span (ms))
    angleList_current = [angle1,angle2,angle3,angle4,angle5]
    if js.getJS()['share'] == 1:# and js.getJS()['options'] == 0:
        SetAngleList(5, angleList_current,angleList_init, 1000)
        angle1,angle2,angle3,angle4,angle5 = angleList_init
        print('set preset 1')
    # set the arm motors to climing position
    if js.getJS()['options'] == 1:# and js.getJS()['share']==0:
        SetAngleList(5,angleList_current, angleList_climing, 1000)
        angle1,angle2,angle3,angle4,angle5 = angleList_climing
    ## set the gripper and waist motion through motors 1,2
    # Incremental step values for joystick and button presses
    inc1 = 5.0
    inc2 = 3.0
    # 't' - gripper open, 'x' - gripper close, 'o' - waist turn clockwise, 's' - waist turn conter-clockwise
    if js.getJS()['t'] == 1:  # triangular
        angle1 = SetAngle(1,angle1,inc1,-125,125)
    if js.getJS()['x'] == 1:  # 'x'
        angle1 = SetAngle(1,angle1,-inc1,-125,125)
    if js.getJS()['o'] == 1:  # circle
        angle2 = SetAngle(2,angle2,inc2)
    if js.getJS()['s'] == 1:  # square
        angle2 = SetAngle(2,angle2,-inc2)


    ## set the arm position through motors 3,4,5
    oldy = y; oldz = z
    if js.getJS()[butYpos] == 1 or js.getJS()[butYneg] == 1 or js.getJS()[butZpos] == 1 or js.getJS()[butZneg] == 1:
        # calculate the new theta angles and y z positions
        theta1,theta2,theta3,y,z = SetNewCoord(js.getJS()[butYpos], js.getJS()[butYneg], js.getJS()[butZpos],js.getJS()[butZneg],y, z)

        ## check whether the calculated value can be reached
        # whether the range of motion is satisfied based on the length of two linkages
        if 11**2 < y**2+z**2 < 26.2**2 and y > 0:
            # whether the desired angles are within the range
            if minang5 < theta1 < maxang5 and minang4 < theta2 < maxang4 and minang3 < theta3 < maxang3:
                arm.setPosition(3,theta3,waitTime, wait=True)
                arm.setPosition(4,theta2,waitTime, wait=True)
                arm.setPosition(5,theta1,waitTime, wait=True)
                oldtheta1 = theta1; oldtheta2 = theta2; oldtheta3 = theta3
            else:
                y = oldy
                z = oldz
                print('oldy ', oldy, 'oldz ',oldz,angle3, angle4, angle5)
                print('Out of workspace angle')
        else:
            arm.setPosition(3,oldtheta3,waitTime, wait=True)
            arm.setPosition(4,oldtheta2,waitTime, wait=True)
            arm.setPosition(5,oldtheta1,waitTime, wait=True)
            y = oldy
            z = oldz
            print('oldy ', oldy, 'oldz ',oldz,angle3, angle4, angle5)
            print('Out of workspace coordinate')

    ## shutdown shortcut
    if js.getJS()['L1'] == 1 and js.getJS()['L2'] == 1 and js.getJS()['R1'] == 1 and js.getJS()['R2'] == 1 and shutdown_started == False:
        shutdown_started = True
        system('shutdown now -h')
    sleep(0.01)

def Initialize_Objects(movement):
    motor = Motor(17,27,22,10)
    motor_DTLever = Motor_DTLever(9,11)
    if movement == 'JoyStick':
        environ['DISPLAY'] = ':0'
        pygame.display.init()
    return motor, motor_DTLever#, arm, servo1, servo2, servo3, servo4, servo5, servo6 #  servo_motor, pixy2, dist1,dist2, , servo3 #, servo4, servo5


def SetNewCoord(button1,button2,button3,button4,y,z):
    '''
    Functions: calculate angles and distances required for the gripper to reach certain position
    Input:
        1. "button1,button2,button3,button4" are the directional buttons in PS4 controller
        2. "y,z" are the y, z positions for the gripper position

    Output:
        1. new y,z values based on the time and increment value
        2. angles for arm motors that control the arm linkage (motor 2,3,4)
    '''
    global angle3, angle4, angle5
    
    # set increment for the z,y coordinates
    increment = 0.35       
    print(button1,button2,button3,button4)
    
    # Change y,z position based on the button info
    if button1 == 1 and button2 == 0 and button3 == 0 and button4 == 0:
        if l1**2 < (y+increment)**2 + z**2 < (l1+l2)**2 and y > 0:
            y+=increment
        else:
            pass
    elif button1 == 0 and button2 == 1 and button3 == 0 and button4 == 0:
        if l1**2 < (y-increment)**2 + z**2 < (l1+l2)**2 and y > 0:
            y-=increment
        else:
            pass
    elif button1 == 0 and button2 == 0 and button3 == 1 and button4 == 0:
        if l1**2 < (y)**2 + (z+increment)**2 < (l1+l2)**2:
            z+=increment
        else:
            pass
    elif button1 == 0 and button2 == 0 and button3 == 0 and button4 == 1:
        if l1**2 < (y)**2 + (z-increment)**2 < (l1+l2)**2:
            z-=increment
        else:
            pass
        
    # calculate the angle change for all motors
    if -1 <= (l1**2+l2**2-y**2-z**2)/(2*l1*l2) <= 1:
        gamma = math.acos((l1**2+l2**2-y**2-z**2)/(2*l1*l2))
        if -1 <= (l2*math.sin(gamma))/math.sqrt(y**2+z**2) <= 1:
            theta2 = math.pi-gamma
            delta = math.asin((l2*math.sin(gamma))/math.sqrt(y**2+z**2))
            theta1 = math.pi/2-math.atan(z/y)-delta
            theta1 = theta1*180.0/math.pi
            theta2 = theta2*180.0/math.pi
            theta3 = theta1 + theta2 - 90.0 + 12 # 12 is offset for theta 3
        else:
            theta1 = angle5; theta2 = angle4; theta3 = angle3;
            return
    else:
        theta1 = angle5; theta2 = angle4; theta3 = angle3;
        return
    return theta1, theta2, theta3, y, z


def SetAngle(numservo,angle,increment,minangle=-100.0,maxangle=100.0):
    '''
    The function can be used to control the arm motor individually

    Input:
        numservo: the servo number
        angle: the desired angle
        increment: increment for each loop
        minangle & maxangle: angle constraints for motors, here the value is based on motor 3,4,5
    '''
    angle += increment
    print(angle)
    if angle >= maxangle:
        angle = maxangle
    elif angle <= minangle:
        angle = minangle
    arm.setPosition(numservo,round(float(angle),2),waitTime, wait=True)
    return round(float(angle),2)

def SetAngleList(numrange, angleList_i, angleList_f,timespan):
    '''
    Function: Set all the arm motors at once

    Notice: numrange here is due to the fact that we use motor 1 to 5. otherwise, you might want to change the function
    Fix: arm.setPosition only takes in angle info with second point decimal places
    '''
    #start_time = time.time()
    
    for i in range(numrange):
        print(i,angleList_i[i], angleList_f[i])
        angle_diff = abs(angleList_i[i] - angleList_f[i])
        if angle_diff > 0.01:      # only set position if there's a difference greater than 0.001 radians
            arm.setPosition(i+1, round(float(angleList_f[i]),2), timespan, wait=True)
    
    #end_time = time.time()
    #print("Time passed: %f"%(end_time - start_time))
