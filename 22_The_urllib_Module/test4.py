import urllib.request


url = "http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip"

print(urllib.request.urlretrieve(url, "/home/mahedi/Desktop/blog.zip"))