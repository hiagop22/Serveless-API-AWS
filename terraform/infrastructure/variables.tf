variable "aws_region" {
  type        = string
  description = ""
  default     = "us-east-1"
}

variable "aws_profile" {
  type    = string
  default = "personal"
}

# variable "dockerhub_credentials" {
#   type = string
# }

variable "codestar_connector_credentials" {
  type = string
}