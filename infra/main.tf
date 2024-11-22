resource "aws_sqs_queue" "image_gen_queue" {
  name                      = "image-gen-queue-83"
  visibility_timeout_seconds = 90
}

resource "aws_iam_role" "lambda_execution_role" {
  name = "image-gen-lambda-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action    = "sts:AssumeRole",
        Effect    = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy" "lambda_policy" {
  name        = "image-gen-lambda-policy"
  description = "Policy for Lambda to access SQS, S3, and Bedrock"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = ["sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueAttributes"],
        Resource = aws_sqs_queue.image_gen_queue.arn
      },
      {
        Effect   = "Allow",
        Action   = ["s3:PutObject"],
        Resource = "arn:aws:s3:::pgr301-couch-explorers/*"
      },
      {
        Effect   = "Allow",
        Action   = ["bedrock:InvokeModel"],
        Resource = "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-image-generator-v1"
      },
      {
        Effect   = "Allow",
        Action   = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
        Resource = "arn:aws:logs:*:*:*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  role       = aws_iam_role.lambda_execution_role.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}

resource "aws_lambda_function" "image_gen_lambda" {
  filename         = "lambda.zip" # Replace with your zipped Lambda function
  function_name    = "image-gen-lambda-83"
  role             = aws_iam_role.lambda_execution_role.arn
  handler          = "lambda_sqs.lambda_handler"
  runtime          = "python3.9"
  timeout          = 60  # Adjusted for image generation
  memory_size      = 512

  environment {
    variables = {
      BUCKET_NAME      = "pgr301-couch-explorers"
      CANDIDATE_NUMBER = "83"
    }
  }

  source_code_hash = filebase64sha256("sqs_lambda.zip")
}

resource "aws_lambda_event_source_mapping" "lambda_sqs" {
  event_source_arn  = aws_sqs_queue.image_gen_queue.arn
  function_name     = aws_lambda_function.image_gen_lambda.arn
  batch_size        = 10
  enabled           = true
}
