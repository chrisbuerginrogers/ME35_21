import hub,utime

hub.battery.info()

for i in range(100):
    (x,y,z)= hub.motion.accelerometer()
    utime.sleep(0.1)
    print(x)