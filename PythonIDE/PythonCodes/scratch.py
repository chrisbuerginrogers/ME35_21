import hub,utime

dial = hub.port.A.motor
dial.mode(2) # 2 is rotations and 3 is degrees
dial.float()  # so the motor does not push back

while True:
    clicks = dial.get()[0]
    print(clicks)
    utime.sleep(0.1)
    