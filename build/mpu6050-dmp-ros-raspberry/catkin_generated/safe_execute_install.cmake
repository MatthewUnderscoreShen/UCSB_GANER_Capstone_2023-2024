execute_process(COMMAND "/home/capstone/UCSB_GANER_Capstone_2023-2024/build/mpu6050-dmp-ros-raspberry/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/capstone/UCSB_GANER_Capstone_2023-2024/build/mpu6050-dmp-ros-raspberry/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
