from machine import Pin
import time

# D1    5
# D2    4

pin1 = Pin(5, Pin.OUT, 0)
pin2 = Pin(4, Pin.OUT, 0)

pwm0 = 0
pwm1 = 127
pwm2 = 256
pwm3 = 512
pwm4 = 1023

while True:
    pin1.value(pwm0)
    time.sleep(0.1)
    pin2.value(pwm4)
    time.sleep(0.5)
    pin1.value(pwm1)
    time.sleep(0.1)
    pin2.value(pwm3)
    time.sleep(0.5)
    pin1.value(pwm2)
    time.sleep(0.1)
    pin2.value(pwm2)
    time.sleep(0.5)
    pin1.value(pwm3)
    time.sleep(0.1)
    pin2.value(pwm1)
    time.sleep(0.5)
    pin1.value(pwm4)
    time.sleep(0.1)
    pin2.value(pwm0)
    time.sleep(0.5)
