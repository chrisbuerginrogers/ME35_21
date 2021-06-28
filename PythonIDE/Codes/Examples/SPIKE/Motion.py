'''
Motion is an object that controls the movement sensors.
'''

import hub,utime

hub.motion.accelerometer()

hub.motion.gyroscope()

hub.motion.position()

hub.motion.orientation()  # has a callback option

def beep():
     hub.sound.volume(10)
     hub.sound.beep(2000, 500, 3)

hub.motion.gesture()  # is it currently active?


'''
possible gestures:

leftside
rightside
down
up
front
back
tapped
doubletapped
shake
freefall
'''