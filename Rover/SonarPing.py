''' Sonar Ping Senor
Service that continually pings and 
provides a distance value as a property
11/8/21
'''
import RPi.GPIO as GPIO
import time
class SonarPing():

    def __init__(self, gpio_mode, trigger_pin, pulse_pin):
        GPIO.setmode(gpio_mode)
        self._trigger_pin = trigger_pin
        self._pulse_pin = pulse_pin
        self.distance = -1
        #TODO implement sonar ping
        
