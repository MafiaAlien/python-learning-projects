# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def spidering(url,position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags[position].get('href',None)


count = int(input('Enter count:'))
position = int(input('Enter position:'))-1


for i in range(count):
# Retrieve all of the anchor tags
    if i == 0:
        present_url = input('Enter URL:')
        present_url = spidering(present_url,position)
        print(present_url)
    else:
        present_url = spidering(present_url,position)
        print(present_url)
print('Done')