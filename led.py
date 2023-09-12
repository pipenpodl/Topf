import RPi.GPIO as GPIO
from time import sleep


def led_off(number):
    if number == 1:
        GPIO.output(6, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(6, GPIO.LOW)
        sleep(0.3)
        GPIO.output(5, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(5, GPIO.LOW)
        sleep(0.3)
        GPIO.output(22, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(22, GPIO.LOW)
        sleep(0.3)
        GPIO.output(27, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(27, GPIO.LOW)
        sleep(0.3)
        GPIO.output(17, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(17, GPIO.LOW)
        sleep(0.3)
        
    elif number == 2:
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        sleep(0.5)
        
    
    elif number == 0: 
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)   
        
    sleep(0.1)