import rospy
import RPi.GPIO as GPIO
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Joy

rospy.init_node("motor_control_test")
# drive_pub = rospy.Publisher("/drive_output", String, queue_size=10)

pin_pwm_left = 22      # 22
pin_dir_left = 10       # 10
pin_pwm_right = 17      # 17
pin_dir_right = 27      # 27
pwm_hz = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin_pwm_left,GPIO.OUT)
GPIO.setup(pin_dir_left,GPIO.OUT)
GPIO.setup(pin_pwm_right,GPIO.OUT)
GPIO.setup(pin_dir_right,GPIO.OUT)
pwm_left = GPIO.PWM(pin_pwm_left,pwm_hz)   # pin, Hz
pwm_right = GPIO.PWM(pin_pwm_right,pwm_hz)

def joy_callback(data):

    left_spd = data.axes[1]
    right_spd = data.axes[4]

    # Set motor direction
    if left_spd != 0 and left_spd/np.abs(left_spd) > 0:  # pos or neg
        GPIO.output(pin_dir_left, GPIO.HIGH)    # forward
    else:
        GPIO.output(pin_dir_left, GPIO.LOW)     # backwards
    if right_spd != 0 and right_spd/np.abs(right_spd) > 0:
        GPIO.output(pin_dir_right, GPIO.LOW)    # forward
    else:
        GPIO.output(pin_dir_right, GPIO.HIGH)   # backwards

    # Set motor power
    # Changes the input -> output profile to have less power at lower inputs
    pwm_left.ChangeDutyCycle(pwm_hz*np.abs(np.power(left_spd,5)))
    pwm_right.ChangeDutyCycle(pwm_hz*np.abs(np.power(right_spd,5)))

    # drive_pub.publish(String("Left: " + str(left_spd) + "   Right: " + str(right_spd)))

def main():
    rospy.loginfo(rospy.get_caller_id() + " now running")
    rospy.Subscriber("/joy", Joy, joy_callback)

    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        print("Execution Aborted By User")