import RPi.GPIO as GPIO
import numpy as np

class Encoder(object):

    def __init__(self, ch_A_pin, ch_B_pin):
        self.ch_A_pin = ch_A_pin    # pwm pin
        self.ch_B_pin = ch_B_pin      # direction pin

        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.ch_A_pin, GPIO.IN)
        GPIO.setup(self.ch_B_pin, GPIO.IN)

    def read(self):
        return (GPIO.input(self.ch_A_pin), GPIO.input(self.ch_B_pin))