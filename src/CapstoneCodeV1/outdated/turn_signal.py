
def turn_signal(trig, echo):
    turn = False

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo)==0:
        start = time.time()

    while GPIO.input(echo)==1:
        end = time.time()

    duration = end - start

    distance = round(duration * 17150, 2)

    if(distance < 10):
        turn = True

    GPIO.cleanup()
    return turn

