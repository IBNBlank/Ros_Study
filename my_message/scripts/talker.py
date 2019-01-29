#!/usr/bin/env python

# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-28 22:50:17
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-29 21:54:21

import rospy
from std_msgs.msg import String



if __name__ == '__main__':
    rospy.init_node("talker", anonymous=True)
    pub = rospy.Publisher("chatter", String, queue_size=10)
    rate = rospy.Rate(2)

    count = 0

    while not rospy.is_shutdown():
        msg_str = "hello world {}".format(count)

        rospy.loginfo(msg_str)
        pub.publish(msg_str)

        count += 1

        rate.sleep()
