import urllib.request
import urllib.parse


data = urllib.parse.urlencode({"q": "python"})
print(data)
url = "http://duckduckgo.com/html/"
full_url = url + '?' + data
response = urllib.request.urlopen(full_url)

with open("/home/mahedi/Desktop/results.html", "wb") as f:
    f.write(response.read())