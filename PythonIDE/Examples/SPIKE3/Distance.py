import distance_sensor as ds
from hub import port
import time

p1 = port.C

# Get distance from object of distance sensor connected to port A
for i in range(10):
    print(ds.distance(p1))
    time.sleep(0.1)
    
# messing around with the lights on the distance sensor

ds.clear(p1)

max_bright = 100
ds.show(p1, [max_bright]*4)

row,col = 1,0  # 2 rows, 2 cols
ds.get_pixel(p1,row,col)
ds.set_pixel(p1,row,col,80)

for b in range(100):
    ds.show(p1, [b]*4)
    time.sleep(0.1)


