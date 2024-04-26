import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self,EnaA,In1A,EnaB,In1B):
        self.EnaA = EnaA
        self.In1A = In1A
        self.EnaB = EnaB
        self.In1B = In1B
        GPIO.setup(self.EnaA,GPIO.OUT)
        GPIO.setup(self.In1A,GPIO.OUT)
        GPIO.setup(self.EnaB,GPIO.OUT)
        GPIO.setup(self.In1B,GPIO.OUT)
        self.pwmA = GPIO.PWM(EnaA,100);
        self.pwmA.start(0);
        self.pwmB = GPIO.PWM(EnaB,100);
        self.pwmB.start(0);

    def move(self,speed=0.5,turn=0,t=0):

        if speed < -0.5: turn*=-1 # Joystick down and left moves robot backwards and left
        maxPWM_norm = 1

        # Apply Exponential growth to outputs for more sensitive control over slow movement (for Stairs)
        sensitivity = 100 # higher sensitivity --> steeper slope
        if speed > 0: speed = sensitivity**abs(speed)/sensitivity # Apply Exponential remap
        elif speed < 0: speed = -sensitivity**abs(speed)/sensitivity # Deal with negative case
        if turn > 0: turn = sensitivity**abs(turn)/sensitivity # Apply Exponential remap
        elif turn < 0: turn = -sensitivity**abs(turn)/sensitivity # Deal with negative case
#        # elif speed == 0: speed = 0 Just in case it doesn't stop moving

#         Turning
        leftSpeed = speed + turn
        rightSpeed = speed - turn

        if leftSpeed > maxPWM_norm: leftSpeed = maxPWM_norm
        elif leftSpeed < -maxPWM_norm: leftSpeed = -maxPWM_norm
        if rightSpeed > maxPWM_norm: rightSpeed = maxPWM_norm
        elif rightSpeed < -maxPWM_norm: rightSpeed = -maxPWM_norm

        # Normalize from -1 to 1 to PWM -100 to 100
        maxPWM = 100
        leftSpeed *= maxPWM
        rightSpeed *= maxPWM
        # Set Motor Speeds
        self.pwmA.ChangeDutyCycle(abs(leftSpeed));
        self.pwmB.ChangeDutyCycle(abs(rightSpeed));

        # Set Motor Directions
        if leftSpeed > 0:
            GPIO.output(self.In1A,GPIO.HIGH)
        else:
            GPIO.output(self.In1A,GPIO.LOW)
        if rightSpeed > 0:
            GPIO.output(self.In1B,GPIO.LOW)
        else:
            GPIO.output(self.In1B,GPIO.HIGH)


        sleep(t)

    def stop(self,t=0):
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);
        sleep(t)

def main():
     motor1.moveF(60,2)
     motor1.stop(2)
     motor1.moveF(60,2)
     motor1.stop(2)

# if __name__ == '__main__':
#    motor1 = Motor(2,3,4,22,17,27) #pin numbers
#    main()