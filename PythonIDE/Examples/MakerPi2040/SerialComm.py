from machine import UART, Pin

uart = UART(0,115200, timeout = 50)
#uart.init(115200, bits=8, parity=None, stop=1, tx = Pin(0), rx = Pin(1), timeout = 50)

uart.write('\x03\r\n\r\n'.encode())
uart.read()

code = '''
# blinking light on a ESP8266 connected to GROVE1 (rx -> tx and tx -> rx)
import time
from machine import Pin

led = Pin(2, Pin.OUT)

while True:
    led.on()
    time.sleep_ms(250)
    led.off()
    time.sleep_ms(250)
'''
CtrlC = '\x03'
CtrlD = '\x04'
CtrlE = '\x05'
uart.write(CtrlE.encode())
code = code.replace('\n','\r\n').encode()
print(code)
uart.write(code)
uart.write(CtrlD.encode())
print(uart.read())

uart.deinit()