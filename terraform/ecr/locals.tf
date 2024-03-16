locals {
  repo_url = aws_ecr_repository.api.repository_url
  image_tags = jsondecode(data.external.image_tags.result.tags)
}

resource "null_resource" "image" {
  # CAUTION with blank space before "Dockerfile"
  # Use "Dockerfile" instead of " Dockerfile"
  triggers = {
    hash = md5(join("-", [for x in fileset("", "${path.module}/../../app/{*.py,Dockerfile}") : filemd5(x)]))
  }

  provisioner "local-exec" {
    command = <<EOF
      aws ecr get-login-password --region ${var.region} | docker login --username AWS --password-stdin ${local.repo_url}
      docker build --platform linux/amd64 -t ${local.repo_url}:latest ${path.module}/../../app
      docker push ${local.repo_url}:latest
    EOF
  }
}

data "aws_ecr_image" "latest" {
  repository_name = aws_ecr_repository.api.name
  image_tag       = "latest"
  depends_on      = [null_resource.image]
}