#!/usr/bin/env python3


from picamera import PiCamera
from time import sleep
from datetime import date

camera = PiCamera()

camera.start_preview()
sleep(5)
today = date.today()

camera.resolution = (1920, 1080)
camera.capture('/home/pi/pictures/test-image-%s.jpg' % today)

camera.stop_preview()
