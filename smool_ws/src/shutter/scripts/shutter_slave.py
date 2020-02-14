#!/usr/bin/env python

import rospy
from shutter.msg import Shutter

def cmd_callback(data):
    cmd = data


def shutter_slave():

    rospy.init_node('shutter_slave', anonymous=True)

    rospy.Subscriber("shutter/cmd", Shutter, cmd_callback)

    #cmd = Shutter()

    rospy.spin()

if __name__ == '__main__':
    shutter_slave()