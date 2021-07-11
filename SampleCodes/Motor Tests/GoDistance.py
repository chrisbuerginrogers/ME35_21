import hub, utime

dial = hub.port.A.motor
dial.mode(2)
Kp = 1
desired = 90

while True:
    current = dial.get()[0]
    error = desired - current
    speed = Kp * error
    speed = min(speed,100)
    speed = max(speed,-100)
    dial.pwm(speed)
    print(current)
    utime.sleep(0.1) 
    
dial.pwm(0)    
