import json
import boto3
import os
import uuid

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Fetch bucket name and candidate ID from environment variables
        bucket_name = os.environ['BUCKET_NAME']
        candidate_id = os.environ['CANDIDATE_ID']

        # Parse the input payload
        body = json.loads(event['body'])
        prompt = body.get('prompt', 'Default prompt')

        # Simulate content generation
        generated_content = f"Generated content for prompt: {prompt}"

        # Generate a unique file name
        file_name = f"{candidate_id}/{uuid.uuid4()}.txt"

        # Upload the generated content to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=generated_content
        )

        # Return success response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "File uploaded successfully",
                "file_key": file_name
            })
        }
    except Exception as e:
        # Handle errors and return failure response
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
