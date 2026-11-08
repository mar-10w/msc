#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    print("Heard:", msg.data)

rospy.init_node("listener")
rospy.Subscriber("chatter", String, callback)
rospy.spin()