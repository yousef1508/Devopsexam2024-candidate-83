output "sqs_queue_url" {
  value = aws_sqs_queue.example_queue.id
}

output "lambda_function_arn" {
  value = aws_lambda_function.sqs_processor.arn
}
