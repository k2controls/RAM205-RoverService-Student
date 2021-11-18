''' Message Service Mock
Simulates message service with messages created from sample list.
No user interaction on smartphone is required.s
'''
import time
class MessageService():
    def __init__(self, messages=None, message_delay=.5):
        if messages:    
            self.messages = messages
        else:
            self.messages = list()
        self.message_delay = message_delay

    def set_message(self, message):
        self.messages.append(message)

    def get_message(self):
        while not self.messages:
            time.sleep(self.message_delay)
        return self.messages.pop(0)


