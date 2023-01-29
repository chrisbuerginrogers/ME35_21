from machine import Pin
from time import sleep
from neopixel import NeoPixel

# Most people have a heart rate of around 60-70 beats per minute
# If we add a once second delay between "beats" you can make and LED
# look like a beating heart.

NUMBER_PIXELS = 2
LED_PIN = 18

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

ramp_delay = .1
beat_delay = 1
skip_interval = 10

while True:
    # ramp brightness up using the ramp_delay
    for i in range(0, 64, skip_interval):
        strip[0] = (i,0,0)   # brightness of  (R, G, B)
        strip[1] = (0,i,0)
        strip.write()
        sleep(ramp_delay)
    # ramp brightness down using the same delay
    for i in range(64, 0, -skip_interval):
        strip[0] = (0,0,i)
        strip[1] = (0,i,0)
        strip.write()
        sleep(ramp_delay)
    strip[0] = (0,0,0)
    strip.write()
    sleep(beat_delay)
    
