''' Sonar Ping Senor
Service that continually pings and 
provides a distance value as a property
11/8/21
'''

class SonarPing():

    def __init__(self, trigger_pin, pulse_pin):
        self._trigger_pin = trigger_pin
        self._pulse_pin = pulse_pin
        self.distance = -1
        #TODO implement sonar ping
        
