''' Colorful Controller class
'''
from threading import Thread
from Rover.Rover import Rover
from Rover.RGBLed import LED_COLOR
import time

class ColorfulController(Thread):
    def __init__(self, rover:Rover):
        self.rover = rover
        self.go = True
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):

        while self.go:
            # this code is for demo only. Delete as required
            # Add code created in mode_colorful.py
            self.rover.rgb_led.set_color(LED_COLOR.WHITE)
            print("x", end="")
            time.sleep(1)
            self.rover.rgb_led.set_color(LED_COLOR.OFF)
            print("-", end="")
            time.sleep(1)

    def teardown(self):
        self.go = False