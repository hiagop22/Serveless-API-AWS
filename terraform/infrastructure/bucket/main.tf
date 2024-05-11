resource "aws_s3_bucket" "main" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_lifecycle_configuration" "bucket-config" {
  bucket = aws_s3_bucket.main.id

  rule {
    id = "log"

    expiration {
      days = 10
    }

    status = var.expiration == true ? "Enabled" : "Disabled"

    # transition {
    #   days          = 10
    #   storage_class = "STANDARD_IA"
    # }
  }
}