import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the trigger and echo
TRIG = 5
ECHO = 6

# Initialize the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Function to measure distance
def measure_distance():
    # Ensure the trigger pin is low for a clean start
    GPIO.output(TRIG, False)
    time.sleep(0.5)  # Short delay to let sensor settle

    # Trigger the ultrasonic pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure the duration of echo pulse
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Calculate distance
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

print("Distance Measurement In Progress")

try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")
        # Short delay between measurements
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
