import rospy
from ultralytics import YOLO
from std_msgs.msg import Float32MultiArray
#from skimage import io
import numpy as np
import os

rospy.init_node("camera_node")
# cam_pub = rospy.Publisher("/camera_out",)

def Detect_Object():
    model = YOLO('best.pt') 
    os.system('raspistill -o image.jpg -h 640 -w 640 -t 10 -rot 0')
    results = model(['image.jpg'])  # return a list of Results objects
    xyxy = results[0].boxes.xyxy.numpy()
    return xyxy

def main():
    

    while not rospy.is_shutdown():
        xyxy = Detect_Object()
        # publish this somehow

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        print("Execution Aborted By User")
