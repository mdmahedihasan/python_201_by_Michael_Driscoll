import urllib.request


url = urllib.request.urlopen("http://www.google.com")
print(url.geturl())
print(url.info())
print(url.info().as_string())
print(url.getcode())