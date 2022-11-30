import json
import boto3 as boto

def create(event, context):
    body = event['body']
    questions = json.loads(body)
    
    dynamodb = boto.resource('dynamodb')
    # connect to survey table
    dynamodb_table = dynamodb.Table('GatorPolls-Survey-1QPWM07UFY0N2')
    dynamodb_table2 = dynamodb.Table('GatorPolls-Votes-1ATO3SY11B772')
    # push questions to survey table
    response = dynamodb_table.put_item(Item = questions)
    print(response)
    response2 = dynamodb_table2.put_item(Item = {'name': questions['name']})
    print(response2)

    """
    Item = {
        name: name of the survey,
        q1: question 1,
        ...
        q5: question 5,
    }
    """
    
    return {
        'statusCode': 201,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'body': "Survey named " + questions['name'] + " created successfully. Survey: " + response.HttpStatusCode + " Votes: " + response2.HttpStatusCode
    }