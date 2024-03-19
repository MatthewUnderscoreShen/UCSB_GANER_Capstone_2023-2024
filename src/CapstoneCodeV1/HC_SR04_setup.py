import RPi.GPIO as GPIO
import time

# Define the GPIO pins
trigPin = 5
echoPin = 6

# Setup the GPIO pins
GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbering
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

# Function to measure distance
def measure_distance():
    # Ensure the trigger pin is set low initially
    GPIO.output(trigPin, False)
    time.sleep(0.000002) # 2 microseconds delay

    # Generate a 10 microseconds pulse on the trigger pin
    GPIO.output(trigPin, True)
    time.sleep(0.00001) # 10 microseconds delay
    GPIO.output(trigPin, False)

    # Measure the duration of the pulse coming back to the echo pin
    while GPIO.input(echoPin) == 0:
        pulse_start = time.time()
    while GPIO.input(echoPin) == 1:
        pulse_end = time.time()

    # Calculate the duration and distanceÅÅÅ
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150 # Speed of sound at sea level is ~34300 cm/s, so 34300 / 2 = 17150
    distance = round(distance, 2)

    return distance

# Main loop to print distance
try:
    while True:
        distance = measure_distance()
        print("Distance:", distance, "cm")
        time.sleep(0.1) # 100 milliseconds delay
except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup() # Clean up GPIO on CTRL+C exit
