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
    try:
        ser = serial.Serial(port, bps, timeout = to)  # open serial port
        ser.flushInput()
        ser.flushOutput()
        return ser.name
    except Exception as e:
        return 'ERR: ' + str(e)

def CloseSerial():
    return('done')
    try:
        ser.flush()
        ser.close()
        return 'done'
    except Exception as e:
        return 'ERR: ' + str(e)    

def WriteSerial(string):
    try:
        reply = ser.write(string.encode())
        return str(reply)
    except Exception as e:
        return 'ERR: ' + str(e)    

def ReadSerial():
    try:
        reply = ''
        if ser.in_waiting:
            reply = ser.readline().decode()
        return reply
    except Exception as e:
        return 'ERR: ' +  str(e)

# note if the timeout is anything but zero it is slow