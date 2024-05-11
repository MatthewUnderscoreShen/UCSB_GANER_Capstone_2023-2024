import RPi.GPIO as GPIO
import numpy as np

class Motor(object):

    def __init__(self, pwm_pin, dir_pin, hz, is_left):
        self.pwm_pin = pwm_pin      # pwm pin
        self.dir_pin = dir_pin      # direction pin
        self.hz = hz                # pwm hertz
        self.is_left = is_left      # is this the left motor?
        self.min_pow = 0.30*hz      # minimum to not stall

        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, self.hz)   # pin, Hz
        self.pwm.start(0)

    def set_teleop(self, is_teleop):
        self.is_teleop = is_teleop

    def set_vel(self, vel):     # Assumes a 0-1 float input
        # Set motor direction. high/low reversed for right motor
        if vel != 0 and vel/np.abs(vel) > 0:  # Forwarwd
            GPIO.output(self.dir_pin, GPIO.HIGH if self.is_left else GPIO.LOW)
        else:   # Backwards
            GPIO.output(self.dir_pin, GPIO.LOW if self.is_left else GPIO.HIGH)
        
        # Changes the control profile to be less sensitive at low inputs
        if vel != 0:
            self.pwm.ChangeDutyCycle(max(self.min_pow,self.hz*np.abs(np.power(vel, 3))))
        else:
            self.stop()

    def stop(self):
        self.pwm.ChangeDutyCycle(0)