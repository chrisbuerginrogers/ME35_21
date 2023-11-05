'''
https://github.com/Seeed-Studio/Accelerometer_MMA7660/blob/master/MMA7660.cpp

connections: 
Ground (B) - GND 
Power  (R)   - 3V3
SCLK - pin Y9
SDATA -  pin Y10
'''

def read(reply):
     EARTH_GRAVITY_MS2   = 9.80665
     SCALE_MULTIPLIER    = 0.004

     x = reply[0] | (reply[1] << 8)
     if(x & (1 << 16 - 1)):
          x = x - (1<<16)
          
     y = reply[2] | (reply[3] << 8)
     if(y & (1 << 16 - 1)):
          y = y - (1<<16)
     
     z = reply[4] | (reply[5] << 8)
     if(z & (1 << 16 - 1)):
          z = z - (1<<16)
     
     x = x * SCALE_MULTIPLIER
     y = y * SCALE_MULTIPLIER
     z = z * SCALE_MULTIPLIER
     
     return x,y,z
     
import machine,utime

machine.Pin('EN_3V3').on()

i2c = machine.I2C(2)
i2c.scan()

i2c.writeto_mem(83,0x2C,b'\x0B')  # set Bandwidth
value = ord(i2c.readfrom_mem(83,0x31,1))
value &= ~0x0F
value |= 0x00  # range_flag
value |= 0x08
i2c.writeto_mem(83,0x31,chr(value))
i2c.writeto_mem(83,0x2D,b'\x08')  # start measuring

while True:
     reply = i2c.readfrom_mem(83,0x32,6)
     print('%f %f %f' % (read(reply)))
     utime.sleep(1)



