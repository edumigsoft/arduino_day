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
    time.sleep(5)
    pinGreen.off()
    pinYellow.on()
    time.sleep(1)
    for i in range(5):
        pinYellow.off()
        time.sleep(0.5)
        pinYellow.on()
        time.sleep(0.5)
    pinYellow.off()
    pinRed.on()
    time.sleep(3)
    pinRed.off()
