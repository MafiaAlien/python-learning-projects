import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url address: ')
sample = urllib.request.urlopen(url)
data = sample.read()

js = json.loads(data)
numbers = js["comments"]
# print('Retrieve data',len(js))

total = 0
for number in numbers:
	total += number['count']
print(total)
