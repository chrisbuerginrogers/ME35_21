'''
from https://dmccreary.medium.com/the-cytron-maker-pi-rp2040-robotics-board-b1dc7f0eab34
    
7 Grove Ports on GPs 1:0,1; 2:2,3; 3:4,5; 4:16,17; 5:6,26; 6:26,27 and 7:7,28
4 servo connectors on ports GP12, GP13, GP14 and GP15
Piezzo buzzer on port GP22
On/Off switch on GP22, which can be used to mute the sound

'''

import machine
import time

photo_pin = machine.ADC(28)  # port 7

while not done:
    val = photo_pin.read_u16()
    print(val)
    time.sleep(.2)
    

   