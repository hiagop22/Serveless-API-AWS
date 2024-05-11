terraform {
  required_version = "1.7.1"

  required_providers {
    aws = {
      source  = "hashicorp/aws",
      version = "5.17.0"
    }
  }


  backend "s3" {
    bucket         = "test-cicd-tf-ai-api-state"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "test-cicd-tf-ai-api-state"
  }
}

provider "aws" {
  profile = var.aws_profile
  region  = var.aws_region
}


module "ecr" {
  source      = "./ecr"
  environment = terraform.workspace
  region      = "us-east-1"
}

module "iam" {
  source      = "./iam"
  environment = terraform.workspace
}

module "lambda" {
  source       = "./lambda"
  environment  = terraform.workspace
  arn_role     = module.iam.api_role_arn
  image_id     = module.ecr.image_id
  ecr_repo_url = module.ecr.repo_url
}

module "artifact_store" {
  source      = "./bucket"
  bucket_name = "my-bucket-artifacts-cicd"
  expiration  = true
}

module "codepipeline" {
  source = "./codepipeline"
  # dockerhub_credentials          = var.dockerhub_credentials
  codestar_connector_credentials = var.codestar_connector_credentials
  bucket_artifact_id             = module.artifact_store.bucket_id
  respository_id                 = "hiagop22/Serveless-API-AWS"
  branch                         = "master"
  account_id                     = local.account_id
  ecr_repo_name                  = module.ecr.repo_name
  lambda_name                    = module.lambda.name
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