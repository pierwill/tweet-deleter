Tweet Deleter
=============

I was sick of those web apps. Get you some Twitter API credentials and
prune your timeline with python!

How to use
----------

Get some Twitter API credentials [here](https://apps.twitter.com/).

Download your twitter archive from [Twitter.com](https://twitter.com/settings/account).

Open "tweets.csv" and remove those tweets that you **do not** want to
delete. Next, remove the header row. You'll end up with a nice list of
unwanted tweets to pass to tweet-deleter.py.

Do a test run:

```
./tweet-deleter.py --test -v [your "tweets.csv" of tweets you want to delete]
```

If this looks good, run

```
./tweet-deleter.py [your "tweets.csv" of tweets you want to delete]
```

(Make sure you have the `docopt` and `tweepy`
requirements. [Docopt](http://docopt.org/) is very cool.)

---

Usage details:

```
tweet-deleter.py is a tool to delete tweets en masse.

Usage:
 tweet-deleter.py [options] LIST

LIST is a csv file with a tweet status ID to be deleted beginning each
line. Ideally this is a modified Twitter.com-provided "tweets.csv" archive.

Recommended: running a verbose test ("--test -v") before deleting anything.

Options:
  -t, --test         test mode, does not delete tweets
  -v, --verbose      show tweet date and partial text

Also:
  -h, --help
  --version

Examples:
  ./tweet-deleter.py --test -v tweets-to-be-deleted.csv
  ./tweet-deleter.py tweets-to-be-deleted.csv
```

---

Inspired by [this post](http://www.mathewinkson.com/2015/03/delete-old-tweets-selectively-using-python-and-tweepy).
