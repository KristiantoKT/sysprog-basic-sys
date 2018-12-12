import RPi.GPIO as GPIO
import time

# Ultrasonic PIN = 31, 33 as represent below
GPIO_TRIGGER = 31
GPIO_ECHO = 33

# LED PIN = 35
GPIO_LED = 35

# Servo PIN = 37
GPIO_SERVO = 37

GPIO.setmode(GPIO.BOARD)

# Set PIN Servo as output 
GPIO.setup(GPIO_SERVO, GPIO.OUT)

# Set PIN Ultrasonic as ouput on trigger, input on Echo
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Set PIN LED as output
GPIO.setup(GPIO_LED, GPIO.OUT)

# Set PWM for servo motor at PIN and 50Hz
pwm = GPIO.PWM(GPIO_SERVO, 50)

# Function to move ServoMotor to open valve of dispenser
def moveServoOpenValve():
    pwm.start(5)
    pwm.ChangeDutyCycle(7.5)
    time.sleep(0.5)

# Function to move ServoMotor to close valve of dispenser
def moveServoCloseValve():
    pwm.ChangeDutyCycle(10)
    time.sleep(0.5)

# Function to get How Deep the remaining food in dispenser
def getFoodDeep():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance

# Loop of all checker
while True:
    # Count remaining food On The Plate
    remainFoodOnPlate = getBerat
    
    # Check remaining food on plate if almost empty do filling
    if remainFoodOnPlate < sekianGram :        
        # Fill the food on plate
        moveServoOpenValve()

        # get the remaining after filling
        remainFoodOnPlate = getBerat
        # check if the food is not full yet
        while remainFoodOnPlate < sekianGram :
            remainFoodOnPlate = getBerat
        
        # Close valve after food full
        moveServoCloseValve()
    # Count remaining food in Dispenser
    remainingDispenserFood = getFoodDeep()
    
    # Check remaining food in dispenser if almost empty do filling 
    if remainingDispenserFood < 15 :
        # Sent notifications
        GPIO.output(GPIO_LED, GPIO.HIGH)
    # Jika remaining food in dispenser is full of the notification
    else :
        GPIO.output(GPIO_LED, GPIO.LOW)

    