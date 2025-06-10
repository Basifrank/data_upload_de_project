resource "aws_s3_bucket" "weather_bucket" {
 
  bucket   = "gozie-google-sheet-data"
  tags = {
    Name        = "Gozie Google Sheet Data"
    Environment = "Dev"
  }
}