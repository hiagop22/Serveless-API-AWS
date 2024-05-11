terraform {
  required_version = "1.7.1"
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

module "s3" {
  source      = "./s3"
  bucket_name = var.bucket_name
  stage       = terraform.workspace
}


module "dynamo" {
  source     = "./dynamo"
  table_name = var.table_name
}