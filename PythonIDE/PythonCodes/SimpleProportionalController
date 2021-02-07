import hub,utime

drive = hub.port.A.motor
sonar = hub.port.F.device
drive.pwm(0)   # stop the motor
sonar.get()[0]

Kp = 10
N = 10000

start = utime.ticks_ms()
for i in range(N):
    dist = sonar.get()[0]
    utime.sleep_ms(1)
    if dist:
        speed =  Kp * (10-dist)
        speed = 1023 if speed > 1023 else speed
        speed = -1023 if speed < -1023 else speed
        drive.pwm(speed)
    
end = utime.ticks_ms()
drive.pwm(0)  
print((end-start)/1000/N)