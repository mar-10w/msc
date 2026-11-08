# msc
cheat


# ROS Laboratory Experiments
## Workspace Setup, Package Configuration and Execution Notes

> **Document note:** This file contains ROS 1 laboratory commands, workspace preparation steps,
> package creation instructions, node execution commands, and development notes.
> Comments are included for organization and documentation.

---

<!-- ============================================================
     EXPERIMENT 1
     BASIC TALKER AND LISTENER
     ============================================================ -->

# Experiment 1 — Talker and Listener

## Workspace Initialization

```bash
# Workspace preparation
mkdir expe1
cd expe1

# Create source directory
mkdir src

# Initialize catkin workspace
catkin_make

# Load workspace environment
source devel/setup.bash
```

## Package Creation

```bash
cd src

# Create ROS package
catkin_create_pkg talkandclient std_msgs rospy roscpp
```

## Talker Node

```bash
cd talkandclient

# Create script directory
mkdir scripts
cd scripts

# Create publisher node
gedit talker.py

# Set executable permission
chmod +x talker.py

# Return to workspace
cd ~/expe1

# Build package
catkin_make
```

## Runtime Terminals

### Terminal 1 — ROS Master

```bash
roscore
```

### Terminal 2 — Talker

```bash
source devel/setup.bash
rosrun talkandclient talker.py
```

### Terminal 3 — Listener Development

```bash
cd ~/expe1/src/talkandclient
cd scripts

# Create subscriber node
gedit listener.py

# Set executable permission
chmod +x listener.py

# Rebuild workspace
cd ~/expe1
catkin_make
```

### Terminal 4 — Listener

```bash
cd ~/expe1
source devel/setup.bash
rosrun talkandclient listener.py
```

<!-- ============================================================
 EXPERIMENT 3
     STARTING WITH TURTLEISM
     ============================================================ -->
### Terminal 1 – Start ROS Master
```bash

 roscore 
``` 
### Terminal 2 – Start Turtlesim
```bash
 rosrun turtlesim turtlesim_node 
``` 
### Terminal 3 – Keyboard Control
```bash
     rosrun turtlesim turtle_teleop_key
```
### terminal 4 6. Publish Velocity Commands
```bash
     
     rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
```

<!-- ============================================================
     EXPERIMENT 4
     TURTLESIM FOLLOW
     ============================================================ -->

# Experiment 4 — Turtlesim Follow

## Workspace Setup

```bash
# Create workspace
mkdir tsim
cd tsim

# Create source directory
mkdir src

# Initialize catkin workspace
catkin_make

# Load environment
source devel/setup.bash
```

## Package Configuration

```bash
cd src

# Create turtlesim package
catkin_create_pkg spawn rospy geometry_msg turtlesim
```

## Follow Node

```bash
cd ~/tsim/src/spawn

# Create scripts directory
mkdir scripts
cd scripts

# Create follow node
gedit follow.py

# Set executable permission
chmod +x follow.py

# Build workspace
cd ~/tsim
catkin_make
```

## Runtime

### Terminal 1 — ROS Master

```bash
roscore
```

### Terminal 2 — Turtlesim

```bash
rosrun turtlesim turtlesim_node
```

### Terminal 3 — Spawn Second Turtle

```bash
rosservice call /spawn 5 5 0 turtle2
```

### Terminal 4 — Teleoperation

```bash
rosrun turtlesim turtle_teleop_key
```

### Terminal 5 — Follow Node

```bash
source devel/setup.bash
rosrun spawn follow.py
```

---


<!-- ============================================================
     EXPERIMENT 6
     SERVICE SERVER AND CLIENT
     ============================================================ -->

# Experiment 6 — ROS Service

## Workspace Initialization

```bash
# Create service workspace
mkdir exp2
cd exp2

# Create source directory
mkdir src

# Initialize workspace
catkin_make

# Load environment
source devel/setup.bash
```

## Package Creation

```bash
cd src

# Create service package
catkin_create_pkg nura rospy std_msgs message_generation
```

## Package Structure

```bash
cd nura

# Create Python scripts directory
mkdir scripts

# Create service definition directory
mkdir srv
```

## Service Server

```bash
cd scripts

# Create server program
gedit server.py
```

## Service Definition

```bash
cd ..
cd srv

# Create service interface
gedit AddTwoInts.srv
```

## Package Configuration

```bash
cd ..

# Edit package configuration
gedit package.xml
```

## Executable Permissions

```bash
cd scripts

chmod +x server.py
chmod +x client.py
```

## Build

```bash
cd ~/exp2
catkin_make
```

## Runtime Terminals

### Terminal 1 — ROS Master

```bash
roscore
```

### Terminal 2 — Service Server

```bash
cd exp2
source devel/setup.bash
rosrun nura server.py
```

### Terminal 3 — Service Client

```bash
cd exp2
source devel/setup.bash
rosrun nura client.py
```

---

<!-- ============================================================
     EXPERIMENT 7
     ACTION SERVER AND CLIENT
     ============================================================ -->

# Experiment 7 — ROS Action Server and Client

## Workspace Initialization

```bash
# Create action workspace
mkdir exp
cd exp

# Create source directory
mkdir src

# Initialize catkin workspace
catkin_make

# Load environment
source devel/setup.bash
```

## Package Creation

```bash
cd src

# Create action package
catkin_create_pkg action_sim rospy actionlib actionlib_msgs geometry_msgs turtle_sim
```

## Package Directories

```bash
cd action_sim

# Create Python node directory
mkdir scripts

# Create custom action directory
mkdir action
```

## Action Server

```bash
cd scripts

# Create action server
gedit turtle_action_server.py

# Create action client
gedit turtle_action_client.py
```

## Action Definition

```bash
cd ..
cd action

# Create action interface
gedit MoveTurtle.action
```

## Build Configuration

```bash
cd ..

# Configure package build system
gedit CMakeLists.txt
```

## Executable Permissions

```bash
cd scripts

chmod +x turtle_action_server.py
chmod +x turtle_action_client.py
```

## Build Workspace

```bash
cd ~/exp
catkin_make
```

## Runtime Terminals

### Terminal 1 — ROS Master

```bash
roscore
```

### Terminal 2 — Turtlesim

```bash
cd exp
rosrun turtlesim turtlesim_node
```

### Terminal 3 — Action Server

```bash
source devel/setup.bash
rosrun action_sim turtle_action_server.py
```

Expected output:

```text
Action Server Started
```

### Terminal 4 — Action Client

```bash
cd exp
source devel/setup.bash
rosrun action_sim turtle_action_client.py
```

---

# General ROS Notes

## Workspace Environment

ROS packages should be built from their corresponding catkin workspace. After compilation,
the generated `devel/setup.bash` file can be sourced to make packages available to ROS.

## Executable Python Nodes

Python ROS nodes launched through `rosrun` generally need executable permissions:

```bash
chmod +x filename.py
```

## Build Verification

After creating or modifying package files, rebuild the workspace when required:

```bash
catkin_make
```

## Runtime Order

A typical ROS experiment uses the following order:

1. Start `roscore`.
2. Start required simulation or supporting nodes.
3. Source the appropriate workspace.
4. Start the custom ROS nodes.
5. Observe the published topics, services, or actions.

---

# End of Laboratory Notes

### Terminal 1 — ROS Master

```bash
roscore
```

### Terminal 2 — Talker

```bash
source /opt/ros/noetic/setup.bash
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```

### Terminal 3 — Listener Development

```bash
source /opt/ros/noetic/setup.bash
rosrun echo /exp name 

```


