import hub,utime

motor = hub.port.A.motor
motor.mode(2)

for speed in range(200):
    for run in range(5):
        vel = []
        motor.run_to_position(0, 25)
        while motor.busy(1):
            utime.sleep(0.1)
        utime.sleep(1)
        motor.pwm(speed-100)
        for i in range(100):
            vel.append(motor.get()[0])
            utime.sleep_ms(5)
        motor.pwm(0)
        utime.sleep(1)
        print(vel)
    
motor.run_to_position(0, 25)