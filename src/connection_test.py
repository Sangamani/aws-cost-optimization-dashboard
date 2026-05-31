import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()

report = {
    "checks": {}
}

try:
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    ec2 = session.client("ec2")
    ce = session.client("ce")

    # EC2 connection test
    ec2.describe_regions()
    report["checks"]["ec2_connection"] = "PASS"

    # Cost Explorer test
    ce.get_cost_and_usage(
        TimePeriod={
            'Start': '2026-05-01',
            'End': '2026-05-27'
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost']
    )

    report["checks"]["cost_explorer"] = "PASS"

except Exception as e:
    report["checks"]["error"] = str(e)

os.makedirs("data", exist_ok=True)

with open("data/connection_report.json", "w") as f:
    json.dump(report, f, indent=4)

print(report)