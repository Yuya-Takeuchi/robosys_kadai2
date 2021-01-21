#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('kotae')
pub = rospy.Publisher('count', Int32, queue_size=1)
while not rospy.is_shutdown():
                 print('数字を入力してください')
                 i = int(input())
                 if i % 3 == 0 or '3' in str(i):
                    pub.publish(1)
                 else:
                    pub.publish(2)
