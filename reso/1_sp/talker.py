#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node("talker")
pub = rospy.Publisher("chatter", String, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    pub.publish("hello world")
    print("hello world")
    rate.sleep()