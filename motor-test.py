import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO_RP = 11
GPIO_RN = 13
GPIO_EN = 15
GPIO_ST = 19

# GPIO_RP = 29
# GPIO_RN = 31
# GPIO_EN = 33
# GPIO_ST = 21

# GPIO_RP = 12
# GPIO_RN = 16
# GPIO_EN = 18
# GPIO_ST = 22

# GPIO_RP = 36
# GPIO_RN = 38
# GPIO_EN = 40
# GPIO_ST = 22

GPIO.setup(GPIO_RP, GPIO.OUT)
GPIO.setup(GPIO_RN, GPIO.OUT)
GPIO.setup(GPIO_EN, GPIO.OUT)
GPIO.setup(GPIO_ST, GPIO.OUT)
GPIO.output(GPIO_ST, GPIO.HIGH)

def setSpeed(speed,p):
    p.ChangeDutyCycle(speed*10)

try:
    p = GPIO.PWM(GPIO_EN, 100)
    p.start(0)
    for i in range(10):
        print(i)
        GPIO.output(GPIO_ST, True)
        GPIO.output(GPIO_RP, False)
        GPIO.output(GPIO_RN, True)
        GPIO.output(GPIO_EN, True)
        setSpeed(i, p)            
        time.sleep(1)
finally:
    GPIO.cleanup()