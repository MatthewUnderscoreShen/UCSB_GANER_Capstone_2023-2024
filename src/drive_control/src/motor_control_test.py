import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import String
import time

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

t = 0
tStart = 0
timer = False   # is a timer running?

def command_callback(data):
    rospy.loginfo(" received: %s",data.data)

    if data.data == "test_start":
        pwm_left.ChangeDutyCycle(50)    # half speed
        pwm_right.ChangeDutyCycle(50)
        GPIO.output()

def main():
    rospy.initnode("test_motor_control")
    

    rospy.Subscriber("drive_command", String, command_callback)
    t = time.time()
    tStart
    
    # todo: normalize pwm input

    while not rospy.is_shutdown():
        t = time.time()
        if cur_comm == "test_signal":
            pwm_left.ChangeDutyCycle()