import boto3
from datetime import datetime, timedelta

def cleanup_unused_resources():
    # AWS credentials and region
    #aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
    #aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
    aws_region = 'ap-southeast-2'

    # Initialize AWS clients
    ec2_client = boto3.client('ec2', region_name=aws_region)
    ec2_resource = boto3.resource('ec2', region_name=aws_region)

    # Calculate cutoff date (120 days ago)
    cutoff_date = datetime.now() - timedelta(days=120)

    # Cleanup unused EBS volumes
    unused_volumes = ec2_client.describe_volumes(
        Filters=[
            {'Name': 'status', 'Values': ['available']},
            {'Name': 'create-time', 'Values': [cutoff_date.strftime('%Y-%m-%d')]}
        ]
    )['Volumes']

    for volume in unused_volumes:
        volume_id = volume['VolumeId']
        print(f"Deleting unused EBS volume: {volume_id}")
        ec2_resource.Volume(volume_id).delete()

    # Cleanup associated snapshots
    for volume_id in [volume['VolumeId'] for volume in unused_volumes]:
        snapshots = ec2_client.describe_snapshots(Filters=[{'Name': 'volume-id', 'Values': [volume_id]}])['Snapshots']
        for snapshot in snapshots:
            snapshot_id = snapshot['SnapshotId']
            print(f"Deleting associated snapshot: {snapshot_id}")
            ec2_resource.Snapshot(snapshot_id).delete()

if __name__ == "__main__":
    cleanup_unused_resources()
