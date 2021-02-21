import hub,utime

left = hub.port.C.motor
right = hub.port.D.motor
left.mode(3)
right.mode(3)

for speed in range(200):
    L = left.get()[0]
    R = right.get()[0]
    print('(%d,%d)'%(-R,180-L))
    utime.sleep_ms(50)

