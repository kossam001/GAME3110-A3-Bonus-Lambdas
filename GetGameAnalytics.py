import json
import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    
    db = boto3.resource("dynamodb")
    table = db.Table("GameAnalytics")
    
    if 'body' in event:
        data = json.loads(event['body'])
    
        response = table.scan(
            FilterExpression=Attr('login_date').gt(data["login_date_start"]) &
                Attr('login_date').lt(data["login_date_end"]) &
                Attr('login_time').gt(data["login_time_start"]) &
                Attr('login_time').lt(data["login_time_end"]) &
                Attr('user_id').eq(data["user_id"])
        )
        
        items = response['Items']
        
        returnResponse = {}
        returnResponse["Query"] = event['body']
        returnResponse["Items"] = items
        
        return {
            'statusCode': 200,
            'body': json.dumps(returnResponse)
        }

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }