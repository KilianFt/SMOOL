#!/usr/bin/env python

import kivy
kivy.require('1.0.5')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty

import rospy

from shutter.msg import Shutter


class Smool(FloatLayout):

    rospy.init_node('shutter_control', anonymous=True)
    cmd_pub = rospy.Publisher('shutter/cmd', Shutter, queue_size=10)

    cmd = Shutter()

    checkBoxModeAll = ObjectProperty(None)
    checkBoxModeSeperate = ObjectProperty(None)
    checkBoxStateOpen = ObjectProperty(None)
    checkBoxStateClose = ObjectProperty(None)

    inputHouse = ObjectProperty(None)
    inputFloor = ObjectProperty(None)
    inputRoom = ObjectProperty(None)
    inputShutter = ObjectProperty(None)


    def execute(self):
        if self.checkBoxModeAll.active:
            self.cmd.mode = 1
            print('Mode All', self.cmd.mode)
        if self.checkBoxModeSeperate.active:
            self.cmd.mode = 2
            print('Mode Seperate', self.cmd.mode)

            if self.inputHouse.text and self.inputFloor.text and self.inputRoom.text and self.inputShutter.text:
                self.cmd.house = int(self.inputHouse.text)
                self.cmd.floor = int(self.inputFloor.text)
                self.cmd.room = int(self.inputRoom.text)
                self.cmd.shutter = int(self.inputShutter.text)

                print('House: ', self.cmd.house)
                print('Floor: ', self.cmd.floor)
                print('Room: ', self.cmd.room)
                print('Shutter: ', self.cmd.shutter)

            else:
                print('Nicht alle Felder aufgefuellt')

        if self.checkBoxStateOpen.active:
            self.cmd.state = 1
            print('State Open', self.cmd.state)

        if self.checkBoxStateClose.active:
            self.cmd.state = -1
            print('State Close', self.cmd.state)

        self.cmd_pub.publish(self.cmd)

        pass




class SmoolApp(App):

    def build(self):
        return Smool()

if __name__ == '__main__':
    SmoolApp().run()
