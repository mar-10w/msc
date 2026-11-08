#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import atan2, hypot

p1, p2 = Pose(), Pose()

rospy.init_node("f")
rospy.Subscriber("/turtle1/pose", Pose, lambda m: globals().update(p1=m))
rospy.Subscriber("/turtle2/pose", Pose, lambda m: globals().update(p2=m))
pub = rospy.Publisher("/turtle2/cmd_vel", Twist, queue_size=1)
rate = rospy.Rate(10)

# Wait until both turtles broadcast valid poses (> 0)
while not rospy.is_shutdown() and (p1.x == 0 or p2.x == 0):
    rate.sleep()

while not rospy.is_shutdown():
    dx, dy = p1.x - p2.x, p1.y - p2.y
    dist = hypot(dx, dy)

    msg = Twist()
    if dist > 0.5:
        msg.linear.x = min(1.5 * dist, 2.0)
        msg.angular.z = 4.0 * (atan2(dy, dx) - p2.theta)

    pub.publish(msg)
    rate.sleep()