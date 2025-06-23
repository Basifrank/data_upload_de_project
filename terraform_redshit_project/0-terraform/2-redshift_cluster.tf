resource "aws_redshift_cluster" "gozie_redshift_cluster" {
  cluster_identifier = "gozie_redshift_cluster"
  database_name      = "mydb"
  master_username    = "gozie_admin"
  master_password    = random_password.password.result
  node_type          = "ra3.xlplus"
  cluster_type       = "multi-node"
  number_of_nodes    = 3
   
}




