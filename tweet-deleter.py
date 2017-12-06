#!/usr/bin/env python

"""

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

"""

from docopt import docopt
import tweepy
import csv
from time import sleep

# get credential and create api object
from secrets import consumer_key, consumer_secret, access_token, access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

# function that deletes tweets
def deleter(LIST, test, verbose):

    arch = open(LIST, "r")
    csvreader = csv.reader(arch)
    
    for line in csvreader:
        if verbose:
            try:
                print "Deleting " + line[0] + " from " + line[3][:10] + ": " + line[5][:50] + "..."
            except IndexError:
                print "Deleting " + line[0]
        else:
            print "Deleting " + line[0]
        if not test:
            try:
                twitter.destroy_status(line[0])
                sleep(1)
                print "Deleted " + line[0]
            except tweepy.error.TweepError:
                print "Error: Not deleting " + line[0]
                sleep(1)
                pass

    arch.close()

def main():
    deleter(arguments['LIST'], arguments['--test'], arguments['--verbose'])

if __name__ == '__main__':
    arguments = docopt(__doc__, version="0.1")
    main()
