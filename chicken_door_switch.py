#!/usr/bin/python3


import time
import RPi.GPIO as GPIO
from datetime import datetime
from pololu_drv8835_rpi import motors, MAX_SPEED

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # or try 16


def run_up(seconds, speed):

    motors.motor2.setSpeed(speed)
    time.sleep(seconds)
    motors.motor2.setSpeed(0)

def run_down(speed):

    speed = -speed # change motor direction

    while True:
        input_state = GPIO.input(21)
        motors.motor2.setSpeed(speed)
        if input_state == False:
            motors.motor2.setSpeed(0)
            break


# check the time
now = datetime.now()

if now.hour > 19:
    run_down(MAX_SPEED)

elif now.hour < 9:
    run_up(35, MAX_SPEED)
