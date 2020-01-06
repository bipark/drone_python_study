import RPi.GPIO as GPIO
import time

IN1 = 0
IN2 = 1
PWM = 2
STB = 3

# 7, 11, 13
# 19, 21, 23
# 16, 22, 24 
# 23, 29, 31
# 26, 32, 

M1 = [7, 11, 13, 26]
M2 = [19, 21, 23, 26]
M3 = [16, 22, 24, 32]
M4 = [3, 5, 31, 32]

SPEED = 10
START = 10

# Pin Setup
def setupPin(motors):
    for motor in motors:
        for pin in motor:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

# Move
def move(motors, direction):
    for motor in motors:
        GPIO.output(motor[STB], True)
        GPIO.output(motor[IN1], direction)
        GPIO.output(motor[IN2], not direction)
        # GPIO.output(motor[PWM], direction)

def stopMotors():
    GPIO.output(11, False)


try: 
    GPIO.setmode(GPIO.BOARD)

    # Setup Pins
    setupPin([M1, M2, M3, M4])

    # PWM SETUP
    p1 = GPIO.PWM(M1[PWM], SPEED)
    p1.start(START)
    p2 = GPIO.PWM(M2[PWM], SPEED)
    p2.start(START)
    p3 = GPIO.PWM(M3[PWM], SPEED)
    p3.start(START)
    p4 = GPIO.PWM(M4[PWM], SPEED)
    p4.start(START)

    print "Forward"
    move([M1, M2, M3, M4], True)
    time.sleep(3)

    print "Backward"
    move([M1, M2, M3, M4], False)
    
    time.sleep(2)
    print "Stop"
    stopMotors()

    p1.stop()
    p2.stop()
    p3.stop()
    p4.stop()
finally:
    GPIO.cleanup() 
