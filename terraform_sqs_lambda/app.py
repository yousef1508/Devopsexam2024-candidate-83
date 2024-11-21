import os
import boto3

# Initialize the SQS client
sqs = boto3.client('sqs')

def lambda_handler(event, context):
    queue_url = os.environ['SQS_QUEUE_URL']
    for record in event['Records']:
        print(f"Message received: {record['body']}")

    return {
        "statusCode": 200,
        "body": "Messages processed successfully."
    }
