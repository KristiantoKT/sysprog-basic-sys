import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# GPIO PIN SETUP
GPIO_SONAR_TRIGGER = 3
GPIO_SONAR_ECHO = 5
GPIO_SERVO_CONTROL = 15
GPIO_WEIGHT_DT = 29
GPIO_WEIGHT_SDK = 31
GPIO_LED_SERVO = 37
GPIO_LED_SONAR = 23

# GPIO I/O SETUP
GPIO.setup(GPIO_SONAR_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_SONAR_ECHO, GPIO.IN)
GPIO.setup(GPIO_SERVO_CONTROL, GPIO.OUT)
GPIO.setup(GPIO_WEIGHT_DT, GPIO.OUT)
GPIO.setup(GPIO_WEIGHT_SDK, GPIO.OUT)
GPIO.setup(GPIO_LED_SERVO, GPIO.OUT)
GPIO.setup(GPIO_LED_SONAR, GPIO.OUT)

def distance():
    GPIO.output(GPIO_SONAR_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_SONAR_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_SONAR_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_SONAR_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == "__main__":
    try:
        while True:
            dist = distance()
            if dist >= 15.0:
                # TODO
            else:
                # TODO
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
