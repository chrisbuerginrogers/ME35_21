import hub,utime

serial = hub.port.C
serial.mode(hub.port.MODE_FULL_DUPLEX)
serial.baud(115200)

reply = b''
while True:
    reply = serial.read(1000)
    if reply:
        print(reply)
    if 'login:' in reply:
        serial.write('pi\n')
    elif 'Password:' in reply:
        serial.write('raspberry\n')
    elif 'i:~$' in reply:
        break
    utime.sleep(1)
    
serial.write('ls\n')
utime.sleep(1)
reply = serial.read(1000)

serial.write('python\n\n')
done = False
reply = b''
utime.sleep(1)
while not done:
    reply += serial.read(1000)
    done = 'more' in reply
#serial.write('import cv2\n')
serial.write('exit()\n')
serial.read(1000)