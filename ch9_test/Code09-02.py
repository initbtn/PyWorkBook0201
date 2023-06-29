import urllib.request
import bs4
import ssl

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl,context=ssl_context)

bsObject = bs4.BeautifulSoup(htmlObject, 'html.parser')

print(bsObject)