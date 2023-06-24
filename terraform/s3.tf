terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~>5.0"
    }
  }
}

provider "aws" {
  region = var.region
}


resource "aws_s3_bucket" "example" {
  count = 2
  bucket = "${element(var.names, count.index)}-platform-challenge"
  
}