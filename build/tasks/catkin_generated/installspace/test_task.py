import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy

rospy.init_node("test_task_sender")
pub_task = rospy.Publisher("/current_task", String, queue_size=10)

def joy_callback(data):     # need a joystick mapping
    rospy.loginfo(rospy.get_caller_id() + ": %s", str(data.axes))
    rospy.loginfo(rospy.get_caller_id() + ": %s", str(data.buttons))
    if data.buttons[0] == 1:
        pub_task.publish(String("test_task"))

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