import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Arm_Class_js():
    def __init__(self,pin1,pin2,freq,minduty1,maxduty1,minduty2,maxduty2,increment1,increment2):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pulse_in_Hz = freq # 50 for 5v and 400 for 12v
        GPIO.setup(self.pin1,GPIO.OUT)
        GPIO.setup(self.pin2,GPIO.OUT)
        self.servo1 = GPIO.PWM(self.pin1,self.pulse_in_Hz) # Note: 50 = 50Hz pulse
        self.servo2 = GPIO.PWM(self.pin2,self.pulse_in_Hz)
        self.servo1.start(0)
        self.servo2.start(0)
        self.minduty1 = minduty1
        self.maxduty1 = maxduty1
        self.minduty2 = minduty2
        self.maxduty2 = maxduty2
        self.increment1 = increment1
        self.increment2 = increment2


    def moveto(self, axis1, axis2, angle1, angle2):

#         increment1 = .25
#         increment2 = .25

        if axis1 != 0:
            if angle1 >= self.minduty1 and angle1 <= self.maxduty1:
                angle1+= self.increment1*axis1
            if angle1 < self.minduty1:
                angle1 = self.minduty1
            elif angle1 > self.maxduty1:
                angle1 = self.maxduty1
            self.servo1.ChangeDutyCycle(round(angle1,2))
        else:
            self.servo1.ChangeDutyCycle(0)
        if axis2 != 0:
            if angle2 >= self.minduty2 and angle2 <= self.maxduty2:
                angle2+= self.increment2*axis2
            if angle2 <= self.minduty2:
                angle2 = self.minduty2
            elif angle2 >= self.maxduty2:
                angle2 = self.maxduty2
            self.servo2.ChangeDutyCycle(round(angle2,2))
        else:
            self.servo2.ChangeDutyCycle(0)


        sleep(0.01)
        return angle1, angle2

    def stop(self):
        self.servo1.stop()
        self.servo2.stop()

        sleep(0.1)