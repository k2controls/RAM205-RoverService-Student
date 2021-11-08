''' Servo Class
Implements basic servo action
11/8/21
'''
import RPi.GPIO as GPIO 

class Servo():
    CCW_POSITION = 0
    CW_POSITION = 180

    def __init__(self, pin):
        self._pin = pin
        #TODO config servo pin

    def __del__(self):
        GPIO.cleanup()

    def rotate(self, position):
        #TODO implement rotate
        pass
    
