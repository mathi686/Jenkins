provider "aws" {
  region = "us-east-2"  # Replace with your desired AWS region
}

data "aws_secretsmanager_secret" "my_secret" {
  name = "my_secret_version"  # Specify the name of your secret in AWS Secrets Manager
}

data "aws_secretsmanager_secret_version" "my_secret_version" {
  secret_id = data.aws_secretsmanager_secret.my_secret.id
}


#terraform {
#  backend "s3" {
#    bucket         = "ookey1"
#    key            = "mathi/terraform.tfstate"
#    region         = "us-east-2"
#    access_key     = "AKIAWNHN56SPM6TBQIPM"
#    secret_key     = "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"
#    dynamodb_table = "ookey"
#  }
#}
