import requests
import os.path

QUOTEURL = "http://www.quotationspage.com/random.php"

quote = requests.get(QUOTEURL)
start = quote.text.index("\"/quote/") # find first quote occurence
start = quote.text.index(">", start, len(quote.text)) + 1 # retain beginning index of quote
end   = quote.text.index("</a>", start, len(quote.text))

homedir = os.path.expanduser("~")

with open(homedir + "/Documents/tweetbot/quote.txt", "w") as f:
	f.write(quote.text[start:end] + "\n")
