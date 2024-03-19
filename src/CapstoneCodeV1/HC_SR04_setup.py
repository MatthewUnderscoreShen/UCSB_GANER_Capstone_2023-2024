import RPi.GPIO as GPIO
import time

# Define GPIO pins
trigPin = 5
echoPin = 6

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

# Function to measure distance
def measure_distance():
    # Ensure the trigger pin is low initially
    GPIO.output(trigPin, False)
    time.sleep(0.2)  # Wait 200ms to settle

    # Trigger the sensor by sending a 10us pulse
    GPIO.output(trigPin, True)
    time.sleep(0.00001)  # 10us pulse
    GPIO.output(trigPin, False)

    start_time = time.time()

    # Wait for echo to start
    while GPIO.input(echoPin) == 0:
        start_time = time.time()

    # Wait for echo to end
    while GPIO.input(echoPin) == 1:
        end_time = time.time()

    # Calculate pulse duration
    pulse_duration = end_time - start_time

    # Calculate distance in centimeters and inches
    distance_cm = pulse_duration * 17000  # uS / 58 = centimeters
    distance_in = pulse_duration * 6665.4  # uS / 148 = inches

    return round(distance_cm, 2), round(distance_in, 2)

# Main loop to print distance
try:
    while True:
        distance_cm, distance_in = measure_distance()
        print(f"Distance: {distance_cm} cm / {distance_in} inches")
        time.sleep(0.06)  # 60ms measurement cycle
except KeyboardInterrupt:
    print("Measurement stopped by User")
finally:
    GPIO.cleanup()  # Clean up GPIO
