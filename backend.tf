terraform {
  backend "s3" {
    bucket = "tf-remote-state-jfidk"
    key    = "vpc"
    region = "us-east-1"
  }
}
