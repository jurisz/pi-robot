#!/usr/bin/env python3

# drive with relay on/off

import RPi.GPIO as GPIO
from smbus import SMBus
from PCA9685 import PWM
import time

motorPin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPin, GPIO.OUT)

fPWM = 50
i2c_address = 0x40 # (standard) adapt to your module
channel = 0 # adapt to your wiring
a = 8.6 # adapt to your servo
b = 2  # adapt to your servo

def setup():
    global pwm
    # Raspberry Pi revision 2
    bus = SMBus(1)
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.setDuty(channel, duty)
    print("direction =", direction, "-> duty =", duty)
    # allow to settle
    time.sleep(1)

def turnLeft(deg):
    setDirection(90 - deg)


def turnRight(deg):
    setDirection(90 + deg)


def drive(seconds):
    GPIO.output(motorPin, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(motorPin, GPIO.LOW)

setup()

time.sleep(1)
turnLeft(0)

drive(5)

print("turing left ")
turnLeft(12)
drive(3)


print("turing right ")
turnRight(12)
drive(3)

turnLeft(0)
drive(10)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
