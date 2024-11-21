resource "aws_sqs_queue" "example_queue" {
  name = "pgr301-couch-explorers-queue-83"
  visibility_timeout_seconds = 30
}

resource "aws_iam_role" "lambda_execution_role" {
  name = "lambda_execution_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "sts:AssumeRole"
        Effect    = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "lambda_sqs_policy" {
  name   = "lambda_sqs_policy"
  role   = aws_iam_role.lambda_execution_role.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = "sqs:ReceiveMessage"
        Effect   = "Allow"
        Resource = aws_sqs_queue.example_queue.arn
      },
      {
        Action   = "sqs:DeleteMessage"
        Effect   = "Allow"
        Resource = aws_sqs_queue.example_queue.arn
      },
      {
        Action   = "sqs:GetQueueAttributes" # Added permission
        Effect   = "Allow"
        Resource = aws_sqs_queue.example_queue.arn
      }
    ]
  })
}

resource "aws_lambda_function" "sqs_processor" {
  filename         = "sqs_lambda.zip" # Replace with your zipped Lambda function
  function_name     = "process_sqs_messages_83"
  handler          = "app.lambda_handler"
  runtime          = "python3.9"
  role             = aws_iam_role.lambda_execution_role.arn

  environment {
    variables = {
      SQS_QUEUE_URL = aws_sqs_queue.example_queue.id
    }
  }
}

resource "aws_lambda_event_source_mapping" "sqs_to_lambda" {
  event_source_arn = aws_sqs_queue.example_queue.arn
  function_name    = aws_lambda_function.sqs_processor.arn
  batch_size       = 5
}


# This is a test branch for Terraform workflow logic
