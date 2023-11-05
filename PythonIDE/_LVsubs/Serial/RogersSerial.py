# https://github.com/scientifichackers/ampy/blob/master/ampy/files.py#L216
import serial
import time
import textwrap
import binascii

import serial.tools.list_ports

ser = None

def serial_ports():
    result = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        comm =  "{}: {}".format(port, desc)
        result.append(comm) 
    return result


BUFFER_SIZE = 32

class SerialError(BaseException):
    pass

class campy():
    def __init__(self, device = None, verbose = False):
        self.device = device
        self.serial = None
        self.verbose = verbose

    def address(self, device):
        self.device=device
        
    def printIt(self, payload):
        if self.verbose:
            print(payload)
        
    def open_serial(self):
        try:
            self.serial = serial.Serial(self.device, baudrate=115200, interCharTimeout=1, timeout = 0)
        except Exception as e:
            print(e)
            
    def close_serial(self):
        self.serial.close()

    def flush(self):
        n = self.serial.inWaiting()
        while n > 0:
            self.serial.read(n)
            n = self.serial.inWaiting()

    def read_until(self, min_len, ending, timeout = 10):
        data = self.serial.read(min_len)
        timeout_count = 0
        while True:
            #print(data)
            if data.endswith(ending):
                break
            elif self.serial.inWaiting() > 0:
                new_data = self.serial.read(1)
                data = data + new_data
                timeout_count = 0
            else:
                timeout_count += 1
                if timeout is not None and timeout_count >= 1 * timeout: #used to be 100 *
                    self.printIt('timeout')
                    self.printIt(ending)
                    self.printIt(data)
                    break
                time.sleep(0.01)
        return data

    def send_get(self, payload, expected, tries = 1):
        for retry in range(0, tries): 
            self.serial.write(payload) 
            data = self.read_until(1, expected)
            if data.endswith(expected):
                self.printIt('Read: ' + repr(data))
                return True
        raise SerialError('no raw mode')

    def run_line(self, command):
        if isinstance(command, bytes): command_bytes = command
        else: command_bytes = bytes(command, encoding='utf8')
        self.flush()
        #self.read_until(1, b'>')
        self.printIt('Sending: '+ repr(command))
        for i in range(0, len(command_bytes), 256):
            self.serial.write(command_bytes[i:min(i + 256, len(command_bytes))])
            time.sleep(0.01)
        self.send_get(b'\x04',b'OK',1)
                    
    def go_raw(self):
        self.serial.write(b'\r\x03')
        time.sleep(0.1)
        self.serial.write(b'\x03')
        time.sleep(0.1)
        self.flush()

        self.send_get(b'\r\x01', b'raw REPL; CTRL-B to exit\r\n>', 5)
        self.send_get(b'\x04', b'soft reboot\r\n', 1)
        time.sleep(0.5)
        self.serial.write(b'\x03')
        time.sleep(0.1) 
        self.send_get(b'\x03', b'raw REPL; CTRL-B to exit\r\n', 1)

    def close_raw(self):
        self.serial.write(b'\r\x02') # ctrl-B: enter friendly REPL
        
    def send_code(self, filename, data):
        self.run_line("f = open('%s', 'wb')"%(filename))
        size = len(data)
        # Loop through and write a buffer size chunk of data at a time.
        for i in range(0, size, BUFFER_SIZE):
            chunk_size = min(BUFFER_SIZE, size - i)
            chunk = repr(data[i : i + chunk_size])
            # Make sure to send explicit byte strings (handles python 2 compatibility).
            if not chunk.startswith("b"):
                chunk = "b" + chunk
            self.run_line("f.write(%s)"%(chunk))
        self.run_line("f.close()")

    def download(self, filename, data, init=True):
        if init:
            self.open_serial()
        self.go_raw()
        self.send_code(filename, data)
        self.close_raw()
        if init:
            self.close_serial()
        payload =  fred.upload(filename, init).decode()
        return (data == payload), payload
        
    def upload(self, filename, init = True):
        command = """
            import sys
            import ubinascii
            with open('%s', 'rb') as infile:
                while True:
                    result = infile.read(%d)
                    if result == b'':
                        break
                    len = sys.stdout.write(ubinascii.hexlify(result))
        """ % (filename, BUFFER_SIZE)
        
        if init:
            self.open_serial()
        self.go_raw()
        try:
            self.run_line(textwrap.dedent(command))
            out = self.read_until(1, b'\x04')
            self.printIt(out)
        except SerialError as ex:
            # Check if this is an OSError #2, i.e. file doesn't exist and
            # rethrow it as something more descriptive.
            try:
                message = ex.args[2].decode("utf-8")
                if message.find("OSError") != -1 and message.find("2") != -1:
                    raise RuntimeError("No such file: {0}".format(filename))
                else:
                    raise ex
            except UnicodeDecodeError:
                raise ex
        self.close_raw()
        if init:
            self.close_serial()
        out = out[:-1]
        return binascii.unhexlify(out)

fred=campy('COM3')

def address(device):
    fred.address(device)

def smartaddress():
    device = '/dev/cu.usbmodem1101'
    ports = serial_ports()
    for port in ports:
        if 'cu.usb' in port:
            device = port.split(':')[0]
            fred.device = device
            break
    return device

def InitSerial(port, bps = 9600, to = 0):
    try:
        fred.device = port
        fred.serial = serial.Serial(port, bps, timeout = to)  # open serial port
        fred.serial.flushInput()
        fred.serial.flushOutput()
        return fred.serial.name
    except Exception as e:
        return 'ERR: ' + str(e)

def CloseSerial():
    try:
        fred.serial.flush()
        fred.serial.close()
        return 'done'
    except Exception as e:
        return 'ERR: ' + str(e)   

def WriteSerial(string):
    try:
        reply =  fred.serial.write(string.encode())
        return str(reply)
    except Exception as e:
        return 'ERR: ' + str(e)    

def ReadSerial():
    try:
        reply = ''
        if fred.serial.in_waiting:
            reply = fred.serial.readline().decode()
        return reply
    except Exception as e:
        return 'ERR: ' +  str(e)

def download(file, code):
    s, p = fred.download(file, code, True)
    return str(s) +','+ p

def simpledownload(file, code):
    s, p = fred.download(file, code, False)
    return str(s) +','+ p

def upload(file):
    return  fred.upload(file).decode()
