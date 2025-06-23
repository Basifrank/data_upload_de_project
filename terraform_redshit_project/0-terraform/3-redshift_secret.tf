

#create a secret in AWS Secrets Manager for Redshift connection details

resource "aws_secretsmanager_secret" "connection_redshift" {
  name = "secret_redshift"
}

# Create a secret version in AWS Secrets Manager for Redshift connection details
# This will store the secret value created above 

resource "aws_secretsmanager_secret_version" "connection_redshift" {
  secret_id     = aws_secretsmanager_secret.connection_redshift.id
  secret_string = jsonencode({
    username            = aws_redshift_cluster.gozie_redshift_cluster.master_username
    password            = aws_redshift_cluster.gozie_redshift_cluster.master_password
    
  })
}