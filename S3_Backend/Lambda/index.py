import boto3
import os
import json

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('webapp-VisitorsCounterDynamodb-1M59HDBZZITER')  # Update this line

    try:
        res = table.update_item(
            Key={"id": "numberofVisitors"},
            UpdateExpression="SET Site = Site + :inc",
            ExpressionAttributeValues={':inc': 1},
            ReturnValues="UPDATED_NEW"
        )

        print("Item updated successfully")
        print(res)

        responseBody = json.dumps({"numberofVisitors": int(float(res["Attributes"]["Site"]))})
        statusCode = 200

    except Exception as e:
        print(f"Error updating item: {e}")
        responseBody = json.dumps({"error": "Could not update item"})
        statusCode = 500

    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": statusCode,
        "body": responseBody,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS"
        },
    }

    return apiResponse





  
