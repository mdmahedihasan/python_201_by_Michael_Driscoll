import requests
from bs4 import BeautifulSoup


url = "https://twitter.com/mousevspython"

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, "lxml")
tweets = soup.find_all("li", "js-stream-item")

for item in range(len(soup.find_all("p", "TweetTextSize"))):
    tweet_text = tweets[item].get_text()
    print(tweet_text)
    dt = tweets[item].find("a", "tweet-timestamp")
    print("this was tweeted on " + dt)