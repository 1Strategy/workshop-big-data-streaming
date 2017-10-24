"""Producer

Generates and puts data into an Amazon Kinesis Stream
"""


from __future__ import print_function
from pprint import pprint
from io import BytesIO, StringIO
from gzip import GzipFile
import random
import base64
import json
import os
import string
import time
import boto3
from botocore.exceptions import ProfileNotFound

PROFILE     = "training"
STREAM_NAME = "test-stream-death-star"
BATCH_SIZE  = 1


try:
    SESSION       = boto3.session.Session(profile_name=PROFILE)
    CREDS         = SESSION.get_credentials()
    ACCESS_KEY    = CREDS.access_key
    SECRET_KEY    = CREDS.secret_key
    SESSION_TOKEN = CREDS.token
    FIREHOSE      = SESSION.client('firehose', region_name='us-west-2')

except ProfileNotFound as pnf:
    SESSION       = boto3.session.Session()
    ACCESS_KEY    = os.environ.get('AWS_ACCESS_KEY_ID')
    SECRET_KEY    = os.environ.get('AWS_SECRET_ACCESS_KEY')
    SESSION_TOKEN = os.environ.get('AWS_SESSION_TOKEN')
    REGION        = os.environ.get('AWS_REGION')
    STREAM_NAME   = os.environ.get('STREAM_NAME')
    BATCH_SIZE    = os.environ.get('BATCH_SIZE')
    FIREHOSE      = SESSION.client('firehose', region_name=REGION)


def generateLifeSupportData():
    """Create a node with demographic attributes
    """

    # use distributions
    node              = {}
    node["Name"]      = random.choice(string.ascii_uppercase)
    node["Temp"]      = random.randint(18, 23) # C
    node["Oxygen"]    = random.randint(0, 100)
    node["Humidity"]  = random.randint(40, 60)
    node["Pressure"]  = random.randint(0, 100)
    node["Radiation"] = random.randint(0, 100) # cpm
    node["Gravity"]   = random.randint(0, 100)
    # node["Humanoids"] = random.randint(0, 10)
    # node["Droids"]    = random.randint(0, 5)
    node["Timestamp"] = int(round(time.time() * 1000))


    return json.dumps(node)


def compressFileToString(inputFile):
    """
    read the given open file, compress the data and return it as a string.
    """
    stream = BytesIO()
    print(stream)
    compressor = GzipFile(fileobj=stream, mode='w')
    readable = BytesIO(inputFile)
    print(readable)
    # while True:
    #     chunk = inputFile.read(8192)
    #     if not chunk:
    #         compressor.close()
    #         return stream.getvalue()
    #     compressor.write(chunk)


def streamData():
    """Stream data to Kinesis Firehose
    """
    for i in range(BATCH_SIZE):
        room = generateLifeSupportData()
        # partition = int(person.get("age")) // 10
        # part_string = "partition-{part}".format(part=str(partition))
        room_file = StringIO(json.dumps(room))
        # compressed_file = compressFileToString(json.dumps(room))
        # response = FIREHOSE.put_record(
        #     DeliveryStreamName=STREAM_NAME,
        #     Record={"Data": room_file.getvalue()}
        # )
        print("PUT: " + json.loads(room).get("Name"))
        pprint(json.loads(room))
        room_bytes = base64.b64encode(room.encode("ascii"))
        print(type(room_bytes))
        print(type(room))
        print(base64.b64encode(room.encode('ascii')))


def lambda_handler(event, context):
    """this is the handler function
    """
    streamData()


if __name__ == '__main__':
    lambda_handler({}, {})