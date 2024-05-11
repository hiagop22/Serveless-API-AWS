resource "aws_ecr_repository" "api" {
  name                 = "lambda-tf-ai-api-${var.environment}"
  image_tag_mutability = "MUTABLE"
  force_delete         = true

  image_scanning_configuration {
    scan_on_push = true
  }
}

data "external" "image_tags" {
  program = [
    "aws", "ecr", "describe-images", "--region", "${var.region}",
    "--repository-name", aws_ecr_repository.api.name,
    "--query", "{\"tags\": to_string(sort_by(imageDetails,& imagePushedAt)[*].imageTags[0])}",
  ]
}

resource "aws_ecr_lifecycle_policy" "policy" {
  repository = aws_ecr_repository.api.name

  policy = jsonencode({
    rules = [{
      "rulePriority" : 1,
      "description" : "Expire untagged images older than 1 day",
      "selection" : {
        "tagStatus" : "untagged",
        "countType" : "sinceImagePushed",
        "countUnit" : "days",
        "countNumber" : 1
      },
      "action" : {
        "type" : "expire"
      }
    }]
  })

}