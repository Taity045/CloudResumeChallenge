###Useful tutorial on how to do more check out https://fernandomc.com/posts/serverless-testing-with-moto/

### https://stackoverflow.com/questions/48711004/how-to-mock-aws-dynamodb-service


###importing dependencies and setup some environment variables that we’ll want set when these tests are being ru
import boto3
import unittest
import os
from moto import mock_dynamodb2






def aws_credentials():
  # Mocked AWS Credentials for moto
  os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
  os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
  os.environ['AWS_SECURITY_TOKEN'] = 'testing'
  os.environ['AWS_SESSION_TOKEN'] = 'testing'
  os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'



class TestDynamo(unittest.TestCase):

  def setUp(self):
    pass

  @mock_dynamodb2   
  def test_handler(self):
    # Create dynamodb boto3 object
    dynamodb = boto3.client('dynamodb')
    table_name = 'Dev-VisitorsCounterDynamodb-1AKIIFZ6S9KBU'
    dynamodb = boto3.resource('dynamodb','us-east-1')

    # Create mock table
    table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'key',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'key',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    item = {}
    item['key'] = 'value'

    table.put_item(Item=item)

    table = dynamodb.Table(table_name)
    response = table.get_item(
            Key={
                'key': 'value'
            }
        )
    if 'Item' in response:
            item = response['Item']

    self.assertTrue('key' in item)
    self.assertEqual(item['key'], 'value')


if __name__ == '__main__':
  aws_credentials()
  unittest.main()
