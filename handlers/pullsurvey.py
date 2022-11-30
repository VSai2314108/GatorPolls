import json
import boto3 as boto

def pullsurvey(event, context):
    pathParams = event['pathParameters']
    name = pathParams['name']
    
    dynamodb = boto.resource('dynamodb')
    dynamodb_table = dynamodb.Table('GatorPolls-Votes-1ATO3SY11B772')
    response = dynamodb_table.scan()

    for element in response['Items']:
        if element['name'] == name:
            return {
                'statusCode': 200,
                'headers': {
                    "Access-Control-Allow-Headers" : "*",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*"
                },
                'body': json.dumps(element)
            } 
            
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'body': 'No survey found'
    }
    