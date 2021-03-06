#!/usr/bin/python3

# from: http://razzpisampler.oreilly.com/ch07.html

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # or try 16

while True:
    input_state = GPIO.input(21)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
