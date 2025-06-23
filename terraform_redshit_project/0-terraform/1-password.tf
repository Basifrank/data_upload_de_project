# This file contains the configuration for generating a random password using Terraform.
resource "random_password" "password" {
  length           = 16
  special          = true
  override_special = "!$%&*()-_=+[]{}<>:?"
}

