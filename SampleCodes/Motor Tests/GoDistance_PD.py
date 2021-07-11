import hub, utime

dial = hub.port.A.motor
dial.mode(2)
Kp = 10
Kd = -1
desired = 90
old = desired - dial.get()[0]

while True:
    current = dial.get()[0]
    error = desired - current
    speed = Kp * error + Kd * (error - old)
    speed = min(speed,100)
    speed = max(speed,-100)
    dial.pwm(int(speed))
    print(current)
    old = error
    utime.sleep(0.1)
    
    
dial.pwm(0)