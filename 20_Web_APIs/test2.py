import praw


red = praw.Reddit(user_agent='pyred')
red.get_top()