resource "aws_codebuild_project" "main" {
  name         = "tf-cicd-build"
  description  = "Apply stage for terraform"
  service_role = aws_iam_role.tf-codebuild-role.arn

  artifacts {
    type = "CODEPIPELINE"
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/amazonlinux2-x86_64-standard:4.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"
  }

  source {
    type = "CODEPIPELINE"
    buildspec = templatefile("${path.module}/buildspec/buildspec.yaml",
      { account_id  = var.account_id,
        repo_name   = var.ecr_repo_name,
        lambda_name = var.lambda_name,
    })
  }
}

resource "aws_codepipeline" "cicd_pipeline" {
  name     = "tf-cicd"
  role_arn = aws_iam_role.tf-pipeline-role.arn

  artifact_store {
    type     = "S3"
    location = var.bucket_artifact_id
  }

  stage {
    name = "Source"
    action {
      name             = "Source"
      category         = "Source"
      owner            = "AWS"
      provider         = "CodeStarSourceConnection"
      version          = "1"
      output_artifacts = ["tf-code"]
      configuration = {
        FullRepositoryId     = var.respository_id
        BranchName           = var.branch
        ConnectionArn        = var.codestar_connector_credentials
        OutputArtifactFormat = "CODE_ZIP"
      }
    }
  }

  stage {
    name = "Build"
    action {
      name            = "Build"
      category        = "Build"
      provider        = "CodeBuild"
      version         = "1"
      owner           = "AWS"
      input_artifacts = ["tf-code"]
      configuration = {
        ProjectName = "tf-cicd-build"
      }
    }
  }

  # stage {
  #   name = "Deploy"
  #   action {
  #     name            = "Deploy"
  #     category        = "Build"
  #     provider        = "CodeBuild"
  #     version         = "1"
  #     owner           = "AWS"
  #     input_artifacts = ["tf-code"]
  #     configuration = {
  #       ProjectName = "tf-cicd-apply"
  #     }
  #   }
  # }
}