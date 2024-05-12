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
    sid = "1"
    actions = ["logs:*",
      "s3:*",
      "codebuild:*",
      "secretsmanager:*",
      "iam:*",
      "lambda:*",
      "codestar:*",
    ]
    resources = ["*"]
    effect    = "Allow"
  }

  statement {
    sid = "2"
    actions = [
      "ecr:BatchCheckLayerAvailability",
      "ecr:BatchGetImage",
      "ecr:CompleteLayerUpload",
      "ecr:GetDownloadUrlForLayer",
      "ecr:InitiateLayerUpload",
      "ecr:PutImage",
      "ecr:UploadLayerPart",
    ]
    resources = [var.ecr_repo_arn]
    effect    = "Allow"
  }

  statement {
    sid = "3"
    actions = [
      "ecr:GetAuthorizationToken",
    ]
    effect    = "Allow"
    resources = ["*"]
  }

  statement {
    sid     = "4"
    actions = ["lambda:UpdateFunctionCode"]
    effect  = "Allow"
    resources = [
      var.lambda_arn
    ]
  }

  statement {
    sid       = "5"
    actions   = ["codestar-connections:UseConnection",
                  # "codecodestar-connections:ProviderAction",
                  ]
    # actions   = ["codestar-connections:*"]
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