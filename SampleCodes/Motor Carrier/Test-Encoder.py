# 2 min in on video on https://edu-content-preview.arduino.cc/content-preview/university/project/CONTENTPREVIEW+AEKR2

import time
from motorController import *

board = NanoMotorBoard()
print("reboot")
board.reboot()
time.sleep_ms(500)

motors = []

# at 50 it works as expected, at 60 shift sides and is too small duty to move, at 70 is very big duty.
for i in range(2):
    motors.append(DCMotor(i))

# Reset the encoder internal counter to zero (can be set to any initial value)
for motor in motors:  # initialize
    b = motor.setDuty(0)
    b = motor.resetEncoder(0)

for i in range(100):
    i=0
    for motor in motors:
        print("Encoder%d Pos [counts]: %d" % (i, motor.readEncoder()))
        print(" Encoder%d vel [counts/sec]: %d" % (i, motor.getCountPerSecond()))
        i += 1
    #Keep active the communication between Nano & Motor Carrier
    board.ping()
    time.sleep_ms(50)
