#!/usr/bin/env python3

import rospy
import actionlib

from action_sim.msg import MoveTurtleAction
from action_sim.msg import MoveTurtleGoal

def feedback_callback(feedback):

    print(
    "Current:",
    feedback.current_x,
    feedback.current_y,
    "Remaining:",
    feedback.distance_remaining
    )

rospy.init_node("turtle_action_client")

client = actionlib.SimpleActionClient(
    "move_turtle",
    MoveTurtleAction
)

client.wait_for_server()

goal=MoveTurtleGoal()

goal.x=8
goal.y=8

client.send_goal(
    goal,
    feedback_cb=feedback_callback
)

client.wait_for_result()

print(client.get_result())