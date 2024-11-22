output "sqs_queue_url" {
  value = aws_sqs_queue.image_gen_queue.id
}

output "lambda_function_arn" {
  value = aws_lambda_function.image_gen_lambda.arn
}
