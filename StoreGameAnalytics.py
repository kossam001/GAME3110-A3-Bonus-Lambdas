import json
import boto3
import decimal

def lambda_handler(event, context):
    
    db = boto3.resource("dynamodb")
    table = db.Table("GameAnalytics")
    
    if 'body' in event:
        data = json.loads(event['body'])
    
    table.put_item(
        Item=data
    )
        
    return {
        'statusCode': 200,
        'body': json.dumps(event['body'])
    }