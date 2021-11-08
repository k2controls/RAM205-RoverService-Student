''' Line Follower class
Senses line follower inputs and
determines next motion required.
11/8/21
'''
import RPi.GPIO as GPIO
from Rover.RoverDrive import DriveCommand

class LineFollower:

    def __init__(self, far_left_pin, left_pin, right_pin, far_right_pin):
        self.far_left_pin = far_left_pin
        self.left_pin = left_pin
        self.right_pin = right_pin
        self.far_right_pin = far_right_pin
        self.state = [0,0,0,0]  #[far_left. left, right, far_right]
        #config GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.far_left_pin, GPIO.IN)
        GPIO.setup(self.left_pin, GPIO.IN)
        GPIO.setup(self.right_pin,GPIO.IN)
        GPIO.setup(self.far_right_pin, GPIO.IN)
        self.read_state()

    def __str__(self):
        return str(self.state)

    def read_state(self):
        self.state[0] = GPIO.input(self.far_left_pin)
        self.state[1] = GPIO.input(self.left_pin)
        self.state[2] = GPIO.input(self.right_pin)
        self.state[3] = GPIO.input(self.far_right_pin)
        
    def next_drive_command(self):
        ret_value = DriveCommand.STOP
        if self.state == [0,0,1,1]:
            ret_value = DriveCommand.LEFTFORWARD
        elif self.state == [0,1,1,1]:
            ret_value = DriveCommand.LEFTROTATE
        elif self.state == [1,0,1,1]:
            ret_value = DriveCommand.LEFTFORWARD
        elif self.state == [1,0,0,1]:
            ret_value = DriveCommand.FORWARD
        elif self.state == [1,1,0,0]:
            ret_value = DriveCommand.RIGHTFORWARD
        elif self.state == [1,1,0,1]:
            ret_value = DriveCommand.RIGHTFORWARD
        elif self.state == [1,1,1,0]:
            ret_value - DriveCommand.RIGHTROTATE

        return ret_value    

