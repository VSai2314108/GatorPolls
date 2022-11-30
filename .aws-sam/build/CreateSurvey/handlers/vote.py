import json
import boto3 as boto

def vote(event, context):
    
    params = event['pathParameters']  

    body = event['body']
    questions = json.loads(body)
    
    dynamodb = boto.resource('dynamodb')
    # connect to survey table
    dynamodb_table = dynamodb.Table('GatorPolls-Votes-1ATO3SY11B772')
    # push questions to survey table
    try:
        response = dynamodb_table.update_item(
            Key={
                'name': params['name']
            },
            UpdateExpression="set " + params['user'] + " = :vote",
            ExpressionAttributeValues={
                ':vote': questions
            },
            ReturnValues="UPDATED_NEW"
        )
    except Exception as e:
        return {
        'statusCode': 400,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'body': json.dumps(e)
    }

    """
    pathParameters = {
        name: name of the survey,
        user: user name,
    }
    
    body = {
        vote: {
            user1: q1 answer,
            ...
            user5: q5 answer,
        }
    }
    """
    
    return {
        'statusCode': 201,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'body': json.dumps(response['Attributes'])
    }