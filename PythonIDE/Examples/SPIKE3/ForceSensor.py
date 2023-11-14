import force_sensor as fs
from hub import port
import time

p1 = port.B

fs.pressed(p1)
print(fs.raw(port.B))

while True:
    print(fs.force(p1))
    time.sleep(0.1)
