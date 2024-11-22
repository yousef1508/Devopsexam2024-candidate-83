import base64
import boto3
import json
import random
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize AWS clients
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
s3_client = boto3.client("s3")

# Environment variables
MODEL_ID = "amazon.titan-image-generator-v1"
BUCKET_NAME = os.environ.get("BUCKET_NAME")
candidate_id = os.environ.get("CANDIDATE_ID", "default")

# Validate environment variables
if not BUCKET_NAME:
    raise ValueError("Environment variable 'BUCKET_NAME' must be set")
if not candidate_id:
    raise ValueError("Environment variable 'CANDIDATE_ID' must be set")

def lambda_handler(event, context):
    for record in event["Records"]:
        try:
            # Extract the SQS message body
            prompt = record["body"]
            logging.info(f"Processing prompt: {prompt}")
            
            seed = random.randint(0, 2147483647)
            s3_image_path = f"{candidate_id}/images/titan_{seed}.png"

            # Prepare the request for image generation
            native_request = {
                "taskType": "TEXT_IMAGE",
                "textToImageParams": {"text": prompt},
                "imageGenerationConfig": {
                    "numberOfImages": 1,
                    "quality": "standard",
                    "cfgScale": 8.0,
                    "height": 512,
                    "width": 512,
                    "seed": seed,
                },
            }

            # Invoke the model
            response = bedrock_client.invoke_model(
                modelId=MODEL_ID,
                body=json.dumps(native_request)
            )

            # Validate response
            model_response = json.loads(response["body"].read())
            if "images" not in model_response or not model_response["images"]:
                logging.error("No images returned by the model")
                continue

            base64_image_data = model_response["images"][0]
            image_data = base64.b64decode(base64_image_data)

            # Upload the image to S3
            s3_client.put_object(Bucket=BUCKET_NAME, Key=s3_image_path, Body=image_data)
            logging.info(f"Uploaded to S3: {s3_image_path}")

        except Exception as e:
            logging.error(f"Error processing record: {e}")

    return {
        "statusCode": 200,
        "body": json.dumps("Processing completed.")
    }
