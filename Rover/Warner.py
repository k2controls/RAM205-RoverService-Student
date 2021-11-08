''' Warner Class
Encapsulates a light and buzzer to
create a warning system
11/8/21
'''
from Rover import LED
from Rover import Buzzer
import time

class Warner():

    def __init__(self, led, buzzer):
        self.led = led
        self.buzzer = buzzer

    def on(self):
        self.led.on()
        self.buzzer.on()
    
    def off(self):
        self.led.off()
        self.buzzer.off()

    def alarm_on(self, frequency, duty_cycle):
        self.led.blink(frequency, duty_cycle)
        self.buzzer.beep(frequency, duty_cycle)
    
    def alarm_off(self):
        self.led.off()
        self.buzzer.beep_off()


