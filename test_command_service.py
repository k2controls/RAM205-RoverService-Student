''' Test command service using test messages
    No smartphone app input required.
11/23/21
'''
    
from tests.test_messages import bluetooth_test_messages
from Bluetooth.MessageServiceMock import MessageService
from Bluetooth.CommandService import CommandService
import time

print("Test Command Service using bluetooth test messages")
print("Sample messages are converted to command objects in a background thread.")
ms = MessageService(bluetooth_test_messages)
commands = list()

cs = CommandService(ms)
while True:
    next_command = cs.next_command()
    if next_command :
        print(f"{next_command.command_type}\t{next_command.command_id}\t\t{next_command.value}\t{next_command.message}")
    time.sleep(.5)