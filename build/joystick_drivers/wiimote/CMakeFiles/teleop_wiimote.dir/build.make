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

# Include any dependencies generated for this target.
include joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/depend.make

# Include the progress variables for this target.
include joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/progress.make

# Include the compile flags for this target's objects.
include joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/flags.make

joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.o: joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/flags.make
joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.o: /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/src/teleop_wiimote.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/capstone/UCSB_GANER_Capstone_2023-2024/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.o"
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.o -c /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/src/teleop_wiimote.cpp

joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.i"
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/src/teleop_wiimote.cpp > CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.i

joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.s"
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote/src/teleop_wiimote.cpp -o CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.s

# Object files for target teleop_wiimote
teleop_wiimote_OBJECTS = \
"CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.o"

# External object files for target teleop_wiimote
teleop_wiimote_EXTERNAL_OBJECTS =

/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/src/teleop_wiimote.cpp.o
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/build.make
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/libroscpp.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libpthread.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libboost_chrono.so.1.71.0
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/librosconsole.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/librosconsole_log4cxx.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/librosconsole_backend_interface.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/liblog4cxx.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libboost_regex.so.1.71.0
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/libroscpp_serialization.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/libxmlrpcpp.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/librostime.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libboost_date_time.so.1.71.0
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/libcpp_common.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.71.0
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libconsole_bridge.so.0.4
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/libroslib.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /opt/ros/noetic/lib/librospack.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libpython3.8.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libboost_filesystem.so.1.71.0
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libboost_program_options.so.1.71.0
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libboost_system.so.1.71.0
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: /usr/lib/aarch64-linux-gnu/libtinyxml2.so
/home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote: joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/capstone/UCSB_GANER_Capstone_2023-2024/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote"
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/teleop_wiimote.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/build: /home/capstone/UCSB_GANER_Capstone_2023-2024/devel/lib/wiimote/teleop_wiimote

.PHONY : joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/build

joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/clean:
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote && $(CMAKE_COMMAND) -P CMakeFiles/teleop_wiimote.dir/cmake_clean.cmake
.PHONY : joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/clean

joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/depend:
	cd /home/capstone/UCSB_GANER_Capstone_2023-2024/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/capstone/UCSB_GANER_Capstone_2023-2024/src /home/capstone/UCSB_GANER_Capstone_2023-2024/src/joystick_drivers/wiimote /home/capstone/UCSB_GANER_Capstone_2023-2024/build /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote /home/capstone/UCSB_GANER_Capstone_2023-2024/build/joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : joystick_drivers/wiimote/CMakeFiles/teleop_wiimote.dir/depend

