import boto3

try:
    session = boto3.session.Session(profile_name='sandbox')
except Exception:
    session = boto3.session.Session()


def lambda_handler(event, context):
    event_type = event.get('detail').get('eventName', None)
    shard_count = event.get('detail').get('requestParameters').get('shardCount', None)
    stream_name = event.get('detail').get('requestParameters').get('streamName', None)

    if event_type is None or shard_count is None or stream_name is None:
        raise ValueError('The event payload is invalid')

    if event_type == 'CreateStream' and shard_count > 1:
        kinesis_client = session.client('kinesis', event.get('region'))
        kinesis_client.delete_stream(StreamName=stream_name)
        print('{stream} was automatically deleted for having too many shards'.format(stream=stream_name))
    else:
        print('potato')



if __name__ == '__main__':
    event = {
    	"version": "0",
    	"id": "97e60097-2aab-4a94-8ae1-76ee99ce19fe",
    	"detail-type": "AWS API Call via CloudTrail",
    	"source": "aws.kinesis",
    	"account": "842337631775",
    	"time": "2017-04-28T18:15:21Z",
    	"region": "us-west-2",
    	"resources": [],
    	"detail": {
    		"eventVersion": "1.04",
    		"userIdentity": {
    			"type": "AssumedRole",
    			"principalId": "AROAJ4LHD2ZAYD3ARYX4K:justiniravani",
    			"arn": "arn:aws:sts::842337631775:assumed-role/1S-Admins/justiniravani",
    			"accountId": "842337631775",
    			"accessKeyId": "ASIAIPQUV73FYKBU7JBA",
    			"sessionContext": {
    				"attributes": {
    					"mfaAuthenticated": "true",
    					"creationDate": "2017-04-28T18:10:02Z"
    				},
    				"sessionIssuer": {
    					"type": "Role",
    					"principalId": "AROAJ4LHD2ZAYD3ARYX4K",
    					"arn": "arn:aws:iam::842337631775:role/1S-Admins",
    					"accountId": "842337631775",
    					"userName": "1S-Admins"
    				}
    			}
    		},
    		"eventTime": "2017-04-28T18:15:21Z",
    		"eventSource": "kinesis.amazonaws.com",
    		"eventName": "CreateStream",
    		"awsRegion": "us-west-2",
    		"sourceIPAddress": "96.82.242.226",
    		"userAgent": "console.amazonaws.com",
    		"requestParameters": {
    			"shardCount": 2,
    			"streamName": "jiravani-stream"
    		},
    		"responseElements": None,
    		"requestID": "ec51b6ed-5e98-55b8-bd2c-3e14fe4d56e4",
    		"eventID": "fc907380-f9bf-455a-a3f5-2c1781fe70cc",
    		"eventType": "AwsApiCall"
    	}
    }


    lambda_handler(event, {})
