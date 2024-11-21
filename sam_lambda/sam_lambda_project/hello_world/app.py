import json
import boto3
import os
import uuid
import logging

# Initialize the logger
logging.basicConfig(level=logging.INFO)

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Log the incoming event for debugging
        logging.info(f"Received event: {json.dumps(event)}")

        # Fetch bucket name and candidate ID from environment variables
        bucket_name = os.environ.get('BUCKET_NAME')
        candidate_id = os.environ.get('CANDIDATE_ID')

        if not bucket_name or not candidate_id:
            raise ValueError("Environment variables 'BUCKET_NAME' or 'CANDIDATE_ID' are not set")

        # Parse the input payload
        if 'body' not in event or not event['body']:
            raise ValueError("Missing or empty 'body' in the event")

        try:
            body = json.loads(event['body'])
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in the 'body' of the event")

        prompt = body.get('prompt', 'Default prompt')

        # Simulate content generation
        generated_content = f"Generated content for prompt: {prompt}"
        logging.info(f"Generated content: {generated_content}")

        # Generate a unique file name
        file_name = f"{candidate_id}/{uuid.uuid4()}.txt"
        logging.info(f"Generated file name: {file_name}")

        # Upload the generated content to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=generated_content
        )
        logging.info("File successfully uploaded to S3")

        # Return success response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "File uploaded successfully",
                "file_key": file_name
            })
        }
    except Exception as e:
        # Log the error for debugging
        logging.error(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
