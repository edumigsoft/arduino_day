from machine import Pin
import time

# D6    12
# D7    13
# D8    15

pinN1 = 12
pinN2 = 13
pinN3 = 15

pinGreen = Pin(pinN1, Pin.OUT, 0)
pinYellow = Pin(pinN2, Pin.OUT, 0)
pinRed = Pin(pinN3, Pin.OUT, 0)

while True:
    pinGreen.on()
    time.sleep(5)
    pinGreen.off()
    pinYellow.on()
    time.sleep(1)
    pinYellow.off()
    pinRed.on()
    time.sleep(3)
    pinRed.off()
