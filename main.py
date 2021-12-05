''' Main for RAM205_RoverService
This is the entry point for the final RAM205_RoverService
Uses RoverService to manage Rover Modes
No student code required to respond to mode commands and switch
modes. Students are required to implement specific mode features. See 
Controllers folder.
Keith E. Kelly
12/5/21
'''

import time
from Bluetooth.MessageService import MessageService
from Bluetooth.CommandService import CommandService
from Rover.rover_factory import make_rover
from RoverService import RoverService
from Bluetooth.Commands import Command_ID

def main():

    message_service = MessageService()
    cs = CommandService(message_service)
    rover = make_rover()
    rover_service = RoverService(cs,rover)
    #press LED OFF twice to exit
    while True:
        if rover_service.last_command == rover_service.command == Command_ID.LED_OFF:
            break
        time.sleep(.5)

if __name__ == "__main__":
    main()