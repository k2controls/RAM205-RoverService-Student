from Rover.Rover import Rover
from Rover.LineFollower import LineFollower
from Rover.RoverDrive import DriveCommand


def test_line_follower(rover):
    test_count = 0
    lf = rover.line_follower

    print("Testing Line Follower")
    print()
    print("Calibrate line follower.")
    print()
    input("No line is under sensor and sensor are off. Press Enter to validate.")
    lf.read_state()
    if lf.state == [1,1,1,1]:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    input("Position line under far_left only. Press Enter to validate.")
    lf.read_state()
    if lf.state == [0,1,1,1]:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    input("Position line under left only. Press Enter to validate.")
    lf.read_state()
    if lf.state == [1,0,1,1]:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    input("Position line under right only. Press Enter to validate.")
    lf.read_state()
    if lf.state == [1,1,0,1]:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    input("Position line under far right only. Press Enter to validate.")
    lf.read_state()
    if lf.state == [1,1,1,0]:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    
    print("Testing line follower next_motion()")
    print("No line is under sensors, sensors are off")
    input("Next motion is STOP. Press Enter to validate.")
    if lf.next_motion()== DriveCommand.STOP:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under far_left only.")
    input("Next motion is LEFTROTATE. Press Enter to validate.")
    if lf.next_motion()== DriveCommand.LEFTROTATE:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under far_left and left.")
    input("Next motion is LEFTFORWARD. Press Enter to validate.")
    if lf.next_motion()== DriveCommand.LEFTFORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under far_left only.")
    input("Next motion is LEFTROTATE. Press Enter to validate.")
    if lf.next_motion()== DriveCommand.LEFTFORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under left and right.")
    input("Next motion is FORWARD. Press Enter to validate.")
    if lf.next_motion()== DriveCommand.FORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under right only.")
    input("Next motion is RIGHTROTATE. Press Enter to validate.")
    if lf.next_motion()== DriveCommand.RIGHTFORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under right and far_right only.")
    input("Next motion is RIGHTROTATE. Press Enter to validate.")
    if lf.next_motion()== DriveCommand.RIGHTFORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under far_right only.")
    input("Next motion is RIGHTROTATE. Press Enter to validate.")
    if lf.next_motion()== DriveCommand.RIGHTROTATE:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    return test_count
