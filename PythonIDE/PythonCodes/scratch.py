import hub,utime

dial = hub.port.A.motor
dial.mode(2) # if no motor is attached you will get an error
dial.float()  # so the motor does not push back

while True:
    clicks = dial.get()[0]
    print(clicks)
    utime.sleep(0.1)
    

            