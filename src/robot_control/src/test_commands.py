#!/sur/bin/env python
import rospy
from std_msgs.msg import String

def test_callback(data):
    rospy.loginfo(rospy.get_caller_id() + ":    ", data.data)

def main():
    rospy.init_node("test_drive_command")

    test_condition_name = "placeholder" # link to file?

    sub = rospy.Subscriber("current_task", String, test_callback)    # topic name, msg type, callback method
    pub = rospy.Publisher("drive_command", String, queue_size = 10)  # topic name, msg type, queue size

    while not rospy.is_shutdown():
        print("help")
        # best way to get subscriber data?
        sub_data = "placeholder"
        if sub_data == test_condition_name:
            pub.publish("test_command")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Execution Aborted By User")