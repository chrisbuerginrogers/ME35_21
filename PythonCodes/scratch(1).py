import hub,utime

motor = hub.port.A.motor
motor.mode(2)
Kp = 1
desired = 90

for j in range(5):
    vel = []
    for i in range(500):
        angle = motor.get()[0]
        speed = Kp*(desired - angle)
        speed = max(-100,min(100,speed))
        motor.pwm(speed)
        vel.append(angle)
        utime.sleep_ms(1)
    motor.pwm(0)  
    motor.run_to_position(0, 25)
    print(vel)
    utime.sleep(1)
