#!/usr/bin/env python3

import rospy
import math

from sensor_msgs.msg import JointState


rospy.init_node("inverse_kinematics_node")

pub = rospy.Publisher("/joint_states", JointState, queue_size=10)

rate = rospy.Rate(10)

L1 = 1.0
L2 = 1.0


while not rospy.is_shutdown():

    try:

        x = float(input("\nEnter X : "))
        y = float(input("Enter Y : "))

        d = (x*x + y*y - L1*L1 - L2*L2)/(2*L1*L2)

        if d > 1 or d < -1:
            print("\nPoint is outside workspace\n")
            continue

        theta2 = math.acos(d)

        theta1 = math.atan2(y,x) - math.atan2(L2*math.sin(theta2),
                                              L1 + L2*math.cos(theta2))

        print("\nInverse Kinematics Solution")
        print("---------------------------")

        print("Theta1 = %.2f deg"%(math.degrees(theta1)))
        print("Theta2 = %.2f deg"%(math.degrees(theta2)))

        msg = JointState()

        msg.header.stamp = rospy.Time.now()

        msg.name = ["joint1","joint2"]

        msg.position = [theta1,theta2]

        for i in range(20):

            msg.header.stamp = rospy.Time.now()

            pub.publish(msg)

            rate.sleep()

    except KeyboardInterrupt:
        break

    except:
        print("\nInvalid Input\n")