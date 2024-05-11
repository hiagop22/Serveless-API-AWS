output "api_url" {
  value = aws_lambda_function_url.api.function_url
}

output "api_arn" {
  value = aws_lambda_function.api.arn
}

output "name" {
  value = aws_lambda_function.api.function_name
}