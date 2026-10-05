cmake_minimum_required(VERSION 3.0.2)
project(action_sim)

find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib
  actionlib_msgs
  geometry_msgs
  turtlesim
  message_generation
)

################################################
## Declare ROS messages, services and actions ##
################################################

add_action_files(
  DIRECTORY action
  FILES
  MoveTurtle.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
)

###################################
## catkin specific configuration ##
###################################

catkin_package(
  CATKIN_DEPENDS
    rospy
    actionlib
    actionlib_msgs
    geometry_msgs
    turtlesim
    message_runtime
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

catkin_install_python(
  PROGRAMS
    scripts/turtle_action_server.py
    scripts/turtle_action_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)