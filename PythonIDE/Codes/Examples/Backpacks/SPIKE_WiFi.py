import hub
import utime, os, ujson
import passwords as p
from Backpack_Code import Backpack

Thing = 'SPIKE'
Property = 'Fred'

commands = '''
import ESPClient
ESPClient.wifi('%s','%s')
PORT = 443
base='pp-21060114127e.portal.ptc.io'
request='GET /Thingworx/Things/%s/Properties/%s HTTP/1.1\r\n'
request += 'Host: pp-21060114127e.portal.ptc.io\r\n'
request += 'Content-Type: application/json\r\n'
request += 'Accept: application/json\r\n'
request += 'appKey: %s\r\n\r\n'
'''
commands = commands.replace('\r\n','\\r\\n')
commands = commands % (p.SSID,p.KEY,Thing,Property,p.appKeys['Thingworx'])

dongle = Backpack(hub.port.F, verbose = True) 

def configure():
    if not dongle.setup(): return False
    for cmd in commands.split('\n'):
        if '>>>' not in dongle.ask(cmd) : return False
    return True

def grab():
    reply = dongle.ask('ESPClient.REST(base, PORT, request, True)')
    if '200' in reply:
        Json = reply.split('\r\n')[-2].split('\\r\\n')[1]
        response = ujson.loads(Json)['rows'][0]
        return(response['Fred'])
    else:
        return reply

if configure():
    print(grab())
