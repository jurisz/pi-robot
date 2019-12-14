#!/usr/bin/env python3

import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

gpioPinsRight = [14, 15, 18, 23]
gpioPinsLeft = [6, 13, 19, 26]

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
forward(512)
left(256)
right(256)
backward(512)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()

