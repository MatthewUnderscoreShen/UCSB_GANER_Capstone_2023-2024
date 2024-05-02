#!/usr/bin/env python3
import rospy
import numpy as np
from drive_control.motor import Motor
from std_msgs.msg import String
from sensor_msgs.msg import Joy

class MotorController(object):

    def __init__(self):
        self.left_motor = Motor(22, 10, 100, True)
        self.right_motor = Motor(17, 27, 100, False)

        self.drive_pub = rospy.Publisher("/drive_output", String)
        self.drive_sub = rospy.Subscriber("/drive_command", String, self.drive_callback, (self))
        self.joy_sub = rospy.Subscriber("/joy", Joy, self.joy_callback, (self))

        self.is_teleop = False
    
    def drive_callback(data, args):
        if data.data == "teleop_on":
            args[0].is_teleop = True
        elif data.data == "autonomous_on":
            args[0].is_teleop = False
    
    def joy_callback(data, args):
        if not is_teleop:
            return
        
        args[0].left_motor.set_vel(data.axes[1])
        args[0].right_motor.set_vel(data.axes[4])

        args[0].drive_pub.publish(String("Left: " + str(data.axes[1]) + "   Right: " + str(data.axes[4])))

if __name__ == "__main__":
    rospy.init_node("motor_control")

    motor_controller = MotorController()

    rospy.loginfo("Motor controller node started")
    rospy.spin()