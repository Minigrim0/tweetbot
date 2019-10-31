import requests
import os.path

QUOTEURL = "http://www.quotationspage.com/random.php"

quote = requests.get(QUOTEURL)
start = quote.text.index("\"/quote/")  # find first quote occurence
# retain beginning index of quote
start = quote.text.index(">", start, len(quote.text)) + 1
end = quote.text.index("</a>", start, len(quote.text))

homedir = os.path.expanduser("~")

with open(homedir + "/Documents/tweetbot/quote.txt", "w") as f:
    f.write(quote.text[start:end] + "\n")
