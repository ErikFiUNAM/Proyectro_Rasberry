#!/usr/bin/env python

import rospy
import cv2
import numpy as np

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

class Camera:
    def __init__(self):
        self.publisher = rospy.Publisher('camera_img',Image, queue_size = 10)
        self.img = cv2.VideoCapture(0)
        self.bridge = CvBridge()


    def publish_image(self):
        image = self.bridge.cv2_to_imgmsg(self.img, encoding="passtrhough")
        self.publisher.publish(image)
        print ("Se publico la imagen")


if __name__ == '__main__':
    try:
        rospy.init_node('camera_emu_node')
        rate = rospy.Rate(10)
        cam = Camera()

        while not rospy.is_shutdown():
            cam.publish_image()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
