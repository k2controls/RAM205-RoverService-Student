''' LED class
Provides basic LED functions. A GPIO pin is required.
PWM used to support dimming and blinking
- added RoverPins.BOARD_MODE
11/23/21
'''
import RPi.GPIO as GPIO
from Rover.RoverPins import RoverPins
class LED:
       
    def __init__(self, pin, active_low=False):
        self._pin = pin
        self._active_low = active_low
        if self._active_low:
            self.DC_ON = 0
            self.DC_OFF = 100
        else:
            self.DC_ON = 100
            self.DC_OFF = 0
        self.is_on = False
        GPIO.setwarnings(False)
        GPIO.setmode(RoverPins.BOARD_MODE)
        GPIO.setup(self._pin, GPIO.OUT)
        self._pwm = GPIO.PWM(self._pin, 50)
        self._pwm.start(self.DC_OFF)
    
    def on(self):
        self._pwm.ChangeDutyCycle(self.DC_ON)
        self.is_on = True

    def off(self):
        self._pwm.ChangeDutyCycle(self.DC_OFF)
        self.is_on = False

    def update(self, state):
        if state:
            self.on()
        else:
            self.off()

    def toggle(self):
        self.update(not self.is_on)

    def blink(self, frequency=.5, duty_cycle=50):
        self.is_on = bool(duty_cycle)
        if self._active_low:
            duty_cycle = 100 - duty_cycle
        self._pwm.ChangeFrequency(frequency)
        self._pwm.ChangeDutyCycle(100-duty_cycle)
        
    def dim(self, brightness):
        self.is_on = bool(brightness)
        if brightness < 0 or brightness > 100:
            raise ValueError("Invalid brightness. Must be 0 to 100.")
        if self._active_low:
            brightness = 100 - brightness
        self._pwm.ChangeFrequency(50)
        self._pwm.ChangeDutyCycle(100-brightness)
        


