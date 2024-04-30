import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Joy

rospy.init_node("test_task_sender")
pub_task = rospy.Publisher("/current_task", String, queue_size=10)
btn_2_msg = ["0","1","2","3","4","5","6","7","Autonomous","Teleop","10","11","12","None"]

# Publishes message corresponding to the button pressed
def joy_callback(data):
    rospy.loginfo(rospy.get_caller_id() + ": %s", str(data.axes))
    rospy.loginfo(rospy.get_caller_id() + ": %s", str(data.buttons))

    # Note: If more than one button is pressed at the exact same time, only registers one
    # so please don't hold the buttons down
    pub_task.publish(String(btn_2_msg[find_pressed(data.buttons)]))

# Function that finds which button is pressed
def find_pressed(axes):
    for i in range(len(axes)):
        if axes[i] > 0.0:
            return i
    return 13   # 13th task is no task

def main():
    # Joystick input corresponds to an order of tasks.
    # This node needs to monitor task completion status
    rospy.Subscriber("/joy", Joy, joy_callback)

    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Execution Aborted By User")