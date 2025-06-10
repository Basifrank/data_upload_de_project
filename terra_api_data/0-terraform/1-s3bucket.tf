resource "aws_s3_bucket" "weather_bucket" {
 
  bucket   = "gozie-weather-data"
  tags = {
    Name        = "Gozie Weather Data"
    Environment = "Dev"
  }
}