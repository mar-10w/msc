#!/usr/bin/env python3
import rospy

rospy.init_node("calc")
a = float(input("Num 1: "))
op = input("Op (+, -, *, /): ")
b = float(input("Num 2: "))

ops = {"+": a + b, "-": a - b, "*": a * b, "/": a / b if b else "Div by zero"}
print("Result:", ops.get(op, "Invalid Op"))