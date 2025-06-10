resource "aws_iam_user" "sheet_user" {
  name = "gozie_google_user"
  tags = {
    tag-key = "tag-value"
  }
}


data "aws_iam_policy_document" "google_sheet_user_policy" {

  statement {
    actions = ["s3:ListAllMyBuckets"]
    resources = ["arn:aws:s3:::gozie-google-sheet-data/*"]
    effect = "Allow"
    }

 statement {
    actions = ["s3:ListBucket"]
    resources = ["arn:aws:s3:::gozie-google-sheet-data"]
    effect = "Allow"
  }

  statement {
    actions = ["s3:GetObject"]
    resources = ["arn:aws:s3:::gozie-google-sheet-data/*"]
    effect = "Allow"
  }
  
  statement {
    actions = ["s3:PutObject"]
    resources = ["arn:aws:s3:::gozie-google-sheet-data/*"]
    effect = "Allow"
  }
  
 
}


resource "aws_iam_policy" "gsheet_user_policy" {
  name   = "sheet_policy"
  policy = data.aws_iam_policy_document.google_sheet_user_policy.json
}


resource "aws_iam_policy_attachment" "g_test-attach" {
  name       = "test-attachment2"
  users      = [aws_iam_user.sheet_user.name]
  policy_arn = aws_iam_policy.gsheet_user_policy.arn
}