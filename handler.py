import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

import boto3
import json
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('profile')
def newpost(event, context):
    table.put_item(Item=event)
    body= {"message":"it was created successfully"}
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
