import serial
import sys
import glob
import time
import serial.tools.list_ports

ser = None

def serial_ports():
     result = []
     ports = serial.tools.list_ports.comports()
     for port, desc, hwid in sorted(ports):
          comm =  "{}: {}".format(port, desc)
          result.append(comm) 
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

def WriteBytes(data,replyLength):
    try:
        buffer=ser.read(ser.in_waiting)
        reply = ser.write(bytes(data))
        if (replyLength < 0): return []
        return list(ser.read(replyLength))    # write bytes and get reply
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