resource "aws_lambda_function" "api" {
  function_name = "lambda-tf-ai-api-${var.environment}"

  role             = var.arn_role
  image_uri        = "${var.ecr_repo_url}:latest"
  package_type     = "Image"
  source_code_hash = trimprefix(var.ecr_id, "sha256:")
  timeout          = 10

  environment {
    variables = {}
  }
}

resource "aws_lambda_function_url" "api" {
  function_name      = aws_lambda_function.api.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = true
    allow_origins     = ["*"]
    allow_methods     = ["*"]
    allow_headers     = ["date", "keep-alive"]
    expose_headers    = ["keep-alive", "date"]
    max_age           = 86400
  }
}