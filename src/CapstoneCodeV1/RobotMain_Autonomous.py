import Control_Options_autonomous as ctl
#import test_arm as ctl
import xarm
import math
import RPi.GPIO as GPIO


# Define Method of Control
#movement = 'JoyStick'
# movement = 'KeyBoard'
movement = 'Autonomous'

# motor, motor_DTLever, servo_motor, pixy2, dist1,dist2, servo1_2, servo3 = ctl.Initialize_Objects(movement)
motor, motor_DTLever = ctl.Initialize_Objects(movement)
############################################################

def main():
#     global current_angle # current_angle of servo motor
#     global angle1
#     Input all objects into functions
    if movement == 'JoyStick':
        ctl.JoyStick_Control(motor, motor_DTLever)
    elif movement == 'KeyBoard':
        ctl.KeyBoard_Control(motor)
    elif movement == 'Autonomous':
        ctl.Autonomous_Control(motor)
    else:
        print('Set Type of Control')


if __name__ == '__main__':
    try:
        while True:
            main().

    except KeyboardInterrupt:
        print('Execution Aborted By User')
        GPIO.cleanup()