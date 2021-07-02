import hub, utime, ujson

class Backpack():
    def __init__(self, SPIKE_port, verbose = True ):
        self.ser = SPIKE_port
        self.ser.mode(hub.port.MODE_FULL_DUPLEX)
        utime.sleep(0.1)
        self.ser.baud(115200)
        self.verbose = verbose
        
    def setup(self):
        self.ser.write('\r\n')
        reply = self.read()
        connected = '>>>' in reply
        if not connected: 
            print('no dongle connected')
        return connected

    def read(self):  
        #reads the UART buffer until empty
        reply = b'sss'
        response = ''
        while (len(reply) > 0):
            utime.sleep(0.01)
            reply = self.ser.read(1000)
            if reply: 
                try: 
                    response += reply.decode()
                except:
                    response += 'ERR: ' + str(reply)
        return response
        
    def read_wait(self, to=5000):
        response = ''
        start = utime.ticks_ms()
        while (utime.ticks_ms()-start < to):
            response += self.read()
            if ('>>>' in response):
                return response
            utime.sleep(0.01)
        return response
        
    def upload(self, text, n=20): 
        #uploads string to the ESP in chunks
        reply = ''
        lines = [text[i:i+n] for i in range(0, len(text), n)]
        for line in lines: #need to go in chunks
            self.ser.write(line)
            reply += self.read()
        if not ('>>>' in reply):
            reply += self.read_wait()
        return reply

    def CtrlE_script(self, text):
        self.ser.write('\x05')
        reply = self.read()
        reply += self.upload(text)
        self.ser.write('\x04')
        reply += self.read_wait()
        return reply
    
    def show(self, text, eol= '\r\n'): 
        # makes reply text readable
        print('vvvvvvvvvvvvvvvvvvvv')
        lines = text.split(eol)
        for line in lines:
            print(line)
        print('^^^^^^^^^^^^^^^^^^^')
        
    def ask(self, text=''): 
        text = text.split('\r\n')[0]   #assume single line
        #if self.verbose: print('asked: %s' % self.clean(text))
        response = self.upload(self.clean(text)+'\r\n')
        if self.verbose: self.show(response,'\r\n')
        return response
        
    def clean(self, text, File = False):
        # cleans text to send out
        text = text.replace("'","\'")
        text = text.replace('"','\"')
        text = text.replace("\r\n", "\\r\\n")
        text = text.replace("\r", "\\r")
        text = text.replace('\n','\n') if File else text.replace('\n','\r\n')
        # note that you have a issue if you are trying to send '\n' as a search character etc
        return text
        
    def load(self,filename,text):
        self.ask('import os')
        files = self.ask('os.listdir()')
        if filename in files: self.ask('os.remove("%s")'%filename)
        payload = "f = open('%s','w')\r\n"% (filename)
        payload += "f.write(\'%s\')\r\n" %(self.clean(text, True).encode())
        payload += "f.write(b'" + new_str + "')\r\n"
        payload += 'f.close()\r\n'
        print(self.CtrlE_script(payload))
                
    def get(self,filename):
        payload = 'import os\r\n'
        payload += "f = open('%s','rb')\r\n"% (filename)
        payload += 'text = f.read()\r\n'
        payload += 'text = text[2:-1]\r\n'
        payload += 'f.close()\r\n'
        print('upld: ' + self.upload(payload))
        self.ask('print(text.decode())')

