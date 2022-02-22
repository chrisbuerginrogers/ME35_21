import hub, utime
from Backpack_Code import Backpack

dongle = Backpack(hub.port.A, verbose = True) 
dongle.ask('\x03')

commands = '''
\x05
import sensor, image, time, os, tf

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

# Load the built-in person detection network (the network is in your OpenMV Cam's firmware).
net = tf.load('person_detection')
labels = ['unsure', 'person', 'no_person']

def check():
    while(True):
        img = sensor.snapshot()
        for obj in net.classify(img, min_scale=1.0, scale_mul=0.5, x_overlap=0.0, y_overlap=0.0):
            img.draw_rectangle(obj.rect())
            num = obj.output().index(max(obj.output()))
            label = labels[num]
            img.draw_string(obj.x()+3, obj.y()-1, label, mono_space = False)
            return num, label


\x04
'''

def configure():
    if not dongle.setup(): return False
    for cmd in commands.split('\n'):
        if not dongle.EOL(dongle.ask(cmd)) : return False
    return True
    
p = hub.port.C.motor.pair(hub.port.D.motor)
p.pwm(0,0)   # drive straight

print(configure())
while(True):
    try:
        reply = dongle.ask('check()')
        r = reply.split('\r\n')[-2]
        label = r.split(',')[1][2:-2]
        num = int(r.split(',')[0][1:])
        #print(label)
        hub.display.show(str(num))
        if num == 1:
            p.pwm(40,-40)
        else:
            p.pwm(0,0)
    except:
        pass
    utime.sleep(0.1)
