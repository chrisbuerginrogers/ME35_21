import hub,utime

dial = hub.port.E.motor
sonar = hub.port.A.device
dial.float()
sonar.get()[0]  # get initial reading

Kp = 50
N = 100000

start = utime.ticks_ms()
for i in range(N):
    pitch = sonar.get()[0]
    if pitch:
        hub.sound.beep(Kp * pitch,100)
        hub.sound.volume(dial.get()[1])

end = utime.ticks_ms()

print((end-start)/1000/N)
