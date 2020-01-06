import RPi.GPIO as GPIO
import time

IN1 = 0
IN2 = 1
PWM = 2
STB = 3

# 3, 5, 7, 11
# 11, 13, 19, 21 
# 23, 29, 31
# 16, 22, 24, 26, 32, 

#M1 = [11, 13, 15, 19]
M1 = [3, 5, 7, 11]
M2 = [29, 31, 33, 19]
M3 = [12, 16, 18, 22]
M4 = [36, 38, 40, 22]

SPEED = 50
START = 50

# Pin Setup
def setupPin(motors):
    for motor in motors:
        for pin in motor:
            GPIO.setup(pin, GPIO.OUT)

# Move
def move(motors, second, direction):
    for motor in motors:
        GPIO.output(motor[STB], GPIO.HIGH)
        GPIO.output(motor[IN1], direction)
        GPIO.output(motor[IN2], not direction)
        # GPIO.output(motor[PWM], direction)
    time.sleep(second)

def changeStatus(motors, status):
    for motor in motors:
        GPIO.output(motor[STB], status)

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


    changeStatus([M1, M2, M3, M4], GPIO.HIGH)
    print "Forward"
    move([M1, M2, M3, M4], 2, True)
    print "Backward"
    # changeStatus([M1, M2, M3, M4], GPIO.LOW)

    move([M1, M2, M3, M4], 2, False)
    print "Stop"

    p1.stop()
    p2.stop()
    p3.stop()
    p4.stop()
finally:
    GPIO.cleanup() 
