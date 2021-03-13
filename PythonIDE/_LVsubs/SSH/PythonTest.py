import paramiko,time
from scp import SCPClient

gSSHRef = None
gchannel = None
scp = None

def InitSSH(server,username,password):
    global gSSHRef, gchannel,scp

    reply = 'already there'
    if gSSHRef == None:
        gSSHRef = paramiko.SSHClient()
        gSSHRef.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        result = gSSHRef.connect(server, username=username, password=password, timeout = 5)
        reply = str(result)
        gchannel = gSSHRef.invoke_shell()
        gchannel.settimeout(0)
    #scp = SCPClient(gSSHRef.get_transport())
    return reply

def CloseSSH():
    if gchannel != None:
        gchannel.close()
    if gSSHRef != None:
        gSSHRef.close()
    if scp != None:
        scp.close()
    return('done')

def WriteSSH(string):
    global gSSHRef, gchannel,scp
    reply = 'no reference'
    if gSSHRef != None:
        reply = 'no file'
        if gchannel != None:
            size = gchannel.send(string.encode())
            reply = str(size)
    return reply

def ReadSSH():
    global gSSHRef, gchannel,scp
    reply = 'no reference'
    if gSSHRef != None:
        reply = 'no file'
        if gchannel != None:
            reply = ''
            if gchannel.recv_ready():
                reply = gchannel.recv(9999).decode()

    return(reply)

def WriteWaitReadSSH(string,char,timeout=10000):
     global gSSHRef, gchannel,scp
     reply = ReadSSH()
     WriteSSH(string)
     n = int(timeout/10)
     for i in range(n):
         ans = ReadSSH()
         reply = reply + ans
         if ans.find(char) >= 0:
             #print(ans)
             return reply
         time.sleep(0.01)
     return reply

def scp_get(name):
     try:
          scp.get(name)
          return 'get succeeded\n'
     except Exception as e:
          return  'scp.get('+name+')\n' +str(e)

def scp_put(source, dest):
     try:
          scp.put(source, dest)
          return 'scp.put('+source+','+dest+')\n' +'put succeeded\n'
     except Exception as e:
          return str(e)

def scp_put_all(source, dest):
     try:
          scp.put(source, recursive = True, remote_path = dest)
          return 'put succeeded\n'
     except Exception as e:
          return str(e)

InitSSH('192.168.86.136','pi','BuddhaLives')
for i in range(10):
    ReadSSH()
    WriteSSH('\n\n')
    time.sleep(1)
CloseSSH()
