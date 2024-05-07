#!/sur/bin/env python3
import rospy
import numpy as np
import time
from std_msgs.msg import String

def main():
    rospy.init_node("test_commands")
    name = str(rospy.get_param("/pins"))
    pub = rospy.Publisher("HELP", String, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(name)
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Execution Aborted By User")