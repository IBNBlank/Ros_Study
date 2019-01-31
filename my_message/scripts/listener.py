#!/usr/bin/env python

# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-28 22:50:17
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-29 21:54:21

import rospy
from my_message.msg import chat_msg


def callback(data):
    rospy.loginfo("I heard [{0}] said '{1}'".format(data.name, data.chat))



if __name__ == '__main__':
    rospy.init_node("listener_py", anonymous=True)
    sub = rospy.Subscriber("chatter", chat_msg, callback, queue_size=10)

    rospy.spin()
