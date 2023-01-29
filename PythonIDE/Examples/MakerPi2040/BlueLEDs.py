import machine
import utime

for i in range(8):
    fred = machine.Pin(i, machine.Pin.OUT)
    fred.on()
    utime.sleep(1)
    fred.off()
    
# or much better:
#  https://www.coderdojotc.org/micropython/kits/maker-pi-rp2040/02-blue-led-lab/
  
import machine
import time

# The Maker Pi RP2040 has 13 fantastic blue GPIO status LEDs
blue_led_pins = [0,1,2,3,4,5,6,7,16,17,26,27,28]
number_leds = len(blue_led_pins)
led_ports = []

# create a list of the ports
for i in range(number_leds):
    led_ports.append(machine.Pin(blue_led_pins[i], machine.Pin.OUT))

delay = .05

# loop forever
while True:
    # blue up
    for i in range(0, number_leds):
        led_ports[i].high()
        time.sleep(delay)
        led_ports[i].low()
    # blue down
    for i in range(number_leds - 1, 0, -1):
        led_ports[i].high()
        time.sleep(delay)
        led_ports[i].low()
