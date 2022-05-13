#!/usr/bin/en python
# coding=utf-8
import rospy
import cv2
import numpy as np
import operator
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Int16

class imagen:
    def __init__(self):
        # Se suscribe al topico de la imagen en ROS
        rospy.Subscriber("cv_camera/image_raw/compressed", CompressedImage, self.imageCallback)

    def imageCallback(self, msg):
        np_arr = np.fromstring(msg.data,np.uint8)
        self.cv2_img = cv2.imdecode(np_arr,cv2.IMREAD_COLOR)
        cv2.imshow("Imagen",self.cv2_img)
        cv2.waitKey(1)

if __name__ == '__main__':
    rospy.init_node('cam_sub_node')
    rospy.loginfo("VENTANAAAAA")
    im = imagen()
    r = rospy.Rate(10)
    try:
        rospy.spin()
        r.sleep()
    except rospy.ROSInterruptException:
        pass
