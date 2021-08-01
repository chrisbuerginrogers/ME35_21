import hub, utime, ujson

class Backpack():
    def __init__(self, SPIKE_port, verbose = True):
        self.ser = SPIKE_port
        self.ser.mode(hub.port.MODE_FULL_DUPLEX)
        utime.sleep(0.1)
        self.ser.baud(115200)
        self.verbose = verbose        
        
    def setup(self):
        reply = self.read()
        for i in range(3): # try 3 times
            self.ser.write('\x03\r\n')
            utime.sleep(0.1)
            reply += self.read()
            if '>>>' in reply: break
        return '>>>' in reply

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
        
    def EOL(self, response):
        E = '===' in response
        P = '>>>' in response
        I = '...' in response
        return (E or P or I)

    def read_wait(self, t0=5000):
        response = ''
        start = utime.ticks_ms()
        while (utime.ticks_ms()-start < t0):
            response += self.read()
            if self.EOL(response):
                return response
            utime.sleep(0.01)
        return response
        
    def upload(self, text, n=15, t0=5000): 
        #uploads string in chunks
        reply = ''
        lines = [text[i:i+n] for i in range(0, len(text), n)]
        for line in lines: 
            self.ser.write(line)
            reply += self.read()
        if not self.EOL(reply): 
            reply += self.read_wait(t0)
        return reply
    
    def show(self, text, eol= '\r\n'): 
        # makes reply text readable
        print('vvvvvvvvvvvvvvvvvvvv')
        lines = text.split(eol)
        for line in lines:
            print(line)
        print('^^^^^^^^^^^^^^^^^^^')
        
    def clean(self, text):
        # cleans text to send out
        text = text.replace("'","\'")
        text = text.replace('"','\"')
        text = text.replace("\r\n", "\\r\\n")
        text = text.replace("\r", "\\r")
        text = text.replace('\n','\\n')
        return text

    def ask(self, text=''): 
        text = text.split('\r\n')[0]   #assume single line
        #if self.verbose: print('asked: %s' % self.clean(text))
        response = self.upload(self.clean(text)+'\r\n')
        if self.verbose: self.show(response,'\r\n')
        return response
        
    def load(self,filename,text):
        self.ask('import os')
        files = self.ask('os.listdir()')
        if filename in files: 
            self.ask('os.remove("%s")'%filename)
        self.ask('\x05')
        self.ask('text = ""')
        redo = True
        while redo:
            redo = False
            for cmd in text.split('\n'):
                cmd = "text += \'" + cmd + "\\n\'"
                reply = self.ask(cmd)
                if 'ERR: ' in reply:
                    print('REDO')
                    redo = True
        self.ask('\x04')
        self.ask('f = open("%s","w")'%filename)
        self.ask('f.write(text)')
        self.ask('f.close()')

    def get(self,filename):
        self.ask('import os')
        self.ask("f = open('%s','r')" % filename)
        text = self.ask('f.read()')
        self.ask('f.close()')
        try:
            reply = text.split('\r\n')[1]
            reply = reply.replace('\\n','\n')[1:-2]
            return reply
        except:
            return text
