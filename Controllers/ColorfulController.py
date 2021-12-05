''' Colorful Controller class
'''
import time
from Rover.RGBLed import RGBLed, LED_COLOR
from threading import Thread

class ColorfulController(Thread):
    def __init__(self, rover):
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