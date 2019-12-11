#!/usr/bin/env python3

import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GpioPins = [14, 15, 18, 23]

# Declare an named instance of class pass a name and motor type
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

# call the function pass the parameters
#512 steps = 360deg
mymotortest.motor_run(GpioPins, .01, 512, False, False, "full")

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
