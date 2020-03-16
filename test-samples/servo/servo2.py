#!/usr/bin/env python3
# Servo2.py
# Two servo motors driven by PCA9685 chip

from smbus import SMBus
from PCA9685 import PWM
import time

fPWM = 50
i2c_address = 0x40 # (standard) adapt to your module
#channel = 0 # adapt to your wiring
a = 8.6 # adapt to your servo
b = 2  # adapt to your servo

def setup():
    global pwm
    # Raspberry Pi revision 2
    bus = SMBus(1)
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

def setDirection(channel, direction):
    duty = a / 180 * direction + b
    pwm.setDuty(channel, duty)
    print("direction =", direction, "-> duty =", duty)
    # allow to settle
    time.sleep(1)

print("starting")
setup()
#for direction in range(0, 181, 10):
#    setDirection(direction)

print("--cycle--")


for direction in range(0, 181, 10):
    setDirection(1, direction)
    setDirection(2, 180 - direction)

for direction in range(75, 106, 5):
    setDirection(0, direction)


#setDirection(1, 0)
#setDirection(2, 45)

# setDirection(92)
# time.sleep(3)
#
# setDirection(97)
# time.sleep(3)
#
# setDirection(87)
# time.sleep(3)


#direction = 0
#setDirection(0)
print("done")


