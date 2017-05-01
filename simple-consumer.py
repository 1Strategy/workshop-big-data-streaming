#!/usr/bin/env python
import boto3
import time
import json

inuser = boto3.session.Session(profile_name='default')
kinesis = inuser.client("kinesis")
shard_id = "shardId-000000000000" #only one shard!
pre_shard_it = kinesis.get_shard_iterator(StreamName="test-twitter-stream", ShardId=shard_id, ShardIteratorType="LATEST")
shard_it = pre_shard_it["ShardIterator"]
while 1==1:
     out = kinesis.get_records(ShardIterator=shard_it, Limit=1)
     shard_it = out["NextShardIterator"]
     print json.dumps(out, indent=2);
     time.sleep(1.0)
