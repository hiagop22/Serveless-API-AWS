output "image_id" {
  value = data.aws_ecr_image.latest.id
}

output "repo_url" {
  value = local.repo_url
}

output "repo_name" {
  value = aws_ecr_repository.api.name
}

output "image_tags" {
  value = local.image_tags
}

output "repo_arn" {
  value = aws_ecr_repository.api.arn
}