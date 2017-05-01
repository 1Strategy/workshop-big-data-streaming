#!/usr/bin/env python
import boto3

#Create Kinesis stream and shards
inuser = boto3.session.Session(profile_name='default')
client = inuser.client('kinesis')
response = client.create_stream(
   StreamName='test-twitter-stream',
   ShardCount=1
)
