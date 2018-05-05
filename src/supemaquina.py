from machine import Pin
import time

# D1    5
# D2    4
# D6    12

pinGreen = Pin(5, Pin.OUT, 0)
pinYellow = Pin(4, Pin.OUT, 0)
pinRed = Pin(12, Pin.OUT, 0)

while True:
    pinGreen.on()
    time.sleep(1)
    pinGreen.off()
    pinYellow.on()
    time.sleep(1)
    pinYellow.off()
    pinRed.on()
    time.sleep(1)
    pinRed.off()
    time.sleep(0.5)
    pinRed.on()
    time.sleep(1)
    pinRed.off()
    pinYellow.on()
    time.sleep(1)
    pinYellow.off()
    pinGreen.on()
    time.sleep(1)
    pinGreen.off()
    time.sleep(0.5)