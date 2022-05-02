terraform {
  backend "s3" {
    bucket = "vorx-infra-remote-state"
    key    = "contador-app.tfstate"
    region = "us-east-1"
  }
}