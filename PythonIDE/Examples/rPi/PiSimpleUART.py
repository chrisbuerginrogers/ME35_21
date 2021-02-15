import serial
ser = serial.Serial('/dev/serial0',9600)
avail = ser.in_waiting
print(avail)
ser.write(b'test')
ser.read(avail)
