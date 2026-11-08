#!/usr/bin/env python3

import rospy
from nura.srv import AddTwoInts

def client():

    rospy.init_node('addition_client')

    rospy.wait_for_service('add_two_numbers') 

    try:

        add = rospy.ServiceProxy(
            'add_two_numbers',
            AddTwoInts
        ) 

        a = int(input("Enter First Number : "))
        b = int(input("Enter Second Number : "))

        response = add(a, b)

        print("Result =", response.sum)

    except rospy.ServiceException as e:
        print("Service Failed:", e)

if __name__ == '__main__':
    client()