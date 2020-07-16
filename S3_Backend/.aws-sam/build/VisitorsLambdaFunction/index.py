import boto3
import os
import json


def lambda_handler(event, context):
  
  dynamodb = boto3.resource('dynamodb')

  table = dynamodb.Table('Dev-VisitorsCounterDynamodb-1AKIIFZ6S9KBU')

  res = table.update_item(
    Key={"id": "numberofVisitors"},
    UpdateExpression="ADD Site :inc",
    ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues="UPDATED_NEW"
    )

#   print("UPDATING ITEM")
#   print(res)

    # Format dynamodb response into variable
  responseBody = json.dumps({"numberofVisitors": int(float(res["Attributes"]["Site"]))})

   #API Response Object And Format To JSON
  apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS" 
        },
    }

    # Return API Response
  return apiResponse




  