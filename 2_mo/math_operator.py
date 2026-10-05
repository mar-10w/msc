#!/usr/bin/env python3
import rospy

def calculator():
    rospy.init_node('calculator_node', anonymous=True)
    
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero."
    else:
        result = "Invalid operator!"
        
    rospy.loginfo("Result : %s", str(result))

if __name__ == '__main__':
    try:
        calculator()
    except rospy.ROSInterruptException:
        pass