''' Verifies smartphone app connection and displays
    raw Bluetooth messages
'''
from Bluetooth.MessageService import MessageService

print("Testing Message Service - a smartphone connect is required!")
print("Press any control on the Yahboom smartphone app to see assocated message.")
print("Press LED OFF button to exit.")
ms = MessageService()
message = ""
while message != "0,0,0,0,0,0,1,0,0": #LED OFF button 
    message = ms.get_message()
    print(message)
print()
