import force_sensor as fs
import port,time

p1 = port.PORTA

fs.get_touch(p1)

while True:
    print(fs.get_force(p1))
    time.sleep(0.1)
