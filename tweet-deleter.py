#!/usr/bin/env python

# this is the special string with which docopt does its magic!

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

# end docopt magic... for now

from docopt import docopt
import tweepy
import csv
from time import sleep

# get credentials and create api object
from secrets import consumer_key, consumer_secret, access_token, access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

# function that deletes tweets
def deleter(LIST, test, verbose):

    # open the file passed as an argument on the CL and make a csv object for it
    arch = open(LIST, "r")
    csvreader = csv.reader(arch)
    
    # iterate over the lines
    for line in csvreader:
        if verbose:
            try:
                # print tweet id and snippets of the tweet's date and text
                print "Deleting " + line[0] + " from " + line[3][:10] + ": \"" + line[5][:50] + "...\""
            except IndexError: # e.g., if the file is just a simple list of tweet ids
                print "Deleting " + line[0]
        else:
            print "Deleting " + line[0]

        # the actual deleting happens here
        # this is not a test
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
    arguments = docopt(__doc__, version="0.1") # docopt magic
    main()
