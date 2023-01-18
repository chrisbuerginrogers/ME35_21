import time
from motorController import *

board = NanoMotorBoard()
print("reboot")
board.reboot()
time.sleep_ms(500)

servos = []

for i in range(4):
    servos.append(Servo(i))

#if (!PMIC.enableBoostMode()):
#    print("Error enabling Boost Mode");\

while True:
    for i in range(180):  # Servo sweep from 0 position to 180
        # Choose which of the servo connectors you want to use: servo1(default), servo2, servo3 or servo4
        for servo in servos:
            reply = servo.setAngle(i)
        print("Servos position %d" % i)
        time.sleep_ms(200)
    time.sleep_ms(200)
    for i in range(180,0,-1): # Servo sweep from 180 position to 0
        # Choose which of the servo connectors you want to use: servo1(default), servo2, servo3 or servo4
        for servo in servos:
            reply = servo.setAngle(i)
        print("Servos position: %d" % i)
        time.sleep_ms(20)

    # Keep active the communication between MKR board & MKR Motor Carrier
    # Ping the SAMD11
    board.ping()
    time.sleep_ms(50)
    