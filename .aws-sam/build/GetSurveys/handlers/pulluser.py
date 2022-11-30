import json
import boto3 as boto

def pulluser(event, context):
    
    pathParams = event['pathParameters']
    user = pathParams['user']
    
    dynamodb = boto.resource('dynamodb')
    dynamodb_table = dynamodb.Table('GatorPolls-Votes-1ATO3SY11B772')
    response = dynamodb_table.scan()
    output = {}
    for response in response['Items']:
        if user in response:
            output[response['name']] = response[user]
    
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'body': json.dumps(output)
    }