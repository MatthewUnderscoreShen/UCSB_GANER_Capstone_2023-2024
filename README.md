This repo contains codes that are used to control the Gaucho Navy Auto Robot(GNAR), which competes in the robot rodeo competition held by Fathomwerx Lab. The main objective is for the GNAR
to navigate through a course consisting of staircases, latches, and narrow paths, whether using joystick control or autonomously. The final goal of this competition is for the robot to be 
fully adapted to a navy ship environment, so it would be capable of accomplishing difficult/dangerous/time-consuming jobs for the Navies. 

All Packages that are imported:
- **For ROS**
  - `Distro: ROS Noetic`
    - rospy, rospack
- **For GPIO Control:**
  - `import RPi.GPIO as GPIO`
  - `import pigpio`
- **For Controller Integration:**
  - `sudo apt-get install libspnav-dev`
  - `sudo apt-get install libbluetooth-dev`
  - `sudo apt-get install libcwiid1 libcwiid-dev`
- **For Arm Control:**
  - `import xarm`
- **For Camera Integration:**
  - `sudo apt install libraspberrypi-bin libraspberrypi-dev`
  - `Raspistill -o test.jpg`
    - Note: steps above is using for setup camera
    - if camera still does not work on current robot, add following code in the end of the file `/boot/firmware/config.txt`
      - ​​`start_x=1`
      - `gpu_mem=128`
  - `from ultralytics import YOLO`
  - `from skimage import io`
- **For General Purpose:**
  - `import math`
  - `import time`
  - `import numpy`
    
    
