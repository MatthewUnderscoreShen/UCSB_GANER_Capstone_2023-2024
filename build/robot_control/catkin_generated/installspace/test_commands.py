#!/sur/bin/env python3
import rospy
import numpy as np
import time
from std_msgs.msg import String

rospy.init_node("test_drive_command")
pub_command = rospy.Publisher("/drive_command", String, queue_size=10)
num_commands = 3    # arbitrary right now
isRunning = np.zeros(num_commands, dtype=int)   # index
when_stop = np.zeros(num_commands, dtype=float) # duration
t = time.time()

def test_callback(data):
    rospy.loginfo(rospy.get_caller_id() + ": %s", data.data)

    if data.data == "test_task":
        pub_command.publish(String("test_start"))
        isRunning[0] = 1                    # starts command #0
        when_stop[0] = 2.0 + time.time()    # with duration 2.0s
        # not necessary to use duration

def main():
    # This node takes the current task and issues the necessary commands
    # consider publishing to the task topic upon completion
    rospy.Subscriber("/current_task", String, test_callback)    # topic name, msg type, callback method

    while not rospy.is_shutdown():
        t = time.time()

        if isRunning[0] and time.time() >= when_stop[0]:
            pub_command.publish(String("test_stop"))
            isRunning[0] = 0    # stops command #0
            when_stop[0] = 0

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Execution Aborted By User")