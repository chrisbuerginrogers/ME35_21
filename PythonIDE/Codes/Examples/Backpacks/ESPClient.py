import network,usocket,ussl,utime,ujson,ubinascii

def wifi(SSID,KEY):
    wlan = network.WLAN()
    wlan.active(True)
    wlan.connect(SSID, KEY)
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    while '0.0.0.0' in wlan.ifconfig():
        utime.sleep(1)
    return wlan.ifconfig()

def REST(base, port, request, verbose = False):
    addr = usocket.getaddrinfo(base, port)[0][4]
    if verbose: print(addr)
    client = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    client.connect(addr)
    client.settimeout(3.0)
    if port == 443:
        try:
            client = ussl.wrap_socket(client, server_hostname=base)
        except Exception as e:
            if verbose:
                print('problem with ussl')
                print(e)
            return -1,'',''
    client.write(request)

    l = client.readline()
    if verbose: print(l)
    l = l.split(None, 2)
    status = int(l[1])
    reason = ''
    if len(l) > 2:
        reason = l[2].rstrip()
    if not (status == 200): return status, reason, ''
    l = client.readline()
    reply_h ={}
    if verbose: print(b' -' +l)
    while l and not l == b'\r\n':
        l = l.decode()
        k, v = l.split(':', 1)
        reply_h[k.lower()] = v.strip()
        l = client.readline()
        if verbose: print(b' --' + l)
    try:
        length = int(reply_h['content-length'])
        reply=client.read(length).decode()
        if verbose: print('LENGTH')
        if verbose: print(reply)
    except:
        if verbose: print('CHUNK')
        reply =''
        l = client.readline()
        while l and not l == b'\r\n':
            if verbose: print(b' ---  ' + l)
            reply += l.decode()
            l = client.readline()

        if verbose: print(reply)
    return status, reason, reply
