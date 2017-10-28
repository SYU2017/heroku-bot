# Dependencies
import pandas as pd
import tweepy
import time
import json
import random

# Twitter API Keys
consumer_key = '0k7SkdnPgcuNr8iNjvJTTpZeP'
consumer_secret = 'TSUQyAKRv9PdzWMURP2UC4oeh6AM0tLbiaArPDW37t6RpfF2FW'
access_token = '4730606363-p4bAJ5PXnfiYaAHaJjxMzuD4TVBtyMGJ2D6cpMx'
access_token_secret = 'SFhrZuarDF0jubsGwNxVXOg08dArMpQwOcyFWwd8xpLu5'
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]


# Create function for tweeting
def HappyItUp():

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet a random quote
    api.update_status(random.choice(happy_quotes))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every minute
while(True):
    HappyItUp()
    time.sleep(60)
