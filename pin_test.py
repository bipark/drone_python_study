import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# 11, 13, 19, 21, 23, 29, 31
# 16, 22, 24, 26, 32, 
Pin = 40

GPIO.setup(Pin, GPIO.OUT)
GPIO.output(Pin, True)
time.sleep(1)

GPIO.cleanup()