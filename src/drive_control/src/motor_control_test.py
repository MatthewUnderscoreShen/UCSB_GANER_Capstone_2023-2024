import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import String

rospy.initnode("test_motor_control")

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

def command_callback(data):
    # Takes a command and sends signals to the motors
    rospy.loginfo(rospy.get_caller_id() + ": %s",data.data)

    if data.data == "test_start":       # Test move forward command
        pwm_left.ChangeDutyCycle(50)    # half speed
        pwm_right.ChangeDutyCycle(50)
        GPIO.output(pin_dir_left,GPIO.HIGH)     # forward for left
        GPIO.output(pin_dir_right,GPIO.LOW)     # forward for right
    elif data.data == "test_stop":      # Stop command
        pwm_left.ChangeDutyCycle(0)
        pwm_right.ChangeDutyCycle(0)

def main():
    rospy.loginfo(rospy.get_caller_id() + " now running")
    rospy.Subscriber("/drive_command", String, command_callback)

    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Execution Aborted By User")