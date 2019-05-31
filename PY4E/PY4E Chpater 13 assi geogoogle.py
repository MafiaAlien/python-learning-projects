import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter a place: ')

query_str = urllib.parse.urlencode({'address': address, 'key': 42})

url = serviceurl + query_str
uh = urllib.request.urlopen(url)
data = uh.read().decode()


try:
	js = json.loads(data)
except:
	js = None

if not js or 'status' not in js or js['status'] != 'OK':
	print('=== Failure to retrieve ===')
	print(data)

placeid = js['results'][0]['place_id']
print(placeid)
