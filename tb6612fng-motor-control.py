import RPi.GPIO as GPIO
import time

IN1 = 0
IN2 = 1
PWM = 2

M1 = [11, 13, 15]
M2 = [29, 31, 33]
M3 = [12, 16, 18]
M4 = [22, 24, 26]

STANBY = [19, 32]

SPEED = 100
START = 50

def setupPin(motors, standby):
    # Pin Setup
    for motor in motors:
        for pin in motor:
            GPIO.setup(pin, GPIO.OUT)
    # Stanby Pin On            
    for pin in standby:
        GPIO.output(pin, GPIO.HIGH)

def forward(motors, second):
    for motor in motors:
        GPIO.output(motor[IN1], GPIO.HIGH)
        GPIO.output(motor[IN2], GPIO.LOW)
        GPIO.output(motor[PWM], GPIO.LOW)        
    time.sleep(second)

def backward(motors, second):
    for motor in motors:
        GPIO.output(motor[IN1], GPIO.LOW)
        GPIO.output(motor[IN2], GPIO.HIGH)
        GPIO.output(motor[PWM], GPIO.LOW)        
    time.sleep(second)

def stopMotors(motors, second):
    for motor in motors:
        for pin in motor:
            if (pin == PWM):
                GPIO.output(pin, GPIO.HIGH)
            else:
                GPIO.output(pin, GPIO.LOW)
    time.sleep(second)

GPIO.setmode(GPIO.BOARD)

# Setup Pins
setupPin([M1, M2, M3, M4, STANBY], STANBY)
GPIO.output(19, GPIO.HIGH)
GPIO.output(31, GPIO.HIGH)

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
forward([M1, M2, M3, M4], 3)
print "Backward"
stopMotors([M1, M2, M3, M4], 2)

backward([M1, M2, M3, M4], 3)
print "Stop"

p1.stop()
p2.stop()
p3.stop()
p4.stop()

GPIO.cleanup() 
