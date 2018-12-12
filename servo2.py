import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 50)
p.start(5)
try:
    for _ in range(1):
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
    GPIO.cleanup()

except KeyboardInterrupt:
    print("Measurement stopped by User")
    p.stop()
    GPIO.cleanup()
     
