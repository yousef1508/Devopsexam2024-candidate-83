provider "aws" {
  region = "eu-west-1"
}

terraform {
  backend "s3" {
    bucket         = "pgr301-couch-explorers"
    key            = "terraform/sqs-lambda/terraform.tfstate"
    region         = "eu-west-1"
    encrypt        = true
  }
}
