#!/usr/bin/python

# Imports
from biobot_ros_msgs.msg import IntList
import pigpio
import rospy
from std_msgs.msg import String

class SafetyTips():
    """Check if there a tips that were not thrown in the trash"""

    def __init__(self):

        rospy.init_node('SafetyTips', anonymous=True)

        # Set GPIO 
        self.pin = 4

        self.pin_kill = [23, 18] # Kill enable pin for tool ps and pm
        self.gpio = pigpio.pi()
        self.gpio.set_mode(self.pin, pigpio.INPUT)

        self.cb_sw_tips = self.gpio.callback(self.pin,            \
                                             pigpio.FALLING_EDGE, \
                                             self.callback_sw_tips)
        

    def callback_sw_tips(self, gpio, level, tick):
       for pin in self.pin_kill:
           self.gpio.write(pin, pigpio.LOW)




# Main function
if __name__ == '__main__':
    try:
        st = SafetyTips()
        rospy.spin()
    except rospy.ROSInterruptException as e:
        print(e)


