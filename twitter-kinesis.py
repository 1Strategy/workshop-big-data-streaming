#!/usr/bin/env python
from TwitterAPI import TwitterAPI
import boto3
import json
import twitterCreds

## twitter credentials

consumer_key = twitterCreds.consumer_key
consumer_secret = twitterCreds.consumer_secret
access_token_key = twitterCreds.access_token_key
access_token_secret = twitterCreds.access_token_secret

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

inuser = boto3.session.Session(profile_name='default')
kinesis = inuser.client('kinesis')

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})

for item in r:
    kinesis.put_record(StreamName="test-twitter-stream", Data=json.dumps(item), PartitionKey="filler")
    print json.dumps(item, indent=2)

# Use below if you have multiple shards
# kinesis.put_record(StreamName="twitter",
#  Data=json.dumps(item),
#  PartitionKey=str(item["zip_code"])
