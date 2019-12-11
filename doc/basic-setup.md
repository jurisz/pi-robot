
## installed image
 - Used "Raspbian Buster Lite" - 435Mb
 - enabled ssh with ssh file in boot partition
 - configured wifi network with  ``sudo raspi-config``
 

##Motor

1. install pip

pi

`sudo apt-get install python3-pip`

ubuntu

`sudo apt install pip3`


2. Gipo lib

`pip3 install RPi.GPIO`

3. motor lib

`pip3 install rpimotorlib`

4. copy file and run

## Camera
1. ``sudo raspi-config`` - enable camera and reboot
2. ``pip3 install picamera``
need numpy support have to install picamera[array]

 
