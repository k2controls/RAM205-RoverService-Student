''' Control Pad controller
'''
from Controllers.Controller import Controller
from Bluetooth.Commands import Command_ID
from Bluetooth.Command import Command
from Rover.Rover import Rover

class ControlPadController(Controller):
    def __init__(self, rover:Rover):
        self.rover = rover

    def update(self, command:Command):
        self.last_command = command
        print(f">>>CommandID={command.command_id}, Value={command.value}")

        if command.command_id == Command_ID.BEEP:
            self.rover.buzzer.toggle()
        ### continue here
        # copy code from mode_controlpad

    def teardown(self):
        pass