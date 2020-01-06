import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# 3, 5, 7, 11, 13, 19, 21, 23, 29, 31
# 16, 22, 24, 26, 32, 
Pin = 7

GPIO.setup(Pin, GPIO.OUT)
GPIO.output(Pin, True)
time.sleep(2)
GPIO.output(Pin, False)

GPIO.cleanup()