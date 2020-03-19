
##### Raspberry 3B+ and servo motors setup and few tests

Used:
 - Servo motors:  MG 996R  
 - Controller with PCA9685 chip

Pi config:
 - install libs <br>
  `sudo apt-get install i2c-tools python-smbus` 
 - enable i2c <br>
   `/etc/modules`  
   add line <br>
   `i2c-dev`
   
 - add line in <br>
   `boot/config.txt` <br>
   `dtparam=i2c_arm=on`
 
 Wiring
   - 1 - VCC
   - 2 - SDA
   - 3 - SCL
   - GND - GND  
  similar to: <br>
  ![](components_raspi_pca9685_i2c_with_servo.png) 
   
 Code here `test-samples/servo/`  
 
 Overall pictures:<br>
 ![](servos-1.jpg) <br><br>
 ![](servos-2.jpg) <br>
 
Video:   
 https://www.youtube.com/watch?v=E5VS4s-R7vk
