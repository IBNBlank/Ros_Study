#!/usr/bin/env python

# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-28 22:50:17
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-29 21:54:21

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard [{}]".format(data.data))



if __name__ == '__main__':
    rospy.init_node("listener", anonymous=True)
    sub = rospy.Subscriber("chatter", String, callback, queue_size=10)

    rospy.spin()