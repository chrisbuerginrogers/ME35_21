# from https://github.com/CytronTechnologies/MAKER-PI-RP2040/tree/main/Examples/MicroPython

# This code reads the analog value on GP26 and print out on serial.
# ---
# Connection: Analog In = GP26
# ---

import machine
import utime

analog = machine.ADC(26)

while True:
    print(analog.read_u16())
    utime.sleep(0.2)
   
   