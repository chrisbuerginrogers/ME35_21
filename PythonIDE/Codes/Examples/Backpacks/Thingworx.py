import hub
import utime, os, ujson
import passwords as p
from Backpack_Code import Backpack

Thing = 'SPIKE'
Property = 'Fred'

commands = '''
\x05
PORT = 443
base='pp-21060114127e.portal.ptc.io'
request='%s /Thingworx/Things/%s/Properties/%s HTTP/1.1\\r\\n'
request += 'Host: %s\\r\\n' % base
request += 'Content-Type: application/json\\r\\n'
request += 'Accept: application/json\\r\\n'
request += 'appKey: KEY\\r\\n'
    
def readIt(thing, property):
    req = request % ('GET',thing,property)
    req += '\\r\\n'
    code, reason, reply = ESPClient.REST(base, PORT, req, False)
    try:
        if code == 200:
            Json = reply.split("\\r\\n")[-3]
            response = ujson.loads(Json)['rows'][0]
            return code, response[property]
        else:
            return code, reason
    except:
        return (-1, reply)

def writeIt(thing, property, value):
    payload = {property: value}
    payload = ujson.dumps(payload)
    req = request % ('PUT',thing,"*")
    req += 'Content-Length: %d\\r\\n\\r\\n' % len(payload)
    req += '%s\\r\\n\\r\\n' % payload

    code, reason, reply = ESPClient.REST(base, PORT, req, False)
    try:
        if code == 200:
            return code, reply
        else:
            return code, reason
    except:
        return (-1, reply)
\x04
'''

commands = commands.replace('KEY',p.appKeys['Thingworx'])

dongle = Backpack(hub.port.F, verbose = True) 
dongle.ask('import ESPClient, ujson')
dongle.ask("ESPClient.wifi('%s','%s')"%(p.SSID,p.KEY))
dongle.ask()  # check for IP address (slow sometimes)

def configure():
    if not dongle.setup(): return False
    for cmd in commands.split('\n'):
        if not dongle.EOL(dongle.ask(cmd)) : return False
    return True

def grab():
    dongle.ask()
    reply = dongle.ask('readIt("%s","%s")' % (Thing, Property))
    try:
        return reply.split('\r\n')[-2]
    except: 
        return None
        
def set(Value):
    dongle.ask()
    reply = dongle.ask('writeIt("%s","%s","%s")' % (Thing, Property, Value))
    dongle.ask()
    try:
        return reply.split('\r\n')[1]
    except: 
        return None
       
while True:
    i = 0
    if configure():
        for j in range(100):
            s = set(i)
            g = grab()
            if s and g:
                i = i+1
                print(s,g)
                utime.sleep(1)
    dongle.ask('\x04')
    utime.sleep(1)
    dongle.ask('\x03')
    
