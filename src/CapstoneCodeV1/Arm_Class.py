import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import xarm


class Arm_Class_blue():
    def __init__(self,servo_id,init_angle):


        self.servo_id = servo_id
        self.init_angle = init_angle
        servo_object = xarm.Servo(self.servo_id, self.init_angle)
        self.minduty = -125
        self.maxduty = 125
#         angle range -125 to 125
#         return servo_object




    def moveto(self,button1,button2,button3,angle):
        if button3 == 1:
            if button1 == 1 and button2 == 1:
                angle+=0
            elif button1 == 1:
                if angle >= self.maxduty:
                    angle = self.maxduty
                else:
                    angle+=1
            elif button2 == 1:
                if angle <= self.minduty:
                    angle = self.minduty
                else:
                    angle-=1
            else:
                self.stop(angle)
        else:
            angle+=0

        self.xarm.setPosition(self.servo_id, angle, 500, wait=True)
        return angle
#         angle must be input as float aka 90.0

    def stop(self,angle):
        self.xarm.setPosition(self.servo_id, angle, 500, wait=True)



