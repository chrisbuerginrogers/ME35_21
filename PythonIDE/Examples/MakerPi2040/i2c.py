   
# This code scans any I2C devices connected to I2C0 at frequency 100kHz
# and print the address(es) on serial.
# ---
# Connection: I2C0, SCL0 = GP1, SDA0 = GP0
# ---
import machine

i2c0 = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=100000)
i2c0 = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
i2c0.readfrom_mem(25,0x28,6)

devices = i2c0.scan()
if devices:
    for d in devices:
        print("i2c0:")
        print(hex(d))
        
import machine
import utime

sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
conversion_factor = 3.3 / (65535)
while True:
   reading = sensor_temp.read_u16() * conversion_factor
   temperature = 27 - (reading - 0.706)/0.001721
   print(temperature)
   print('\n')
   utime.sleep(1)
   
   
