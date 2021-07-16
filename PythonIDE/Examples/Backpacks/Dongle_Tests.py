import hub
import utime, os, ujson
from Backpack_Code import Backpack
              
dongle = Backpack(hub.port.F, verbose = True) #connect to ESP - test to make sure it is working, load needed functions
success = dongle.setup()
dongle.ask('\x03')


payload = '''
def test():
    payload = "f = open('%s','wb')\r\n"
    payload += "f.write(%s)\r\n"
    payload += "f.close()\r\n"
    print(payload)
'''
dongle.show(dongle.CtrlE_script(payload %(filename,arr)))
dongle.ask('test()')
text = '''
import os

os.listdir()
for i in range(10):
    print('test: ' + str(i))
'''
dongle.load('test.py',str(chuck))
dongle.get('test.py')
data = [ord(x) for x in payload]
print(data)

str = ''
for i in data:
    str += '\x' + '{0:2}'.format(hex(data[i])[2:])

new_str = ''
for i in fred:
    new_str = ''.join('\x{:02x}'.format(ord(x)) for x in fred)(ord(i))
print(new_str)
