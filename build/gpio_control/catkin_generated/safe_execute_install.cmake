execute_process(COMMAND "/home/ubuntu/UCSB_GANER_Capstone_2023-2024/build/gpio_control/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ubuntu/UCSB_GANER_Capstone_2023-2024/build/gpio_control/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
