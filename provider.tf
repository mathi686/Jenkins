provider "aws" {
  region     = "us-east-2"
  access_key = "AKIAWNHN56SPM6TBQIPM"
  secret_key = "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"
}


terraform {
  backend "s3" {
    bucket = "ookey1"
    key = "mathi/terraform.tfstate"
    region = "us-east-2"
    access_key = "AKIAWNHN56SPM6TBQIPM"
  secret_key = "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
    dynamodb_table = "ookey"
  }
}