# variable "dockerhub_credentials" {
#   type = string
# }

variable "codestar_connector_credentials" {
  type = string
}

variable "bucket_artifact_id" {
  type = string
}

variable "branch" {
  type = string
}

variable "respository_id" {
  type        = string
  description = "user/project-name"
}

variable "account_id" {
  type = string
}

variable "ecr_repo_name" {
  type = string
}

variable "ecr_repo_arn" {
  type = string
}

variable "lambda_name" {
  type = string
}

variable "lambda_arn" {
  type = string
}