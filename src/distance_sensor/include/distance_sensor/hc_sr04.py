import time
import RPi.GPIO as GPIO

class HCSR04(object):

    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo

        self.timeout = 0.05

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def distance(self):
        GPIO.output(self.trigger, True) # set trigger to HIGH

        # set trigger after 0.01 ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        startTime = time.time()
        arrivalTime = time.time()

        timeout_start = time.time()

        # store startTime
        while GPIO.input(self.echo) == 0:
            startTime = time.time()

            if startTime - timeout_start > self.timeout:
                return -1

        # store arrivalTime
        while GPIO.input(self.echo) == 1:
            arrivalTime = time.time()

            if startTime - timeout_start > self.timeout:
                return -1

        if startTime != 0 and arrivalTime != 0:
            # calculate the difference between start and stop
            duration = arrivalTime - startTime

            # multiply with speed of sound (34300 cm/s)
            # and divide by 2 because there and back
            distance = (duration * 34300) / 2

            if distance >= 0:
                return distance
            else:
                return -1
        else:
            return -1

    def speed(self):
        start_time = time.time()

        start_distance = self.distance() * 0.01     # to m conversion
        end_distance = self.distance() * 0.01       # to m conversion

        end_time = time.time()

        speed = (end_distance - start_distance) / 1.0   # m/s

        return speed