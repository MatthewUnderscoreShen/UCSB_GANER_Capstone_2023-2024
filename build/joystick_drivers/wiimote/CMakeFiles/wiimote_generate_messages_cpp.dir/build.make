# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/capstone/UCSB_GANER_Capstone_2023-2024/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/capstone/UCSB_GANER_Capstone_2023-2024/build

# Utility rule file for wiimote_generate_messages_cpp.

# Include the progress variables for this target.
include joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp.dir/progress.make

joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp: /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/IrSourceInfo.h
joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp: /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/State.h
joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp: /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/TimedSwitch.h


/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/IrSourceInfo.h: /opt/ros/noetic/lib/gencpp/gen_cpp.py
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/IrSourceInfo.h: /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg/IrSourceInfo.msg
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/IrSourceInfo.h: /opt/ros/noetic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/capstone/UCSB_GANER_Capstone_2023-2024/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating C++ code from wiimote/IrSourceInfo.msg"
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote && /home/capstone/UCSB_GANER_Capstone_2023-2024/build/catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg/IrSourceInfo.msg -Iwiimote:/home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/cmake/../msg -p wiimote -o /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote -e /opt/ros/noetic/share/gencpp/cmake/..

/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/State.h: /opt/ros/noetic/lib/gencpp/gen_cpp.py
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/State.h: /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg/State.msg
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/State.h: /opt/ros/noetic/share/geometry_msgs/msg/Vector3.msg
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/State.h: /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg/IrSourceInfo.msg
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/State.h: /opt/ros/noetic/share/std_msgs/msg/Header.msg
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/State.h: /opt/ros/noetic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/capstone/UCSB_GANER_Capstone_2023-2024/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating C++ code from wiimote/State.msg"
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote && /home/capstone/UCSB_GANER_Capstone_2023-2024/build/catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg/State.msg -Iwiimote:/home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/cmake/../msg -p wiimote -o /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote -e /opt/ros/noetic/share/gencpp/cmake/..

/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/TimedSwitch.h: /opt/ros/noetic/lib/gencpp/gen_cpp.py
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/TimedSwitch.h: /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg/TimedSwitch.msg
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/TimedSwitch.h: /opt/ros/noetic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/capstone/UCSB_GANER_Capstone_2023-2024/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating C++ code from wiimote/TimedSwitch.msg"
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote && /home/capstone/UCSB_GANER_Capstone_2023-2024/build/catkin_generated/env_cached.sh /usr/bin/python3 /opt/ros/noetic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg/TimedSwitch.msg -Iwiimote:/home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/msg -Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg -Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/cmake/../msg -p wiimote -o /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote -e /opt/ros/noetic/share/gencpp/cmake/..

wiimote_generate_messages_cpp: joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp
wiimote_generate_messages_cpp: /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/IrSourceInfo.h
wiimote_generate_messages_cpp: /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/State.h
wiimote_generate_messages_cpp: /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/include/wiimote/TimedSwitch.h
wiimote_generate_messages_cpp: joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp.dir/build.make

.PHONY : wiimote_generate_messages_cpp

# Rule to build all files generated by this target.
joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp.dir/build: wiimote_generate_messages_cpp

.PHONY : joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp.dir/build

joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp.dir/clean:
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote && $(CMAKE_COMMAND) -P CMakeFiles/wiimote_generate_messages_cpp.dir/cmake_clean.cmake
.PHONY : joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp.dir/clean

joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp.dir/depend:
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/capstone/UCSB_GANER_Capstone_2023-2024/src /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote /home/capstone/UCSB_GANER_Capstone_2023-2024/build /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : joystick_drivers/wiimote/CMakeFiles/wiimote_generate_messages_cpp.dir/depend

