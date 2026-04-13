import boto3

def list_instances():
    ec2 = boto3.client("ec2", region_name="us-east-1")

    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print("Instance ID:", instance["InstanceId"])


if __name__ == "__main__":
    list_instances()
