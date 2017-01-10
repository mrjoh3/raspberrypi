#!/usr/bin/python3


import time
from datetime import datetime
from pololu_drv8835_rpi import motors, MAX_SPEED

def run_motor(direction, seconds, speed):

    if direction == 'reverse':
        speed = -speed

    motors.motor2.setSpeed(speed)
    time.sleep(seconds)
    motors.motor2.setSpeed(0)


# check the time
now = datetime.now()

if now.hour > 19:
    direction = 'reverse'
elif now.hour < 8:
    direction = 'forward'

run_motor(direction, 35, MAX_SPEED)
