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
WHEELS = [M1, M2]

SPEED = 100
START = 50

# Pin Setup
def setupPin(motors):
    for motor in motors:
        for pin in motor:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.output(motor[STB], True)

# Move
def goMove(motors, direction):
    for motor in motors:
        GPIO.output(motor[IN1], direction)
        GPIO.output(motor[IN2], not direction)

def goSide(motors, direction):
    if direction:
        for motor in motors:
            GPIO.output(motor[IN1], direction)
            GPIO.output(motor[IN2], not direction)
    else:    
        for motor in motors:
            GPIO.output(motor[IN1], not direction)
            GPIO.output(motor[IN2], direction)

def stopMotors():
    GPIO.output(11, False)


try: 
    GPIO.setmode(GPIO.BOARD)

    # Setup Pins
    setupPin([M1, M2])

    # PWM SETUP
    p1 = GPIO.PWM(M1[PWM], SPEED)
    p1.start(START)
    p2 = GPIO.PWM(M2[PWM], SPEED)
    p2.start(START)


    print ("Forward")
    goMove(WHEELS, True)
    time.sleep(3)

    print ("Backward")
    goMove(WHEELS, False)
    
    time.sleep(3)
    goSide(WHEELS, True)

    time.sleep(3)
    goSide(WHEELS, False)

    print ("Stop")
    stopMotors()

    p1.stop()
    p2.stop()
finally:
    GPIO.cleanup() 
