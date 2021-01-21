#!/usr/bin/env python3

"""
BSD 3-Clause License
Copyright (c) 2020, Yuya Takeuchi & Ryuichi Ueda.
All rights reserved.
"""

import subprocess
import rospy
from std_msgs.msg import Int32

def cb(message):
    if message.data == 1:
        rospy.loginfo('アホになる')
    elif message.data == 2:
        rospy.loginfo('何もなし')

if __name__ == '__main__':
    rospy.init_node('suuzi')
    sub = rospy.Subscriber('count',Int32, cb)
    rospy.spin()
