import serial
import sys
import glob
import time

ser = None

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    return ports

def InitSerial(port, bps = 9600, to = 0):
    global ser
    ser = serial.Serial(port, bps, timeout = to)  # open serial port
    return (ser.name)

def CloseSerial():
    global ser
    ser.close()
    return('done')

def WriteSerial(string):
    global ser
    return(ser.write(string.encode()))    # write a string

def ScriptSerial(string):
    global ser
    reply = ''
    lines = string.split('\n')
    for line in lines:
        ser.write(line.encode())
        time.sleep(1)
        reply += ReadSerial() + '\n'
    return reply 

def ReadSerial():
    global ser
    reply = ''
    if ser.in_waiting:
        reply = ser.readline().decode()
    return(reply)
