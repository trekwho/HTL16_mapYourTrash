from twython import Twython
import json
import pandas as pd

# This loads our app key and app secret from a config file.
with open("config.json") as config_file :
    config = json.load(config_file)

# This connects our app to the Twitter API.
twitter = Twython(config["app_key"], config["app_secret"], oauth_version=2)
access_token = twitter.obtain_access_token()
twitter = Twython(config["app_key"], access_token=access_token)

# This searches the Twitter API for the keyword 'python'

search_results = twitter.search(q='#htl16_litter', geocode='51.4752006531,-3.1733899117,50km', count='100')

# search_results is now a dictionary that holds a lot of tweets.

#print (json.dumps(search_results['statuses'],indent =4))

data = {
    'tweet_text':[],
    'picture_url':[],
    'retweet_number':[],
    'like_number':[],
    'location':[]
    }

for tweet in search_results['statuses'] :
    print('---')
    pics = ''
    try:
        for pic in tweet['entities']['media']:
            pics += pic['media_url'] + ';'
    except KeyError:
        pass
    print(tweet['text'],'\npicture url: ', pics,'\nretweet number:', tweet['retweet_count'],'like number:', tweet['favorite_count'])
    print('geo location:',tweet['geo'])
    

    try:
        data['picture_url'].append(tweet['entities']['media'][0]['media_url'])
    except KeyError:
        data['picture_url'].append('none')
    data['tweet_text'].append(tweet['text'])
    data['retweet_number'].append(tweet['retweet_count'])
    data['like_number'].append(tweet['favorite_count'])
    try:
        data['location'].append(tweet['geo']['coordinates'])
    except TypeError:
        data['location'].append('none')
        
df = pd.DataFrame(data,columns=['tweet_text','picture_url','retweet_number','like_number','location'])
df.to_csv('mapTrash_generated.csv')
