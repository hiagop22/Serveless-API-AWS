output "ecr_id" {
  value = data.aws_ecr_image.latest.id
}

output "repo_url" {
  value = local.repo_url
}

output "image_tags" {
  value = local.image_tags
}