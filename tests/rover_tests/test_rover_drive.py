from Rover.RoverDrive import DriveCommand

def test_rover_drive(rover):
    test_count = 0

    drive = rover.rover_drive

    print("Testing Rover Drive.")
    print()
    input("PREPARE ROVER FOR MOTION! Press enter to continue.")
    print()
    input("Rover is stopped. Press Enter to move FORWARD.")
    drive.update(DriveCommand.FORWARD)
    if input("Is drive moving FORWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(DriveCommand.STOP)
    else:
        drive.update(DriveCommand.STOP)
        return 0

    input("Rover is stopped. Press Enter to move BACKWARD.")
    drive.update(DriveCommand.BACKWARD)
    if input("Is drive moving BACKWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(DriveCommand.STOP)
    else:
        drive.update(DriveCommand.STOP)
        return 0

    input("Rover is stopped. Press Enter to move LEFTFORWARD.")
    drive.update(DriveCommand.LEFTFORWARD)
    if input("Is drive moving LEFTFORWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(DriveCommand.STOP)
    else:
        drive.update(DriveCommand.STOP)
        return 0

    input("Rover is stopped. Press Enter to move LEFTBACKWARD.")
    drive.update(DriveCommand.LEFTBACKWARD)
    if input("Is drive moving LEFTBACKWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(DriveCommand.STOP)
    else:
        drive.update(DriveCommand.STOP)
        return 0

    input("Rover is stopped. Press Enter to move LEFTROTATE.")
    drive.update(DriveCommand.LEFTROTATE)
    if input("Is drive moving LEFTROTATE? ").lower()[0]=="y":
        test_count +=1
        drive.update(DriveCommand.STOP)
    else:
        drive.update(DriveCommand.STOP)
        return 0


    input("Rover is stopped. Press Enter to move RIGHTFORWARD.")
    drive.update(DriveCommand.RIGHTFORWARD)
    if input("Is drive moving RIGHTFORWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(DriveCommand.STOP)
    else:
        drive.update(DriveCommand.STOP)
        return 0

    input("Rover is stopped. Press Enter to move RIGHTBACKWARD.")
    drive.update(DriveCommand.RIGHTBACKWARD)
    if input("Is drive moving RIGHTBACKWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(DriveCommand.STOP)
    else:
        drive.update(DriveCommand.STOP)
        return 0

    input("Rover is stopped. Press Enter to move RIGHTROTATE.")
    drive.update(DriveCommand.RIGHTROTATE)
    if input("Is drive moving RIGHTROTATE? ").lower()[0]=="y":
        test_count +=1
        drive.update(DriveCommand.STOP)
    else:
        drive.update(DriveCommand.STOP)
        return 0

    drive.update(DriveCommand.STOP)

    return test_count
