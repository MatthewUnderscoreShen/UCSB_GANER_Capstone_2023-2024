import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_PIN = 6
GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(GPIO_PIN):
            print("No obstacle detected")
        else:
            print("Obstacle detected")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
