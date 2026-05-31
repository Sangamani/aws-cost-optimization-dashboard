import boto3

session = boto3.Session(
    profile_name="default"
)

ec2 = session.client(
    "ec2",
    region_name="ap-south-1"
)