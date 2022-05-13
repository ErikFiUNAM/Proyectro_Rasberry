#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError

from sensor_msgs.msg import Image
from std_msgs.msg import String

class Image_processing:
    def __init__(self):
        self.sub_teclado = rospy.Subscriber("color", String, self.color_callback)
        self.sub_image = rospy.Subscriber("camera_img", Image , self.image_callback)

        self.img  = []
        self.bridge = CvBridge()

        self.light_red = (0 ,150 ,70)
        self.dark_red = (19 , 255 ,255)
        self.light_green = (34 , 50 , 50)
        self.dark_green = (80 , 255 , 255)
        self.light_blue = (92 , 50 , 50)
        self.dark_blue = (124, 220, 200)
        ##Diccionario de colores que son tuplas
        self.hue_colors = {"red": (self.light_red,self.dark_red),"green":(self.light_green, self.dark_green) ,"blue" :(self.light_blue, self.dark_blue)}

    def image_callback(self,msg):
        self.img = self.bridge.imgmsg_to_cv2(msg)

    def color_callback(self,msg):
        hsv_img =cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

        light, dark = self.hue_colors[msg.data]

            ##haciendo la mascara
        mask = cv2.inRange(hsv_img, light,dark)
        result = cv2.bitwise_and(self.img, self.img, mask = mask)

if __name__=='__main__':
    try:
        rospy.init_node('image_processing_node')
        rate = rospy.Rate(10)
        img_p = Image_processing()

        rospy.spin()

    except rospy.ROSInterruptException:
        pass
