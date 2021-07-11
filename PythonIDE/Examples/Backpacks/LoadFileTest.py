import hub
import utime, os
from Backpack_Code import Backpack

file = '''
import os

fred = os.listdir()
print(fred)
if 'ESPClient.py' in fred:
    print('success')
'''
file = file.replace("\'",'"')

dongle = Backpack(hub.port.F, verbose = True) 

dongle.setup()
filename = 'test.py'
dongle.load(filename,file)
reply = dongle.get(filename)
print(reply == file)
