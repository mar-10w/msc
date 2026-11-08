#!/usr/bin/env python3
import rospy, math
from sensor_msgs.msg import JointState

L1, L2 = 0.30, 0.30

def callback(msg):
    # Direct index mapping: [0]=theta1, [1]=theta2, [2]=d3
    t1, t2, d3 = msg.position[0], msg.position[1], msg.position[2]

    # Forward Kinematics (SCARA / 2R + Prismatic)
    x = L1 * math.cos(t1) + L2 * math.cos(t1 + t2)
    y = L1 * math.sin(t1) + L2 * math.sin(t1 + t2)
    z = -d3

    print(f"X: {x:.2f} m | Y: {y:.2f} m | Z: {z:.2f} m")

rospy.init_node("fk")
rospy.Subscriber("/joint_states", JointState, callback)
rospy.spin()