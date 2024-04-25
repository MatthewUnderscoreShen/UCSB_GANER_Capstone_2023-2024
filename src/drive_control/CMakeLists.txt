cmake_minimum_required(VERSION 3.0.2)
project(drive_control)

find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    #message_generation
)

catkin_python_setup()

## Generate messages in the 'msg' folder
#add_message_files(
#    FILES
#)

## Generate added messages and services with any dependencies listed here
#generate_messages(
#    DEPENDENCIES
#    std_msgs  # Or other packages containing msgs
#)

## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
    #CATKIN_DEPENDS rospy
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS src/motor_control_test.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})