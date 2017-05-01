#!/usr/bin/env python

import tweepy

auth = tweepy.OAuthHandler('pLUBsJ8GmtoKQk7nso2EEk9LY', 'sUnWYKnEBwpz45Mfx4YQbcLgIideDcy9NmFiuOKQdARfnOZUF4')
auth.set_access_token('137907618-2FOgxMdI7cbmMB2ticw1PSRjxulc92cpDQAC63AH', 'RGb9ef5GEquPthyLk1m8gFK5101bhMi8P0UpOZR93ercc')

api = tweepy.API(auth)

public_tweets = api.home_timeline(count=200)
for tweet in public_tweets:
    print tweet.text

#user = api.get_user('twitter')
user = api.get_user('H4L9OOO')

print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name

#override tweepy.StreamListener to add logic to on_status
#class MyStreamListener(tweepy.StreamListener):
#
#    def on_status(self, status):
#        print(status.text)
#myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())
#
#myStream.filter(track=['python'])
