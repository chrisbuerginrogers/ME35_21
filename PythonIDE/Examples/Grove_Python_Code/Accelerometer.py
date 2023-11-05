'''
https://github.com/Seeed-Studio/Accelerometer_MMA7660/blob/master/MMA7660.cpp

connections: 
Ground (B) - GND 
Power  (R)   - 3V3
SCLK - pin Y9
SDATA -  pin Y10
'''
import machine,utime

machine.Pin('EN_3V3').on()


i2c = machine.I2C(2)
i2c.scan()

i2c.writeto_mem(83,7,b'\x00')

i2c.writeto_mem(83,8,b'\x02')

i2c.writeto_mem(83,7,b'\x01')

while True:
     print(i2c.readfrom_mem(83,0,7))
     utime.sleep(1)













