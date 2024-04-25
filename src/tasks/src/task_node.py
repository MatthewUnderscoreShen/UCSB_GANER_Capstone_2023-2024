import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Joy

rospy.init_node("test_task_sender")
pub_task = rospy.Publisher("/current_task", String, queue_size=10)
btn_2_msg = [""]
axes_last = np.zeros(8, dtype=float)
buttons_last = np.zeros(13, dtype=int)

def joy_callback(data):     # need a joystick mapping
    rospy.loginfo(rospy.get_caller_id() + ": %s", str(data.axes))
    rospy.loginfo(rospy.get_caller_id() + ": %s", str(data.buttons))

    # Publishes message corresponding to the button pressed
    # Note: If more than one button is pressed at the exact same time, only registers one
    pub_task.publish(String(btn_2_msg[np.where((data.buttons-buttons_last) == 1)[0][0]]))

    # Records last publish instance to take out unintended repeat pressed if a button is held
    global axes_last
    global buttons_last
    axes_last = data.axes
    buttons_last = data.buttons

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