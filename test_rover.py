''' Runs a series of test on Rover model
    asking user to verify behaviors
    11/23/21
'''
from Rover.rover_factory import make_rover
from tests.test_rover import test_rover

print("This is a test of the rover unit. Components will be activated")
print("and you will be asked to verify by entering either Y or N.")
input("Press Enter to continue...")
rover = make_rover()
test_rover(rover)
print("Test complete.")
