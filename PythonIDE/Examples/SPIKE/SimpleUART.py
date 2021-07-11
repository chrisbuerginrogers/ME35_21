import hub, utime

wio = hub.port.C
wio.mode(hub.port.MODE_FULL_DUPLEX)

utime.sleep(1)
wio.baud(9600)

wio.write('test\n')
