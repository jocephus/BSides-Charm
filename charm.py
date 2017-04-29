from twitter_keys import *
 
import json
import requests
import time
import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
#
# Download Tweets from a user profile
#
def download_tweets(screen_name, number_of_tweets, exclude_replies):
 
    api_url  = '%s/statuses/user_timeline.json' % base_twitter_url
 
    params  = {
        'screen_name':  screen_name,
        'count':        number_of_tweets,
	'replies':	exclude_replies,
    }
 
    # send request to Twitter
    response = requests.get(api_url, params=params, auth=oauth)
 
    if response.status_code == 200:
 
        tweets = json.loads(response.content)
 
        return tweets
 
    return None
 
 
# get a list of Tweets
tweet_list = download_tweets('bsidescharm', 150, 'true')
 
if tweet_list is not None:
 
    # loop over each Tweet and print the date and text
    for tweet in tweet_list:
 
        print ('%s : %s' % (tweet['created_at'], tweet['text']))
 
else:
 
    print '[*] No Tweets retrieved.'
