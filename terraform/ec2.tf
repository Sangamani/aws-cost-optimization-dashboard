resource "aws_instance" "cost_detective_server" {

  ami           = var.ami_id
  instance_type = var.instance_type

  subnet_id = "subnet-07d11da880dfc14cb"

  tags = {
    Name = "AI-Cost-Detective"
  }
}