resource "aws_iam_role" "tf-pipeline-role" {
  name = "tf-pipeline-role"

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
          Service = "codepipeline.amazonaws.com"
        }
      },
    ]
  })
}

data "aws_iam_policy_document" "tf-pipeline-policies" {
  statement {
    sid       = ""
    actions   = ["codestar-connections:UseConnection"]
    # actions   = ["codestar-connections:*"]
    resources = ["*"]
    effect    = "Allow"
  }
  statement {
    sid       = ""
    actions   = ["cloudwatch:*", "s3:*", "codebuild:*"]
    resources = ["*"]
    effect    = "Allow"
  }
}

resource "aws_iam_policy" "tf-pipeline-policy" {
  name        = "tf-pipeline-policiy"
  path        = "/"
  description = "Pipeline policy"
  policy      = data.aws_iam_policy_document.tf-pipeline-policies.json
}

resource "aws_iam_role_policy_attachment" "tf-pipeline-attachment" {
  policy_arn = aws_iam_policy.tf-pipeline-policy.arn
  role       = aws_iam_role.tf-pipeline-role.id
}

