import distance_sensor as ds
import port,time

p1 = port.PORTB

# Get distance from object of distance sensor connected to port A
for i in range(100):
    print(ds.get_distance(p1))
    time.sleep(0.1)
    
ds.clear(p1)

max_bright = 100
ds.set_pixels(p1, bytes([max_bright]*4))

(row,col) = (1,0)
ds.get_pixel(p1,row,col)
ds.set_pixel(p1,row,col,80)

for b in range(100):
    ds.set_pixels(p1, bytes([b]*4))
    time.sleep(0.1)


