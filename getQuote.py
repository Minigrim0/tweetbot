import requests
from settings import homedir, appdir

QUOTEURL = "http://www.quotationspage.com/random.php"

quote = requests.get(QUOTEURL)
start = quote.text.index("\"/quote/")  # find first quote occurence
# retain beginning index of quote
start = quote.text.index(">", start, len(quote.text)) + 1
end = quote.text.index("</a>", start, len(quote.text))

with open("{}{}quote.txt".format(homedir, appdir), "w") as f:
    f.write(quote.text[start:end] + "\n")
