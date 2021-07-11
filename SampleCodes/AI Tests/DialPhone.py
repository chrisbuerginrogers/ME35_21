import hub, utime

dial = hub.port.A.motor
force = hub.port.F.device
dial.mode(2)
dial.float()

data = []

for counter in range(10):
    hub.display.show(str(counter))
    while not force.get()[1]:
        utime.sleep(.1)
    angle = dial.get()[0]
    while force.get()[1]:
        utime.sleep(.1)
    data.append((counter,angle))
