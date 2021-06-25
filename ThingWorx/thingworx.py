import requests
import json

# Info
url = 'https://pp-2008281301ci.portal.ptc.io:8443/Thingworx/Things/MyHouse/Properties/'
headers = {'Content-Type':'application/json','Accept':'application/json','appKey':'3b9f3e5a-95c2-4eb7-937d-794488fc2396'}
propName = 'Fred'
propValue = {propName:2}

# PUT
requests.put(url+'*',headers=headers,json=propValue)

## GET
text = requests.get(url+propName,headers=headers).text
try:
    data = json.loads(text)
    rows = data.get('rows')
    value = rows[0][propName]
    print(value)
except:
    pass
#
