resource "aws_iam_access_key" "google_user_key" {
  user = aws_iam_user.sheet_user.name
}


resource "aws_ssm_parameter" "sheet_user_access_key" {
  name        = "/sheet/access_key"
  type        = "SecureString"
  value       = aws_iam_access_key.google_user_key.id
  description = "Access key for the weather user"
  
}


resource "aws_ssm_parameter" "sheet_user_secret_key" {
  name        = "/sheet/secret_key"
  type        = "SecureString"
  value       = aws_iam_access_key.google_user_key.secret
  description = "Secret key for the weather user"
  
}