################################################################################
# AWS Provider
################################################################################

provider "aws" {
  region  = "${var.aws_region}"
  profile = "management"

  assume_role {
      # Sandbox Account
      role_arn = "arn:aws:iam::842337631775:role/1S-Admins"
  }
}

################################################################################
# S3 Backend
################################################################################

terraform {
  backend "s3" {
    region = "us-west-2"
    profile = "management"
    role_arn = "arn:aws:iam::842337631775:role/1S-Admins"
    bucket = "1s-bd-streaming-terraform"
    key = "big_data_streaming.tfstate"
  }
}