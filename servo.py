import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm = GPIO.PWM(11, 50)

a = 0 #initial position of a is 5
pwm.start(a)
try:
    while True:
        #a is rotation speed
        a += 0.1
        if a>25:
            a = 0
        pwm.ChangeDutyCycle(a)
        time.sleep(0.01)
        
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
