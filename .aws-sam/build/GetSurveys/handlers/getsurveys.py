import json
import boto3 as boto

def getsurveys(event, context):
    dynamodb = boto.resource('dynamodb')
    dynamodb_table = dynamodb.Table('GatorPolls-Survey-1QPWM07UFY0N2')
    response = dynamodb_table.scan()
    
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'body': json.dumps(response['Items'])
    }