output "instance_id" {
  value = aws_instance.cost_detective_server.id
}

output "public_ip" {
  value = aws_instance.cost_detective_server.public_ip
}