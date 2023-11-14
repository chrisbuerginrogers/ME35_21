import device
from hub import port
import time

device.id(port.A)
pwm = device.get_duty_cycle(port.A)
device.set_duty_cycle(port.A, pwm)   # pwm 0-10,000
device.ready(port.F)  # use for startup test
device.data(port.A)   # aw LPF-2 data from a device.

device_type = {'61':'light', '62': 'dist', '63': 'force', 
    '64': 'color_matrix', '65': 'essentials motor'}

for i in range(6):
    r = device.ready(i)
    if r:
        fred = device.id(i)
        print('port %d: id %d, type: %s data ' %(i,  fred, device_type[str(fred)]), end='')
        print(device.data(i))
