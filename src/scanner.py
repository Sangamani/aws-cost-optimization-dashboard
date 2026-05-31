from src.aws_client import ec2


def get_instances():

    try:

        response = ec2.describe_instances()

        instances = []

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                instances.append({
                    "instance_id": instance["InstanceId"],
                    "instance_type": instance["InstanceType"],
                    "state": instance["State"]["Name"]
                })

        return instances

    except Exception as e:

        return {
            "error": str(e)
        }