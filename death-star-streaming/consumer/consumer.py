#!env python
"""Consumer

Pulls data from an Amazon Kinesis Stream
"""


from __future__ import print_function  # Python 2/3 compatibility
from pprint import pprint
from amazon_kclpy import kcl
import json
import base64
import boto3
import testdata
from botocore.exceptions import ProfileNotFound

try:
    SESSION = boto3.session.Session(profile_name='training')
except ProfileNotFound as pnf:
    SESSION = boto3.session.Session()


class RecordProcessor(kcl.RecordProcessorBase):

    def initialize(self, shard_id):
        pass

    def process_records(self, records, checkpointer):
        pass

    def shutdown(self, checkpointer, reason):
        pass


kinesis = session.client('kinesis')

response = kinesis.describe_stream(StreamName="TestStreamBeta")

pprint(response)

again = kinesis.get_shard_iterator(StreamName="TestStreamBeta",
                ShardId="shardId-000000000000",
                ShardIteratorType="LATEST")

iter = str(again.get("ShardIterator"))

pprint(again)

# item = kinesis.get_records(ShardIterator=iter)

# pprint(item)

if __name__ == "__main__":
    kclprocess = kcl.KCLProcess(RecordProcessor())
    kclprocess.run()