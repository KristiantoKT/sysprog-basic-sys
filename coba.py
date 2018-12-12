import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BOARD)
GPIO_LED_1 = 10
GPIO_LED_2 = 11
GPIO.setup(GPIO_LED_1, GPIO.OUT)
GPIO.setup(GPIO_LED_2, GPIO.OUT)

def led1():
    while True:
        GPIO.output(GPIO_LED_1, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GPIO_LED_1, GPIO.LOW)
        time.sleep(1)

def led2():
    while True:
        GPIO.output(GPIO_LED_2, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(GPIO_LED_2, GPIO.LOW)
        time.sleep(3)

threading.Thread(target=led1).start()
threading.Thread(target=led2).start()

"""
def loop1_10():
    for i in range(1,11):
        time.sleep(3)
        print(i)

def loop2_10():
    for i in range(65,75):
        time.sleep(1)
        print(chr(i))

threading.Thread(target=loop1_10).start()
threading.Thread(target=loop2_10).start()
"""