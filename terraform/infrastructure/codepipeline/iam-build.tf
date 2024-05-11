resource "aws_iam_role" "tf-codebuild-role" {
  name = "tf-ccodebuild-role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "codebuild.amazonaws.com"
        }
      },
    ]
  })
}

data "aws_iam_policy_document" "tf-codebuild-policies" {
  statement {
    sid       = ""
    actions   = ["logs:*", "s3:*", "codebuild:*", "secretsmanager:*", "iam:*"]
    resources = ["*"]
    effect    = "Allow"
  }
}

resource "aws_iam_policy" "tf-codebuild-policy" {
  name   = "tf-codebuild-policy"
  path   = "/"
  policy = data.aws_iam_policy_document.tf-codebuild-policies.json
}

resource "aws_iam_role_policy_attachment" "tf-codebuild-attachment" {
  policy_arn = aws_iam_policy.tf-codebuild-policy.arn
  role       = aws_iam_role.tf-codebuild-role.id
}