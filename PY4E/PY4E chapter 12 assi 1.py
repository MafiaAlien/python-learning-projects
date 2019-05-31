from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter a web address :')
html = urlopen(url,context=ctx).read()

soup = BeautifulSoup(html,"html.parser")


tags = soup('span')
number = 0

for tag in tags:
    number = number + int(tag.contents[0])
#print(tag.contents)
print(number)
