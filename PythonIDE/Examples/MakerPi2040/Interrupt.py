'''
from https://dmccreary.medium.com/the-cytron-maker-pi-rp2040-robotics-board-b1dc7f0eab34
    
7 Grove Ports on GPs 1:0,1; 2:2,3; 3:4,5; 4:16,17; 5:6,26; 6:26,27 and 7:7,28
4 servo connectors on ports GP12, GP13, GP14 and GP15
Piezzo buzzer on port GP22
On/Off switch on GP22, which can be used to mute the sound

https://www.coderdojotc.org/micropython/advanced-labs/02-interrupt-handlers/
'''

import machine, micropython
import time

#-------initialize things
micropython.alloc_emergency_exception_buf(100) # allows error reporting for callbacks

button1 = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)

period = 20 #msec
frequency = int(1000/period)
min = int(65536/period * 1.0)
mid = int(1.5 * period)
max = int(2.0 * period)


pwm = machine.PWM(machine.Pin(15))
pwm.freq(frequency)

photo_pin = machine.ADC(28)

done = False

#---------define two functions
def servo(angle=0):
    dutycycle = int(((max - min)/180)*angle)+min
    pwm.duty_u16(dutycycle)

def button1_pressed(change):
    global done
    print('pushed')
    time.sleep(0.1)
    done = True  #stop the loop
    button1.irq(None) #end the interrupt

#---------go
servo(0)#starting point
button1.irq(handler=button1_pressed, trigger=machine.Pin.IRQ_FALLING)  #start interrupt

while not done:
    val = photo_pin.read_u16()
    print(val)
    time.sleep(.2)
    

   