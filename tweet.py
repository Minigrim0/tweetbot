import os
from twython import Twython
from settings import homedir, appdir

tweetStr = "a"*256  # Satisfying the condition to enter the loop

while len(tweetStr) > 255:
    try:
        os.system("python3 {}{}getQuote.py".format(homedir, appdir))
    except Exception:  # In case the quote couldn't be fetched
        with open("{}{}quote.txt".format(homedir, appdir), "w") as f:
            f.write("I have nothing to tell you. \n")

    quote = " ".join(open("{}{}quote.txt".format(homedir, appdir)).readlines())
    tweetStr = quote + "\n #growth #basilic"

CONSUMER_KEY = 'SUPERSECRET'
CONSUMER_SECRET = 'YOULLNEVERFIND'
ACCESS_TOKEN = 'WELLATLEASTYOUTRIED'
ACCESS_SECRET = 'NOPNOTTHISONE'

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

photo = open(homedir + appdir + 'pic.jpg', 'rb')
response = api.upload_media(media=photo)
api.update_status(status=tweetStr, media_ids=[response['media_id']])
