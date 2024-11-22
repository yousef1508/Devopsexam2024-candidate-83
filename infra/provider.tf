provider "aws" {
  region = "eu-west-1"
}

terraform {
  required_version = ">= 1.9.0"

  backend "s3" {
    bucket         = "pgr301-2024-terraform-state"
    key            = "83/terraform.tfstate"
    region         = "eu-west-1"
    encrypt        = true
  }
}
