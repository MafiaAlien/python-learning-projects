import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url address: ')
sample = urllib.request.urlopen(url)
data = sample.read()

tree = ET.fromstring(data)
numbers = tree.findall('.//count')

print('Numbers: ', len(numbers))

total = 0
for number in numbers:
	total += int(number.text)
print(total)