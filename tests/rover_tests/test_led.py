
def test_led(rover):
    test_count = 0

    print("Testing led.")
    # test red
    led = rover.rgb_led.redLED
    led.on()
    if input("Is red led on? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    led.off()
    if input("Is red led off? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    # test green
    led = rover.rgb_led.greenLED
    led.on()
    if input("Is green led on? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    led.off()
    if input("Is green led off? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    # test blue
    led = rover.rgb_led.blueLED
    led.on()
    if input("Is blue led on? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    led.off()
    if input("Is blue led off? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    # test other using red
    led = rover.rgb_led.redLED
    led.toggle()
    if input("Did red led toggle on? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    
    led.toggle()
    if input("Did red led toggle off? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0


    led.blink(.5,30)
    if input("Is red led short blinking at 2 sec period? ").lower()[0]=="y":
        test_count += 1
    else:
        return 0


    return test_count

