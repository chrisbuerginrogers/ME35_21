# Code to generate a generic webpage

Start_html = '''
            <html>
            <body style="width:960px; margin: 20px auto;">
            <aside bgcolor="#FFFFFF" style="float:left;width:500px;">
              <h3><br><br>Welcome to {}</h3>
                <p>You are connected to {} on {}</p>
                <form action="/IP" method="POST">
                    <input type="submit" name="Close" value="Close" onclick="myFunction()">
                </form>
              <form action="/" method="POST">
                <select name = "page">
                {}
                </select>
                <input type="submit" name ="Page">
               </form>
              
              Some Hints:  click on these buttons and see what they do on the hub.
              See the text below to see the python code they send.  Try typing your
              own versions of the code and hit the Send Command button
              <br><br>
              '''
Form_html = '''
               
                  <form action="/" method="POST">
                       <textarea rows="{}" cols="60" name = "{}"
                          style = "border:none;resize:none;background-color:#F5F5F5"
                       >{}</textarea>
                      <input type="submit" name = "REPL" value = "{}"><br>

                  </form>
'''
Rest_html = '''
              </p>
             </aside>
           <h1>{} Terminal Window</h1>
            <aside bgcolor="#FFFFFF" style="float:right;width:400px;"><br><br><br><br><br><br>
            Type your script below and then hit "Send Command"
                <form action="/" method="POST">
                    <textarea rows="10" cols="60" name = "Text to send"> {} </textarea>
                    <input type="submit" name="SendCommand" value="Send Script">
                </form>
                <form action="/" method="POST">
                     <input type="submit" name="Clear" value="Clear Terminal" onclick="myFunction()">
                </form>
                <form action="/" method="POST">
                    <textarea rows="21" cols="60" name = "TerminalWindow">{} </textarea>
                    <input type="submit" name="SendCommand" value="update">
                </form>
            </aside>
            </body>
            </html>
'''

Init_html = '''
            <html>
            <body style="width:960px; margin: 20px auto;">
            <aside bgcolor="#FFFFFF" style="float:left;width:400px;">
              <h3><br><br>Welcome to {}</h3>
              <form action="/" method="POST">
             <p>
              Some Hints:<br> First, hit the connect button.<br>
                If it does not connect, make sure it is on and plugged in
              </p>
             </aside>
            <h1>{} Terminal Window</h1>
            <form action="/IP" method="POST">
            <aside bgcolor="#FFFFFF" style="float:right;width:400px;">
            <p>Press Connect to connect to {}</p>
               <form action="/" method="POST">
                 <select name = "processors">
                   {}
                   </select>
                <input type="submit" name = "Connect">
               </form>
            </aside> 
            </body>
            </html>
'''


from time import sleep
from http.server import BaseHTTPRequestHandler
import getpass, sys, socket, os
import serial,glob,time

from urllib.parse import unquote

# Initialize global variables
connected = False
terminal = "" #intialize blank terminal
ser = None
spike = ''
page = "start"
script = 'Type Here'

def InitSerial(port, bps = 115200, to = 0):
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

def ReadSerial():
    global ser
    reply = ''
    if ser.in_waiting:
        reply = ser.read(ser.in_waiting).decode()
    return(reply)

def serial_ports():
    result = []
    if sys.platform.startswith('win'):
        for i in range(256):
            try:
                s = serial.Serial('COM%s' % (i + 1))
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
        for port in ports:
            if 'usbmodem' in port:
                result.append(port)
    else:
        raise EnvironmentError('Unsupported platform')
    print(result)
    return result

def StartConnection():

    print('looking')
    reply = ''
    try:
        reply = serial_ports()
    except:
        pass
    return(reply)

def WaitForIt():
    doneReading = False
    text = ''
    starttime = time.time()
    while not doneReading:
        text = text + ReadSerial()
        doneReading = '>>>' in text
        if (time.time() > starttime+1):
            break
    return text

def SendIt(text):
    global ser
    
    WriteSerial(text + '\r\n')
    reply = WaitForIt()
    return(reply)

# Webserver
class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        global connected
        global terminal,script
        global spike

        print('page = ' + page)
        self.do_HEAD()
        if  (page == 'start'):
            connections = StartConnection()
            p_list = ''
            for p in connections:
                p_list = p_list + '''<option selected="{}">{}</option>'''.format(p,p)
            self.wfile.write(Init_html.format(processor,processor,processor,p_list).encode("utf-8"))
        else:
            page_list = ''
            for p in pyCode:
                if p == page:
                    select = 'selected'
                else:
                    select = ''
                page_list = page_list + '<option {}>{}</option>'.format(select,p)
            pageContent = Start_html.format(processor,processor,spike,page_list)
            if  page  in pyCode:
                for line in pyCode[page]:
                    pageAppend = Form_html.format(len(pyCode[page][line][1].split('\n')),line,pyCode[page][line][1],pyCode[page][line][0])
                    pageContent = pageContent + pageAppend
            else:
                pageContent = 'Error - you are asking for a page that does not exist'
            pageContent = pageContent + Rest_html.format(processor,script.strip(),terminal)
            self.wfile.write(pageContent.encode("utf-8"))

    def do_POST(self):
        global connected
        global terminal,script
        global ser
        global spike, page

        content_length = int(self.headers['Content-Length'])  # Get the size of data
        post_data = self.rfile.read(content_length).decode('utf-8')  # Get the data
        #print(post_data)
        post_data = post_data.split("=")[1]  # Only keep the value
        print('POST data ' + post_data) # Uncomment for debugging
        

        if 'Connect' in post_data and spike == '':
            spike = unquote(post_data.split("&")[0]) #StartConnection()[0].strip()
            if not (spike == ''):
                InitSerial(spike)
                WriteSerial('\x03\n')
                reply = WaitForIt()
                terminal = "Starting...\n"+ reply
                page = 'simple'
            else:
                terminal = "Failed to connect\n"
            print("-----------Connection Initiated-----------")

        elif 'SendCommand' in post_data and not (spike == ''):
            command = post_data.split("&")[0]
            if not (len(command) == 0):
                command = command.replace("+", " ")
                command = unquote(command).split(">>>")[-1]
                command = command.strip()  #replace('\r','\n')
                script = command   #keep this in memory to update the terminal
                cmds = command.split('\n')
                for sendcmd in cmds:
                    sendcmd = sendcmd.strip()
                    print('Command to send ' + sendcmd)
                    terminal = terminal+SendIt(sendcmd)

        elif 'Close' in post_data and not (spike == ''):
            CloseSerial()
            terminal = terminal + '\n closed'
            spike = ''
            page = 'start'
            
        elif 'Clear' in post_data:
            print('clearing')
            terminal = '>>> '
            
        elif 'Page' in post_data:
            print('new page: ' + post_data)
            if 'simple' in post_data:
                page = 'simple'
            if 'accel' in post_data:
                page = 'accel'
            if 'sensor' in post_data:
                page = 'sense'
            if 'advance' in post_data:
                page = 'advance'
            
        elif not (spike == ''):
            LinesOfCode = unquote(post_data.split("&")[0].replace("+", " ")).split('\n')
            print(LinesOfCode)
            for line in LinesOfCode:
                terminal = terminal + SendIt(line.strip())
            
            
        self._redirect('/')  # Redirect back to the root url
