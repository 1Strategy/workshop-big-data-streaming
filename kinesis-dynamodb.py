#!/usr/bin/env python

import boto3
import time
import json
import decimal

## script to read data from Kinesis, extract hashtags and store into dynamoDB
#Connent to the kinesis stream
inuser = boto3.session.Session(profile_name='default')
kinesis = inuser.client("kinesis")
shard_id = 'shardId-000000000000' #only one shard
shard_it = kinesis.get_shard_iterator(StreamName="test-twitter-stream", ShardId=shard_id, ShardIteratorType="LATEST")["ShardIterator"]


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hashtags')

while 1==1:
    out = kinesis.get_records(ShardIterator=shard_it, Limit=100)
    for record in out['Records']:
        if 'entities' in json.loads(record['Data']):
            htags = json.loads(record['Data'])['entities']['hashtags']
            if htags:
                 for ht in htags:
                    htag = ht['text']
                    checkItemExists = table.get_item(
                        Key={
                            'hashtag':htag
                        }
                    )
                    if 'Item' in checkItemExists:
                        response = table.update_item(
                            Key={
                                'hashtag': htag
                            },
                            UpdateExpression="set htCount  = htCount + :val",
                            ConditionExpression="attribute_exists(hashtag)",
                            ExpressionAttributeValues={
                                ':val': decimal.Decimal(1)
                            },
                            ReturnValues="UPDATED_NEW"
                        )
                    else:
                        response = table.update_item(
                            Key={
                                'hashtag': htag
                            },
                            UpdateExpression="set htCount = :val",
                            ExpressionAttributeValues={
                                ':val': decimal.Decimal(1)
                            },
                            ReturnValues="UPDATED_NEW"
                        )
    shard_it = out["NextShardIterator"]
    time.sleep(1.0)
