'''
http://wiki.seeedstudio.com/Grove-Sound_Sensor/

connections: 
Ground (B) - GND 
Power  (R)   - 3V3 
NC
Signal -  pin W24
'''

from pyb import ADC
import machine

machine.Pin('EN_3V3').on()

class GroveSPL(object):
     def __init__(self, pin):
          self.adc = ADC(pin)

     def value(self):
          val = 0
          for i in range (100):
               val = val + self.adc.read()
          val = val / 100
          return val
          
import utime

sound = GroveSPL('W24')
while True:
     SPL = 0
     size = 100
     for i in range(size):
          SPL += sound.value()/40.96
     SPL /= size
     print ('%4.2f' % (SPL))
     utime.sleep_ms(200)
     




