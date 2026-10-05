#!/usr/bin/env python3

import rospy
from nura.srv import AddTwoInts, AddTwoIntsResponse

def add_numbers(req):

    result = req.a + req.b

    rospy.loginfo("Number1 = %d", req.a)
    rospy.loginfo("Number2 = %d", req.b)
    rospy.loginfo("Sum = %d", result)

    return AddTwoIntsResponse(result)

def service_server():

    rospy.init_node('addition_server')

    service = rospy.Service(
        'add_two_numbers',
        AddTwoInts,
        add_numbers
    )

    rospy.loginfo("Addition Service Started")

    rospy.spin()

if __name__ == '__main__':
    service_server()