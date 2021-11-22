''' Test command service using smartphone app
    buzzer only
    ** Smartphone app input required.**
'''
import time    
from Bluetooth.MessageService import MessageService
from Bluetooth.CommandService import CommandService
from Bluetooth.Commands import Command_Type, Command_ID
from Rover.rover_factory import make_rover

ms = MessageService()
cs = CommandService(ms)
rover = make_rover()
while True:
    next_command = cs.next_command()
    if next_command :
        if next_command.command_id == Command_ID.BEEP:
            rover.buzzer.toggle()
        print(f"{next_command.command_type}\t{next_command.command_id}\t\t{next_command.value}\t{next_command.message}")
    time.sleep(.5)
