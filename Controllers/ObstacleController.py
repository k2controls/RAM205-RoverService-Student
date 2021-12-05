''' Obstacle Controller
'''
from threading import Thread
from Rover.Rover import Rover
from Rover.RGBLed import LED_COLOR
import time

class ObstacleController(Thread):
    
    def __init__(self, rover:Rover):
        self.rover = rover
        self.go = True
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while self.go:
            # This code is for demo only. Delete as required.
            # Add code created in mode_obstacle.py
            self.rover.rgb_led.set_color(LED_COLOR.RED)
            print("y", end="")
            time.sleep(1)
            self.rover.rgb_led.set_color(LED_COLOR.OFF)
            print("-", end="")
            time.sleep(1)
        
    def teardown(self):
        self.go = False