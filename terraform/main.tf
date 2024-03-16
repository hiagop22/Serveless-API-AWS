terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws",
      version = "5.17.0"
    }
  }
}

provider "aws" {
  profile = var.aws_profile
  region  = var.aws_region
}

module "ecr" {
  source      = "./ecr"
  environment = terraform.workspace
  region = "us-east-1"
}

module "iam" {
  source      = "./iam"
  environment = terraform.workspace
}

module "lambda" {
  source       = "./lambda"
  environment  = terraform.workspace
  arn_role     = module.iam.api_role_arn
  ecr_id       = module.ecr.ecr_id
  ecr_repo_url = module.ecr.repo_url
}

output "api_url" {
  value = module.lambda.api_url
}

output "ecr_repo_url" {
  value = module.ecr.repo_url
}

output "image_tags" {
  value = module.ecr.image_tags
}