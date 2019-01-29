#!/usr/bin/env python

# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-28 22:50:17
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-29 22:14:20

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


class Teleop(object):
    def __init__(self):
        self.__pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
        self.__sub = rospy.Subscriber("joy", Joy, self.callback, queue_size=10)
        self.__max_lin_speed = rospy.get_param('~max_angular_speed', 2.0)
        self.__max_ang_speed = rospy.get_param('~max_linear_speed', 2.0)
        self.__lin_speed = 0
        self.__ang_speed = 0
        self.__lin_axis = rospy.get_param('~linear_axis_num', 1)
        self.__ang_axis = rospy.get_param('~angular_axis_num', 3)

    def pub_twist(self):
        twist = Twist()
        twist.linear.x = self.__lin_speed
        twist.angular.z = self.__ang_speed
        self.__pub.publish(twist)

    def callback(self, data):
        self.__lin_speed = data.axes[self.__lin_axis] * self.__max_lin_speed
        self.__ang_speed = data.axes[self.__ang_axis] * self.__max_ang_speed
        rospy.loginfo("Turtle speed change: linear:{0:.3f} angular:{1:.3f}".format(self.__lin_speed, self.__ang_speed))



if __name__ == '__main__':
    rospy.init_node('js_turtle_teleop_node', anonymous=True)
    teleop = Teleop()
    rate = rospy.Rate(50)

    while not rospy.is_shutdown():
        teleop.pub_twist()
        rate.sleep()
