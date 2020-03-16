#!/usr/bin/env python3
# Servo2.py
# Two servo motors driven by PCA9685 chip

from smbus import SMBus
from PCA9685 import PWM
import time

fPWM = 50
i2c_address = 0x40 # (standard) adapt to your module
channel = 0 # adapt to your wiring
a = 10 # adapt to your servo
b = 5  # adapt to your servo

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

print("starting")
setup()
for direction in range(0, 181, 10):
    setDirection(direction)
direction = 0
setDirection(0)
print("done")


