''' Command List
Provides a queue of bluetooth commands
Required for multiple presses and RGB message
that creates three command objects.
11/23/21
'''
from collections import UserList
from Bluetooth.Command import Command

class CommandList(UserList):

    def __init__(self):
        UserList.__init__(self)
        self._commands = []

    def append(self, command:Command):
        self._commands.append(command)
        return self._commands

    def next_command(self) -> Command: 
        if self._commands:
            return self._commands.pop(0)
        else:
            return None

    def extend(self, command_list:UserList):
        self._commands.extend(command_list._commands)

    def __len__(self):
        return len(self._commands)

    def __repr__(self):
        return f"Queue({self._commands})"