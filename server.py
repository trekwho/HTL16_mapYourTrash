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

search_results = twitter.search(q='Ted Cruz', geocode='37.781157,-122.398720,6400km', count='100')
ret = twitter.get_retweets(id='692647161067102208')

# search_results is now a dictionary that holds a lot of tweets.
# now, let's detect emojis with a regular expression:
regexp = re.compile(u'['u'\U0001F300-\U0001F64F'u'\U0001F680-\U0001F6FF'u'\u2600-\u26FF\u2700-\u27BF]+', re.UNICODE)

#print (search_results['statuses'])
for tweet in search_results['statuses'] :
    print('---')
    print(tweet['text'],'\nretweet number:', tweet['retweet_count'],'like number:', tweet['favorite_count'])
    print("EMOJIS DETECTED: " + str(re.findall(regexp, tweet['text'])))
    print(tweet['geo'])

# Now let's go to the Twitter API documentation and find out how we can format them in a readable way.
