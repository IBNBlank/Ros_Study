#!/usr/bin/env python

# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-28 22:50:17
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-29 21:54:21

import rospy
from my_message.msg import chat_msg



if __name__ == '__main__':
    rospy.init_node("talker_py", anonymous=True)
    pub = rospy.Publisher("chatter", chat_msg, queue_size=10)
    rate = rospy.Rate(2)

    count = 0

    while not rospy.is_shutdown():
        msg = chat_msg()
        msg.name = rospy.get_name()
        msg.chat = "hello world {}".format(count)

        rospy.loginfo(msg.chat)
        pub.publish(msg)

        count += 1

        rate.sleep()
