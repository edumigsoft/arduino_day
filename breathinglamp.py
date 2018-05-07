from machine import Pin, PWM
import time, math

# D6    12  PWM
# D7    13  PWM
# D8    15

pinN1 = 12
pinN2 = 13
pinN3 = 15

pin1 = Pin(pinN1)
pinPWM1 = PWM(pin1, freq=1000)

pin2 = Pin(pinN2)
pinPWM2 = PWM(pin2, freq=1000)

pin3 = Pin(pinN3, Pin.OUT, 0)

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

#pulse(pinPWM1, 50)

#for i in range(10):
#    pulse(pinPWM1, 20)

while True:
    pulse(pinPWM1, 50)
    pulse(pinPWM2, 10)
    time.sleep(1)

    pulse(pinPWM1, 20)
    pulse(pinPWM2, 100)
    time.sleep(1)