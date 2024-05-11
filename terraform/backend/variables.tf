variable "aws_region" {
  type        = string
  description = ""
  default     = "us-east-1"
}

variable "aws_profile" {
  type    = string
  default = "personal"
}

variable "bucket_name" {
  type    = string
  default = "test-cicd-tf-ai-api-state"
}

variable "table_name" {
  type    = string
  default = "test-cicd-tf-ai-api-state"
}
