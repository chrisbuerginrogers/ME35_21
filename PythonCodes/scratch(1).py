import hub, utime

dial = hub.port.A.motor
dial.mode(2)

while True:
    dial.get()[0]
    utime.sleep(0.1)
    