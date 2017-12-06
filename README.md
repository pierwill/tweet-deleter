Tweet Deleter
=============

I was sick of those web apps. Get you some Twitter API credentials and
prune your timeline with python!

How to use
----------

Download your twitter archive from Twitter.com.

Open "tweets.csv" and remove those tweets that you **do not** want to
delete. Next, remove the header row. You'll end up with a nice list of
unwanted tweets to pass to tweet-deleter.py.

Do a test run:

```./tweet-deleter.py --test -v [your "tweets.csv" of tweets you want to delete]```

If this looks good, run

```./tweet-deleter.py [your "tweets.csv" of tweets you want to delete]```

(Make sure you have the ```docopt``` and ```tweepy``` requirements.)

---

Inspired by [this post](http://www.mathewinkson.com/2015/03/delete-old-tweets-selectively-using-python-and-tweepy).
