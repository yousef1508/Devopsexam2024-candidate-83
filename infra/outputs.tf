output "sqs_queue_url" {
  description = "The URL of the SQS queue"
  value       = aws_sqs_queue.image_requests.url
}

output "sqs_queue_arn" {
  description = "The ARN of the SQS queue"
  value       = aws_sqs_queue.image_requests.arn
}

output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = aws_lambda_function.sqs_lambda.function_name
}
