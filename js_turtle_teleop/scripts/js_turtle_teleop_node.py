#!/usr/bin/env python

# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-28 22:50:17
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-29 18:52:52

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class 
    def callback(data):
        twist = Twist()
        twist.linear.x = 4*data.axes[1]
        twist.angular.z = 4*data.axes[0]
        pub.publish(twist)

    def start():
        # publishing to "turtle1/cmd_vel" to control turtle1
        global pub
        pub = rospy.Publisher('turtle1/cmd_vel', Twist)
        # subscribed to joystick inputs on topic "joy"
        rospy.Subscriber("joy", Joy, callback)
        # starts the node
        rospy.init_node('Joy2Turtle')
        rospy.spin()

    if __name__ == '__main__':
        start()