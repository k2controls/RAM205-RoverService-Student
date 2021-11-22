''' Command Service
Fetches next command from Message Service, 
transfers message to command and updates
command list 
'''
from threading import Thread
from Bluetooth.CommandMessages import CommandMessages
from Bluetooth.Command import Command_Type, Command
from Bluetooth.Commands import Command_Type, Command_ID
from Bluetooth.CommandList import CommandList

class CommandService(Thread):

    def __init__(self, message_service):
        self.message_service = message_service
        self.command_queue = CommandList()
        Thread.__init__(self)
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            message = self.message_service.get_message()
            new = self.make_commands(message)
            self.command_queue.extend(new)
            
    def make_commands(self, message):
        new_commands = CommandList()
        if message.count("4WD") and message.count("MODE"):
            # this is a mode message
            command_id = CommandMessages.MODE_MESSAGES[message]
            command = Command(Command_Type.MODE, command_id, message=message)
            new_commands.append(command)
        elif message.count("4WD"):
            # this is an analog message
            seg = message.split(",")
            if len(seg) == 4:   #rgb analog color message
                # red first
                red = seg[1]
                value = int(red[3:])
                command = Command(Command_Type.ANALOG, Command_ID.LED_RED_ANALOG, value, message)
                new_commands.append(command)
                #green
                green = seg[2]
                value = int(green[3:])
                command = Command(Command_Type.ANALOG, Command_ID.LED_GREEN_ANALOG, value, message)
                new_commands.append(command)
                #blue
                blue = seg[3]
                value = int(blue[3:])
                command = Command(Command_Type.ANALOG, Command_ID.LED_BLUE_ANALOG, value, message)
                new_commands.append(command)               
            elif len(seg) == 2:     #analog servo message
                servo = seg[1]
                value = int(servo[3:])
                command = Command(Command_Type.ANALOG, Command_ID.SERVO_ANALOG, value, message)
                new_commands.append(command) 
            else:
                raise ValueError("Invalid message format.")
        else: # Control pad button message
            command_id = CommandMessages.BUTTON_MESSAGES[message]
            command = Command(Command_Type.CONTROL, command_id, message=message)
            new_commands.append(command)

        return new_commands

    def next_command(self) -> Command:
        return self.command_queue.next_command()
        