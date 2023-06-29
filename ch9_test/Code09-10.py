import bs4
import urllib.request
import ssl

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl,context=ssl_context)

bsObject = bs4.BeautifulSoup(htmlObject, 'html.parser')

# webPage = htmlObject.read()
# bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'id':'NateBi'})
print()
print(tag , '\n')

a_tag = tag.find("a")
print(a_tag , '\n')

href = a_tag['href']
print( href , '\n')

text = a_tag.text
print(text)