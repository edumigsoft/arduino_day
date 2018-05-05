from machine import Pin
import time

# D4    2
pin = Pin(2, Pin.OUT)

while True:
    # On in LOW
    pin.off()
    time.sleep(0.5)
    # Off in HIGH
    pin.on()
    time.sleep(0.5)
