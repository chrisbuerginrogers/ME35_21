import hub
import utime

class screen:
    def __init__(self, port): 
        self.s=port
        port.mode(hub.port.MODE_FULL_DUPLEX)
        utime.sleep(0.1)
        self.s.baud(115200)   
        
        
    def fillScreen(self, x):
        self.ret=self.call_function("graphics",2,[x]) #fillScreen
        return self.ret

    def setTextSize(self, x):
        self.ret=self.call_function("graphics",3,[x]) #setTextSize
        return self.ret

    def drawString(self, string,x,y):
        self.ret=self.call_function("graphics",1,[string,x,y])#drawString
        return self.ret

    def drawLine(self, x1,y1,x2,y2,c):
        self.ret=self.call_function("graphics",4,[x1,y1,x2,y2,c])#drawLine
        return self.ret
       
    def drawPixel(self, x,y,c):
        self.ret=self.call_function("graphics",5,[ x,y,c])#drawPixel
        return self.ret
    
    def drawRect(self, x1,y1,x2,y2,c):
        self.ret=self.call_function("graphics",6,[x1,y1,x2,y2,c])#"drawRect"
        return self.ret
       
    def fillRect(self, x1,y1,x2,y2,c):
        self.ret=self.call_function("graphics",7,[x1,y1,x2,y2,c])#"drawRect"
        return self.ret
       
    def drawCircle(self, x,y,r,c):
        self.ret=self.call_function("graphics",8,[x,y,r,c])#"drawCircle"
        return self.ret
    
    def fillCircle(self, x,y,r,c):
        self.ret=self.call_function("graphics",9,[x,y,r,c])#"fillCircle"
        return self.ret
    
    def drawTriangle(self, x1,y1,x2,y2,x3,y3,c):
        self.ret=self.call_function("graphics",10,[x1,y1,x2,y2,x3,y3,c])#"drawTriangle"
        return self.ret
    
    def fillTriangle(self, x1,y1,x2,y2,x3,y3,c):
        self.ret=self.call_function("graphics",11,[x1,y1,x2,y2,x3,y3,c])#"fillTriangle"
        return self.ret
    
    def drawRoundRect(self, x1,y1,x2,y2,r,c):
        self.ret=self.call_function("graphics",12,[x1,y1,x2,y2,r,c])#"drawRoundRect"
        return self.ret
    
    def fillRoundRect(self, x1,y1,x2,y2,r,c):
        self.ret=self.call_function("graphics",13,[x1,y1,x2,y2,r,c])#"fillRoundRect"
        return self.ret
    
    def connectWifi(self, ssid, pwd):
        self.ret=self.call_function("wifi",1,[ssid,pwd])
        return self.ret
        
        
    def setAirtable(self, AppKey, baseID):
        self.ret=self.call_function("wifi",4,[AppKey,baseID]) # set credentials for Airtable
        return self.ret
    
    def getAirtable(self, table):
        self.ret=self.call_function("wifi",5,[table]) #get value from Airtable
        return self.ret
    
    def postAirtable(self, table, field, value):
        self.ret=self.call_function("wifi", 6,[table,field, value]) #putvalue on Airtable field
        return self.ret

    def call_function(self, library, fname,arg):
        try:
            self._waitACK= b''
            self._iter=len(arg)
            self.s.write(("{\"lib\":\""+ str(library) + "\",").encode())
            utime.sleep(0.01)
            self.s.write(("\"function\":\""+ str(fname) +"\",").encode())
            utime.sleep(0.01)
            self.s.write("\"arg\":[".encode())
            utime.sleep(0.01)
            for _index in range(self._iter-1):
                self.s.write(("\""+str(arg[_index])+"\",").encode())
                utime.sleep(0.01)
            self.s.write(("\""+ str(arg[self._iter-1])+"\"").encode())
            utime.sleep(0.01)
            self.s.write("]}".encode())
            utime.sleep(0.01)
            self.s.write("done".encode())
            utime.sleep(0.01)
            self._waitACK=self.s.read(100)
            while(self._waitACK.decode("UTF-8").find("True")<0 and self._waitACK.decode("UTF-8").find("False")<0):
                self._waitACK+= self.s.read(100)
            if(self._waitACK.decode("UTF-8").find("True")<0):
                raise Exception("Arduino Error")
            else:
                return self._waitACK[:-6].decode("UTF-8")
            utime.sleep(0.1)
        except:
            raise Exception("Python Error")
