import urllib.request


url = urllib.request.urlopen("https://www.google.com/")
print(url.geturl())
print(url.info())
print(url.getcode())
print(url.read())