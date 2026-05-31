from src.scanner import get_instances

print("Starting EC2 scan...")

instances = get_instances()

print("Scan completed")

print(instances)