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
        return ports
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def InitSerial(port, bps = 9600, to = 0):
    global ser
    ser = serial.Serial(port, bps, timeout = to)  # open serial port
    ser.flushInput()
    ser.flushOutput()
    return ser.name

def FlushSerial():
    ser.flushInput()
    ser.flushOutput()
    return(ser.in_waiting)

def CloseSerial():
    ser.flush()
    ser.close()
    return('done')

def WriteSerial(string):
    return (ser.write(string.encode()))    # write a string

def WriteBytes(data,replyLength):
    buffer=ser.read(ser.in_waiting)
    reply = ser.write(bytes(data))
    if (replyLength < 0): return []
    return list(ser.read(replyLength))    # write bytes and get reply

def ScriptSerial(string):
    reply = ''
    lines = string.split('\n')
    for line in lines:
        ser.write(line.encode())
        time.sleep(1)
        reply += ReadSerial() + '\n'
    return reply 

def ReadSerial():
    reply = ''
    if ser.in_waiting:
        reply = ser.readline().decode()
    return(reply)

# note if the timeout is anything but zero it is slow