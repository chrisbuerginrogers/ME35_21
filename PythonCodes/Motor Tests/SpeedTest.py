import hub,utime

motor = hub.port.A.motor
motor.mode(2)

for speed in range(100):
    motor.run_to_position(0, 50)
    while motor.busy(1):
        utime.sleep(0.1)
    utime.sleep(1)
    motor.pwm(speed)
    utime.sleep(1)
    motor.pwm(0)
    utime.sleep(1)
    motor.get()[0]
    
motor.run_to_position(0, 50)
