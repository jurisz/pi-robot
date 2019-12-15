#!/usr/bin/env python3

from datetime import datetime

import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from picamera import PiCamera
from time import sleep

gpioPinsRight = [14, 15, 18, 23]
gpioPinsLeft = [6, 13, 19, 26]
camera = PiCamera()
camera.start_preview()
# camera.resolution = (1280x720)
camera.resolution = (1280, 720)
startTime = datetime.now().strftime("%Y-%m-%d_%H:%M")
picName = "pictures/sample-%s-%s.jpg"

# for camera to adjust
sleep(3)

# Declare an named instance of class pass a name and motor type
motorRight = RpiMotorLib.BYJMotor("MotRight", "28BYJ")
motorLeft = RpiMotorLib.BYJMotor("MotLeft", "28BYJ")


def forward(steps):
    move(steps, True, False)


def backward(steps):
    move(steps, False, True)


def left(steps):
    for i in range(steps):
        motorRight.motor_run(gpioPinsRight, .005, 1, True, False, "full")


def right(steps):
    for i in range(steps):
        motorLeft.motor_run(gpioPinsLeft, .005, 1, False, False, "full")


def move(steps, right, left):
    for i in range(steps):
        motorRight.motor_run(gpioPinsRight, .005, 1, right, False, "full")
        motorLeft.motor_run(gpioPinsLeft, .005, 1, left, False, "full")


# 512 steps = 360deg
for i in range(6):
    camera.capture(picName % (startTime, i + 1))
    forward(512)

# left(256)
# right(256)
# backward(512)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
