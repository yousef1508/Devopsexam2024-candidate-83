import base64
import boto3
import json
import os
import random
import logging

# Initialize the logger
logging.basicConfig(level=logging.INFO)

# Initialize AWS clients
s3_client = boto3.client("s3")
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

def lambda_handler(event, context):
    try:
        # Parse and validate the request body
        body = json.loads(event.get("body", "{}"))
        prompt = body.get("prompt")
        if not prompt:
            raise ValueError("Missing 'prompt' in the request body.")
        logging.info("Prompt received: %s", prompt)

        # Fetch bucket name and candidate ID from environment variables
        bucket_name = os.environ.get("BUCKET_NAME")
        candidate_id = os.environ.get("CANDIDATE_ID")
        if not bucket_name or not candidate_id:
            raise ValueError("Environment variables 'BUCKET_NAME' or 'CANDIDATE_ID' are not set.")

        # Generate random seed and S3 image path
        seed = random.randint(0, 2147483647)
        s3_image_path = f"{candidate_id}/generated_images/titan_{seed}.png"
        logging.info("Generated image with seed %s and S3 path %s", seed, s3_image_path)

        # Construct the Bedrock model request
        native_request = {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {"text": prompt},
            "imageGenerationConfig": {
                "numberOfImages": 1,
                "quality": "standard",
                "cfgScale": 8.0,
                "height": 1024,
                "width": 1024,
                "seed": seed,
            },
        }

        # Call the Bedrock model
        response = bedrock_client.invoke_model(
            modelId="amazon.titan-image-generator-v1", 
            body=json.dumps(native_request)
        )
        model_response = json.loads(response["body"].read())

        # Decode the Base64 image data
        image_data = base64.b64decode(model_response["images"][0])

        # Upload the decoded image to S3
        s3_client.put_object(
            Bucket=bucket_name, 
            Key=s3_image_path, 
            Body=image_data, 
            ContentType="image/png"
        )
        logging.info("Image successfully uploaded to S3.")

        # Return success response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Image generated and uploaded successfully.",
                "file_key": s3_image_path,
            }),
        }

    except Exception as e:
        logging.error("Error occurred", exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }
