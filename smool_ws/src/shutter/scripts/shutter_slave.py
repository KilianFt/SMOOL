#!/usr/bin/env python3

import rospy
from shutter.msg import Shutter
import RPi.GPIO as GPIO
from time import sleep

def activate(acLED):
	GPIO.output(acLED, True)
	sleep(5)
	GPIO.output(acLED, False)

def changeState(LED, state):
	if(state == -1):
		if(LED == 99):
			activate([15,17])
		elif(LED == 1):
			activate(15)
		elif(LED == 2):
			activate(17)
		else:
			print('Shutter ID is out of range')
		
	if(state == 1):
		if(LED == 99):
			activate([14,16])
		elif(LED == 1):
			activate(14)
		elif(LED == 2):
			activate(16)
		else:
			print('Shutter ID is out of range')
	

def cmd_callback(msg):
	#print('heard something')
	global house
	global floor
	global room

	if(msg.mode == 1):
		changeState(99, msg.state)
	if(msg.mode == 2) and (msg.house == house) and (msg.floor == floor) and (msg.room == room):
		if(msg.shutter == 99):
			changeState(99, msg.state)
		else:
			changeState(msg.shutter, msg.state)


def shutter_slave():

	rospy.init_node('shutter_slave', anonymous=True)

	GPIO.setmode(GPIO.BCM)
	myLED = [14,15,16,17]
	GPIO.setup(myLED, GPIO.OUT)

	global house
	global floor
	global room
	house = 1
	floor = 1
	room = 1

	rospy.Subscriber("shutter/cmd", Shutter, cmd_callback)

	rospy.spin()

if __name__ == '__main__':
    shutter_slave()
