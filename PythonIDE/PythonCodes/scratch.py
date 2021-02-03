import hub,utime

wheel = hub.port.A.motor

while True:
    angle = wheel.get()[1]
    print(angle)
    utime.sleep(1)