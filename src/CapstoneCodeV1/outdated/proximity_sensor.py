import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_PIN = 6
GPIO.setup(GPIO_PIN, GPIO.IN)

try:
    while True:
        input_value = GPIO.input(6)
        if input_value == 0:
            print("No obstacle detected")
        else:
            print("Obstacle detected")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
