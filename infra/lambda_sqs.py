import base64
import boto3
import json
import random
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Initialize AWS clients
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
s3_client = boto3.client("s3")

# Environment variables
MODEL_ID = "amazon.titan-image-generator-v1"
BUCKET_NAME = os.environ.get("BUCKET_NAME")
CANDIDATE_ID = os.environ.get("CANDIDATE_ID", "default")

# Validate environment variables
if not BUCKET_NAME:
    raise ValueError("Environment variable 'BUCKET_NAME' must be set.")
if not CANDIDATE_ID:
    raise ValueError("Environment variable 'CANDIDATE_ID' must be set.")

def lambda_handler(event, context):
    logger.info("Lambda handler started.")
    processed_records = 0

    for record in event["Records"]:
        try:
            # Extract the SQS message body
            prompt = record["body"]
            logger.info(f"Processing prompt: {prompt}")

            # Generate a unique seed and S3 image path
            seed = random.randint(0, 2147483647)
            s3_image_path = f"{CANDIDATE_ID}/images/titan_{seed}.png"
            logger.info(f"Generated S3 path: {s3_image_path}")

            # Prepare the Bedrock request payload
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

            # Invoke the Bedrock model
            response = bedrock_client.invoke_model(
                modelId=MODEL_ID,
                body=json.dumps(native_request)
            )
            logger.info("Model invoked successfully.")

            # Parse and validate the response
            model_response = json.loads(response["body"].read())
            images = model_response.get("images", [])
            if not images:
                logger.error("No images returned by the model.")
                continue

            # Decode the image and upload to S3
            base64_image_data = images[0]
            image_data = base64.b64decode(base64_image_data)
            s3_client.put_object(Bucket=BUCKET_NAME, Key=s3_image_path, Body=image_data)
            logger.info(f"Image uploaded to S3: {s3_image_path}")

            processed_records += 1

        except Exception as e:
            logger.error(f"Error processing record: {e}", exc_info=True)

    logger.info(f"Lambda handler completed. Processed {processed_records} record(s).")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Processed {processed_records} record(s)."})
    }

