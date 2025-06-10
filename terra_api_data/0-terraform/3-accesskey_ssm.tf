resource "aws_iam_access_key" "weather_user_key" {
  user = aws_iam_user.weather_user.name
}



resource "aws_ssm_parameter" "weather_user_access_key" {
  name        = "/weather/access_key"
  type        = "SecureString"
  value       = aws_iam_access_key.weather_user_key.id
  description = "Access key for the weather user"
  
}


resource "aws_ssm_parameter" "weather_user_secret_key" {
  name        = "/weather/secret_key"
  type        = "SecureString"
  value       = aws_iam_access_key.weather_user_key.secret
  description = "Secret key for the weather user"
  
}