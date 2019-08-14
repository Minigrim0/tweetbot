import os
import sys
import time
import requests
from twython import Twython
import os.path

tweetStr = "a"*256 #Satisfying the condition to enter the loop
homedir = os.path.expanduser("~")
appdir = "/Documents/tweetbot/"

while len(tweetStr) > 255:
        try:
            os.system("python3 " + homedir + appdir + "getQuote.py")
        except:
            with open(homedir + appdir + "quote.txt", "w") as f:
                f.write("I have nothing to tell you. \n")
        quote = " ".join(open(homedir + appdir + "quote.txt").readlines())
        print(quote)

        tweetStr = quote + "\n #growth #basilic"

        print("len :", len(tweetStr))

CONSUMER_KEY = 'SUPERSECRET'
CONSUMER_SECRET = 'YOULLNEVERFIND'
ACCESS_TOKEN = 'WELLATLEASTYOUTRIED'
ACCESS_SECRET = 'NOPNOTTHISONE'

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

photo = open(homedir + appdir + 'pic.jpg', 'rb')
response = api.upload_media(media=photo)
api.update_status(status=tweetStr, media_ids=[response['media_id']])
