import hub, utime

sonic = hub.port.C.device

start=utime.ticks_ms()
for i in range(1000):
    fred = sonic.get()
(utime.ticks_ms() - start) /1000


 p = hub.port.A.motor.pair(hub.port.B.motor)