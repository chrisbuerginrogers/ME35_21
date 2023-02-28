import time
from machine import Pin, PWM

# Construct PWM object, with LED on Pin(25).
S0 = PWM(Pin(0))

# Set the PWM frequency.
S0.freq(50) # 20ms
# duty_u16 max 65535
S0.duty_u16(0)

for x in range(3):
    print("time: ", x+1)
    for i in range(0,6553,10):  
        S0.duty_u16(i)
        time.sleep(0.01)
    
    for i in range(6553,0,-10):
        S0.duty_u16(i)
        time.sleep(0.01)
print("PWM down")
S0.duty_u16(0)
