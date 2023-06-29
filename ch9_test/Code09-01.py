

#맥에서 열 때, 추가 작업 필요
# import ssl

# ssl_context = ssl.SSLContext()
# ssl_context.verify_mode = ssl.CERT_NONE


# nateUrl = "https://www.nate.com"
# htmlObject = urllib.request.urlopen(nateUrl,context=ssl_context)


import urllib.request
import ssl

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl,context=ssl_context)

html = htmlObject.read()

print(html)