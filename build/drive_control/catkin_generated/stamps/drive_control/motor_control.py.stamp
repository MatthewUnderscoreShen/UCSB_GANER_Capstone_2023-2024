import rospy
import RPi.GPIO as GPIO
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Joy

# Intialize publisher
rospy.init_node("motor_control_test")
drive_pub = rospy.Publisher("/drive_output", String, queue_size=10)

# GPIO constants and setup
pin_pwm_left = 17
pin_dir_left = 27
pin_pwm_right = 22
pin_dir_right = 10

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin_pwm_left,GPIO.OUT)
GPIO.setup(pin_dir_left,GPIO.OUT)
GPIO.setup(pin_pwm_right,GPIO.OUT)
GPIO.setup(pin_dir_right,GPIO.OUT)
pwm_left = GPIO.PWM(pin_pwm_left,100)   # pin, Hz
pwm_right = GPIO.PWM(pin_pwm_right,100)

# Other constants
is_teleop = False
left_spd = 0
right_spd = 0

def command_callback(data):
    global is_teleop
    # Takes a command and sends signals to the motors
    rospy.loginfo(rospy.get_caller_id() + ": %s", data.data)
    #drive_pub.publish(String("Driving"))

    if data.data == "teleop_on":
        is_teleop = True
    elif data.data == "autonomous_on":
        is_teleop = False

    return
    if data.data == "test_start":       # Test move forward command
        pwm_left.ChangeDutyCycle(50)    # half speed
        pwm_right.ChangeDutyCycle(50)
        GPIO.output(pin_dir_left,GPIO.HIGH)     # forward for left
        GPIO.output(pin_dir_right,GPIO.LOW)     # forward for right
    elif data.data == "test_stop":      # Stop command
        pwm_left.ChangeDutyCycle(0)
        pwm_right.ChangeDutyCycle(0)

# 
# Drive method is currently tank drive (left joy -> left tread, etc)
def joy_callback(data):
    # This method only needs to be run in teleop
    if not is_teleop:
        return

    left_spd = data.axes[1]
    right_spd = data.axes[4]

    # Set motor direction
    if left_spd/np.abs(left_spd) >= 0:  # pos or neg
        GPIO.output(pin_dir_left, GPIO.HIGH)    # forward
    else:
        GPIO.output(pin_dir_left, GPIO.LOW)     # backwards
    if right_spd/np.abs(right_spd) >= 0:
        GPIO.output(pin_dir_right, GPIO.LOW)    # forward
    else:
        GPIO.output(pin_dir_right, GPIO.HIGH)   # backwards

    # Set motor power
    # Changes the input -> output profile to have less power at lower inputs
    pwm_left.ChangeDutyCycle(np.abs(np.power(left_spd,3)))
    pwm_right.ChangeDutyCycle(np.abs(np.power(right_spd,3)))

    drive_pub.publish(String("Left: " + str(left_spd) + "   Right: " + str(right_spd)))

def main():
    rospy.loginfo(rospy.get_caller_id() + " now running")
    rospy.Subscriber("/drive_command", String, command_callback)
    rospy.Subscriber("/joy", Joy, joy_callback)

    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        print("Execution Aborted By User")