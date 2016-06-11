from twython import Twython
import json
import re

print("If you can read this, you have correctly installed Twython ...")

# This loads our app key and app secret from a config file.
with open("config.json") as config_file :
    config = json.load(config_file)

print("... and if you can read this, you have correctly cloned the github repository.")

# This connects our app to the Twitter API.
twitter = Twython(config["app_key"], config["app_secret"], oauth_version=2)
access_token = twitter.obtain_access_token()
twitter = Twython(config["app_key"], access_token=access_token)

# This searches the Twitter API for the keyword 'python'

search_results = twitter.search(q='#htl16_litter', geocode='51.4752006531,-3.1733899117,50km', count='20')

# search_results is now a dictionary that holds a lot of tweets.

#print (json.dumps(search_results['statuses'],indent =4))
for tweet in search_results['statuses'] :
    print('---')
    pics = ''
    try:
        for pic in tweet['entities']['media']:
            pics += pic['media_url'] + ';'
    except KeyError:
        pass
    print(tweet['text'],'\npicture url: ', pics,'\nretweet number:', tweet['retweet_count'],'like number:', tweet['favorite_count'])
    print('geo location:',tweet['geo'], '\nuser location:',tweet['user']['location'])

# Now let's go to the Twitter API documentation and find out how we can format them in a readable way.
