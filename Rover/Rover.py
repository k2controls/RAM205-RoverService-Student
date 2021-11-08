''' Rover Class
Container used to encapsulate all rover objects
'''

from Rover.Buzzer import Buzzer
from Rover.Camera import Camera
from Rover.Gimbal import Gimbal
from Rover.LineFollower import LineFollower
from Rover.RGBLed import RGBLed
from Rover.RoverDrive import RoverDrive
from Rover.Servo import Servo
from Rover.SonarPing import SonarPing
from Rover.Warner import Warner


class Rover():

    def __init__(self):
        self.buzzer:Buzzer = None 
        self.camera:Camera = None   #???
        self.gimbal:Gimbal = None
        self.line_follower:LineFollower = None
        self.rgb_led:RGBLed = None
        self.rover_drive:RoverDrive = None
        self.servo:Servo = None
        self.sonar_ping:SonarPing = None
        self.warner:Warner = None

    def __del__(self):
    
        self.buzzer = None
        self.camera = None
        self.gimbal = None
        self.line_follower = None
        self.rgb_led = None
        self.rover_drive = None
        self.servo = None
        self.sonar_ping = None
        self.warner = None
