import boto3

# Specify the AWS region
region_name = 'ap-southeast-2'

# Create a Boto3 EC2 client
ec2_client = boto3.client('ec2', region_name=region_name)

# Describe instances
response = ec2_client.describe_instances()

# Iterate over reservations
for reservation in response['Reservations']:
    # Iterate over instances
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}, Type: {instance['InstanceType']}")
