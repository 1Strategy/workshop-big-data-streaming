#!/usr/bin/env python

import tweepy

auth = tweepy.OAuthHandler('pLUBsJ8GmtoKQk7nso2EEk9LY', 'sUnWYKnEBwpz45Mfx4YQbcLgIideDcy9NmFiuOKQdARfnOZUF4')
auth.set_access_token('137907618-2FOgxMdI7cbmMB2ticw1PSRjxulc92cpDQAC63AH', 'RGb9ef5GEquPthyLk1m8gFK5101bhMi8P0UpOZR93ercc')

api = tweepy.API(auth)


