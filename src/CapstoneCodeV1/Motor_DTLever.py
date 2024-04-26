import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor_DTLever():
    def __init__(self,EnaA,In1A):
        self.EnaA = EnaA
        self.In1A = In1A
        GPIO.setup(self.EnaA,GPIO.OUT)
        GPIO.setup(self.In1A,GPIO.OUT)
        self.pwmA = GPIO.PWM(EnaA,100);
        self.pwmA.start(0);

    def move(self,button_1,button_2,button_3=0,button_4=0):
        button_1+=1; button_2+=1;
        button_1/=2; button_2/=2;
        button_1 *=100; button_2*=100;

        if button_1 > 100: button_1 = 100
        elif button_1 < -100: button_1 = -100
        if button_2 > 100: button_2 = 100
        elif button_2 < -100: button_2 = -100

        speed = 50

        if button_1 == 0 and button_2 == 0 and button_3 == 1 and button_4 == 1:
            pass
        elif button_1 == 0 and button_2 == 0 and button_3 == 0 and button_4 == 1:
            GPIO.output(self.In1A,GPIO.HIGH)
            self.pwmA.ChangeDutyCycle(speed);
        elif button_1 == 0 and button_2 == 0 and button_3 == 1 and button_4 == 0:
            GPIO.output(self.In1A,GPIO.LOW)
            self.pwmA.ChangeDutyCycle(speed);
        elif button_1 != 0 and button_2 != 0 and button_3 == 0 and button_4 == 0:
            pass
        elif button_2 > 0 and button_1 == 0 and button_3 == 0 and button_4 == 0:
            GPIO.output(self.In1A,GPIO.HIGH)
            self.pwmA.ChangeDutyCycle(button_2);
#             print(button_2)
        elif button_1 > 0 and button_2 == 0 and button_3 == 0 and button_4 == 0:
            GPIO.output(self.In1A,GPIO.LOW)
            self.pwmA.ChangeDutyCycle(button_1);
#             print(button_1)
        else:
            self.pwmA.ChangeDutyCycle(0);


    def stop(self):
        self.pwmA.ChangeDutyCycle(0);