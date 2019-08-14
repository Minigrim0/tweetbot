# TWEETBOT
Tweetbot is a bot that allows you to take a pictures regularly and post it on twitter with a random quote gathered on the internet.

## Installation
The easiest way to install it is to clone this repository in your "Documents" folder.
If you prefer to install it somewhere else, you'll have to change some lines of code.

* get_pic.py line 12  ``` pygame.image.save(img, homedir + "/path/you/want/from/home/$USER/tweetbot/pic.jpg") ```
* getQuote.py line 13 ``` with open(homedir + "/path/you/want/from/home/$USER/tweetbot/quote.txt", "w") as f: ```
* savePic.sh line 3   ``` cp /home/$USER/Documents/tweetbot/pic.jpg /home/$USER/Path/you/want/tweetbot/imgs/$NOW.jpg ```
* tweet.py line 10    ``` appdir = "/path/you/want/tweetbot/" ```


You may need to install python3 requirements, to do so, simply type ``` pip3 install -r requirements.txt ``` once in the tweetbot folder

## utilization
First, you'll need a [twitter developer account](https://developer.twitter.com) and you'll need to create a new application.

Then you'll get :

* A consumer key
* A consumer secret
* An access token
* An access secret

Simply copy-paste these keys in the corresponding vars in tweet.py file

Then you simply need to add automatic tasks with crontab, which will first run 

```
python3 /path/to/your/folder/get_pic.py /path/to/your/webcam 
```

and then

```
python3 /path/to/your/folder/tweet.py
```

And you're good to go !
