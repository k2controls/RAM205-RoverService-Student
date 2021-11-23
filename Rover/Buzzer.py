''' Buzzer class
Abstracts basic Buzzer functions. GPIO Pin is required.
PWM created on if Beep() called.
- added RoverPins.BOARD_MODE
11/23/21
'''
import RPi.GPIO as GPIO
from Rover.RoverPins import RoverPins
class Buzzer:

    def __init__(self, pin, active_low=True):
        self._pin = pin
        self._active_low = active_low
        self._on = not active_low
        self._pwm = None
        GPIO.setwarnings(False)
        GPIO.setmode(RoverPins.BOARD_MODE)
        GPIO.setup(self._pin, GPIO.OUT)
        self.off()

    def __del__(self):
        GPIO.cleanup()
        
    def off(self):
        GPIO.output(self._pin, not self._on)

    def on(self):
        GPIO.output(self._pin, self._on)

    def is_on(self):
        return GPIO.input(self._pin) == self._on

    def is_off(self):
        return GPIO.input(self._pin) != self._on

    def toggle(self):
        if self.is_on():
            self.off()
        else:
            self.on()

    def beep(self, frequency=1, duty_cycle=50):
        if frequency < 0 and frequency > 10:
            raise ValueError("Blink frequency must be between 0 and 10.")
        if duty_cycle < 0 and duty_cycle > 100:
            raise ValueError("Blink duty_cycle must be between 0 and 100.")
        if self._active_low:
            duty_cycle = 100 - duty_cycle
        if self._pwm == None:
            self._pwm = GPIO.PWM(self._pin, frequency)
            self._pwm.start(duty_cycle)
        else:
            self._pwm.ChangeFrequency(frequency)
            self._pwm.ChangeDutyCycle(duty_cycle)

    def beep_off(self):
        duty_cycle = 0
        if self._active_low:
            duty_cycle = 100 - duty_cycle
        if self._pwm:
            self._pwm.ChangeDutyCycle(duty_cycle)
