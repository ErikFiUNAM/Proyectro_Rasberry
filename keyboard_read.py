#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class Keyboard_read:
    def __init__(self):
        self.publisher = rospy.Publisher("/color", String , queue_size = 1)

    def publish_color(self):
        color = raw_input()
        self.publisher.publish(color)

if __name__ == '__main__':
    try:
        rospy.init_node('keyboard_read_node')
        rate = rospy.Rate(10)
        kb = Keyboard_read()

        while rospy.is_shutdown:
            kb.publish_color()
            rate.sleep

    except rospy.ROSInterruptException:
        pass
