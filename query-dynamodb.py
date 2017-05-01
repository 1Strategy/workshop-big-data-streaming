#!/usr/bin/env python
import boto3
from boto3.dynamodb.conditions import Key, Attr
import json

inuser = boto3.session.Session(profile_name='default')
dynamodb = inuser.resource('dynamodb')
table = dynamodb.Table('hashtags')
#print(table.creation_date_time)
response = table.scan(
    FilterExpression=Attr('htCount').gt(100)
)
items = response['Items']
#print items[0]['hashtag']
for i in items:
    print i['hashtag'], i['htCount']
