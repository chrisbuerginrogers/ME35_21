import hub
import utime, os, ujson
import passwords as p

Thing = 'SPIKE'
Property = 'Fred'

dongle = Backpack(hub.port.F, verbose = True) #connect to ESP - test to make sure it is working, load needed functions
success = dongle.setup()
dongle.ask('\x03')
dongle.ask('import ESPClient')
dongle.ask('ESPClient.wifi("%s","%s")'%(p.SSID,p.KEY))
dongle.ask('PORT = 443')
dongle.ask('Thing = "%s"' % Thing)
dongle.ask('Property = "%s"' % Property)
dongle.ask('appKey = "%s"' %(p.appKey))
dongle.ask("base='pp-21060114127e.portal.ptc.io'")
dongle.ask('''request='GET /Thingworx/Things/%s/Properties/%s HTTP/1.1\\r\\n'
request += 'Host: pp-21060114127e.portal.ptc.io\\r\\n'
request += 'Content-Type: application/json\\r\\n'
request += 'Accept: application/json\\r\\n'
request += 'appKey: %s\\r\\n\\r\\n\'''')
dongle.ask('request = request % (Thing,Property,appKey)')
reply = dongle.ask('ESPClient.REST(base, PORT, request, True)')
Json = reply.split('\r\n')[-2].split('\\r\\n')[1]
response = ujson.loads(Json)['rows'][0]
response['Fred']