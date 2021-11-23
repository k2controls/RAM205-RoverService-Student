''' RoverDrive Class
Control drive by passing in a DriveCommand to the update
method. Requires motor controller pin numbers
- added RoverPins.BOARD_MODE
11/23/21
'''
import RPi.GPIO as GPIO
from Rover.RoverPins import RoverPins
class DriveCommand:
    ''' (l_in1, l_in2, r_in1, r_in2)
    '''
    STOP =          (0, 0, 0, 0)                #(l_in1, l_in2, r_in1, r_in2)
    FORWARD =       (0, 1, 0, 1)
    BACKWARD =      (1, 0, 1, 0)
    LEFTFORWARD =   (0, 0, 0, 1)
    LEFTROTATE =    (1, 0, 0, 1)
    LEFTBACKWARD =  (1, 0, 0, 0)
    RIGHTFORWARD =  (0, 1, 0, 0)
    RIGHTROTATE =   (0, 1, 1, 0)
    RIGHTBACKWARD = (0, 0, 1, 0)
   

class RoverDrive:

    DEFAULT_SPEED = 50

    def __init__(self, 
        left_in1_pin, 
        left_in2_pin, 
        left_speed_pin,
        right_in1_pin, 
        right_in2_pin, 
        right_speed_pin):
        #storing pin detail
        self.left_in1_pin = left_in1_pin
        self.left_in2_pin = left_in2_pin
        self.left_speed_pin = left_speed_pin
        self.right_in1_pin = right_in1_pin
        self.right_in2_pin = right_in2_pin
        self.right_speed_pin = right_speed_pin

        self.speed = RoverDrive.DEFAULT_SPEED
        self.drive_command = DriveCommand.STOP

        #config GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(RoverPins.BOARD_MODE)
        GPIO.setup(self.left_in1_pin, GPIO.OUT)
        GPIO.setup(self.left_in2_pin, GPIO.OUT)
        GPIO.setup(self.left_speed_pin, GPIO.OUT)
        GPIO.setup(self.right_in1_pin, GPIO.OUT)
        GPIO.setup(self.right_in2_pin, GPIO.OUT)
        GPIO.setup(self.right_speed_pin, GPIO.OUT)
        # config PWM for speed control
        self._left_speed_pwm = GPIO.PWM(self.left_speed_pin, 50)
        self._right_speed_pwm = GPIO.PWM(self.right_speed_pin, 50)
        self._left_speed_pwm.start(self.speed)
        self._right_speed_pwm.start(self.speed)

    def __del__(self):
        GPIO.cleanup()

    def __str__(self):
        return f"The rover has a current speed of {self.speed}."

    def update(self, drive_command:DriveCommand):
        self.drive_command = drive_command
        GPIO.output(self.left_in1_pin, drive_command[0])
        GPIO.output(self.left_in2_pin, drive_command[1])
        GPIO.output(self.right_in1_pin, drive_command[2])
        GPIO.output(self.right_in2_pin, drive_command[3])

    def speed_up(self, step=10):
        new_speed = self.speed + step
        if new_speed <= 100:
            self.speed = new_speed
            self._left_speed_pwm.ChangeDutyCycle(self.speed)
            self._right_speed_pwm.ChangeDutyCycle(self.speed)

    def speed_down(self, step=10):
        new_speed = self.speed - step
        if new_speed >= 0:
            self.speed = new_speed
            self._left_speed_pwm.ChangeDutyCycle(self.speed)
            self._right_speed_pwm.ChangeDutyCycle(self.speed)
        
    # def set_speed(self, left_speed, right_speed):
    #     pass
        





