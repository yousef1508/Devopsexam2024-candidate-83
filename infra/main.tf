terraform {
  required_version = ">= 1.9.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.74.0"
    }
  }

  backend "s3" {
    bucket         = "pgr301-2024-terraform-state"
    key            = "infra/terraform.tfstate"
    region         = "eu-west-1"
    encrypt        = true
  }
}

provider "aws" {
  region = "eu-west-1"
}

resource "aws_sqs_queue" "image_requests" {
  name                      = "image-generation-queue-cand83"
  visibility_timeout_seconds = 30
}

resource "aws_iam_role" "lambda_execution_role" {
  name = "lambda-sqs-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "lambda_policy" {
  name   = "lambda-sqs-policy"
  role   = aws_iam_role.lambda_execution_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = [
          "sqs:ReceiveMessage",
          "sqs:DeleteMessage",
          "sqs:GetQueueAttributes"
        ]
        Resource = aws_sqs_queue.image_requests.arn
      },
      {
        Effect   = "Allow"
        Action   = "s3:PutObject"
        Resource = "arn:aws:s3:::pgr301-couch-explorers/*"
      },
      {
        Effect   = "Allow"
        Action   = "logs:*"
        Resource = "arn:aws:logs:*:*:*"
      },
      {
        Effect   = "Allow"
        Action   = "bedrock:InvokeModel"
        Resource = "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-image-generator-v1"
      }
    ]
  })
}

resource "aws_lambda_function" "sqs_lambda" {
  filename         = "${path.module}/lambda_sqs.py.zip"
  function_name    = "sqs-image-generator"
  role             = aws_iam_role.lambda_execution_role.arn
  handler          = "lambda_sqs.lambda_handler"
  runtime          = "python3.9"
  timeout          = 30
  memory_size      = 128

environment {
  variables = {
    BUCKET_NAME  = "pgr301-couch-explorers"
    CANDIDATE_ID = "83"
  }
}


  source_code_hash = filebase64sha256("${path.module}/lambda_sqs.py.zip")
}

resource "aws_lambda_event_source_mapping" "sqs_event_source" {
  event_source_arn  = aws_sqs_queue.image_requests.arn
  function_name     = aws_lambda_function.sqs_lambda.arn
  batch_size        = 10
  enabled           = true
}

# SNS Topic for alarm notifications
resource "aws_sns_topic" "sqs_alarm_topic" {
  name = "sqs-alarm-cand83"
}

# Email subscription for the SNS Topic
resource "aws_sns_topic_subscription" "sqs_alarm_email_subscription" {
  topic_arn = aws_sns_topic.sqs_alarm_topic.arn
  protocol  = "email"
  endpoint  = var.alarm_email
}

# CloudWatch alarm for monitoring ApproximateAgeOfOldestMessage
resource "aws_cloudwatch_metric_alarm" "sqs_oldest_message_alarm" {
  alarm_name          = "SQS_OldestMessage_Age_Alarm-cand83"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "ApproximateAgeOfOldestMessage"
  namespace           = "AWS/SQS"
  period              = 
  statistic           = "Average"
  threshold           = var.alarm_threshold  
  alarm_description   = "Triggers if the oldest message in the SQS queue exceeds the defined threshold."
  dimensions = {
    QueueName = aws_sqs_queue.image_requests.name
  }
  alarm_actions = [aws_sns_topic.sqs_alarm_topic.arn]
}
