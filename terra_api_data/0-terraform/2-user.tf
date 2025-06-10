resource "aws_iam_user" "weather_user" {
  name = "gozie_weather_user"
  tags = {
    tag-key = "tag-value"
  }
}


data "aws_iam_policy_document" "weather_user_policy" {

  statement {
    actions = ["s3:ListAllMyBuckets"]
    resources = ["arn:aws:s3:::gozie-weather-data/*"]
    effect = "Allow"
    }

 statement {
    actions = ["s3:ListBucket"]
    resources = ["arn:aws:s3:::gozie-weather-data"]
    effect = "Allow"
  }

  statement {
    actions = ["s3:GetObject"]
    resources = ["arn:aws:s3:::gozie-weather-data/*"]
    effect = "Allow"
  }
  
  statement {
    actions = ["s3:PutObject"]
    resources = ["arn:aws:s3:::gozie-weather-data/*"]
    effect = "Allow"
  }
  
 
}


resource "aws_iam_policy" "weather_user_policy" {
  name   = "weather_policy"
  policy = data.aws_iam_policy_document.weather_user_policy.json
}


resource "aws_iam_policy_attachment" "test-attach" {
  name       = "test-attachment"
  users      = [aws_iam_user.weather_user.name]
  policy_arn = aws_iam_policy.weather_user_policy.arn
}