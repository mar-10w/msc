#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import atan2, sqrt, pi

leader_pose = Pose()
follower_pose = Pose()

def leader_callback(msg):
    global leader_pose
    leader_pose = msg

def follower_callback(msg):
    global follower_pose
    follower_pose = msg

def normalize_angle(angle):
    while angle > pi:
        angle -= 2 * pi
    while angle < -pi:
        angle += 2 * pi
    return angle

def follow():

    rospy.init_node('follow')

    rospy.Subscriber('/turtle1/pose', Pose, leader_callback)
    rospy.Subscriber('/turtle2/pose', Pose, follower_callback)

    pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(20)

    while not rospy.is_shutdown():

        vel = Twist()

        dx = leader_pose.x - follower_pose.x
        dy = leader_pose.y - follower_pose.y

        distance = sqrt(dx * dx + dy * dy)

        desired_theta = atan2(dy, dx)
        angle_error = normalize_angle(desired_theta - follower_pose.theta)

        # Stop when close to Turtle1
        if distance < 0.5:
            vel.linear.x = 0.0
            vel.angular.z = 0.0

        else:
            # Rotate towards Turtle1
            vel.angular.z = 4.0 * angle_error

            # Move only if facing Turtle1
            if abs(angle_error) < 0.3:
                vel.linear.x = min(2.0 * distance, 2.0)
            else:
                vel.linear.x = 0.0

        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        follow()
    except rospy.ROSInterruptException:
        pass