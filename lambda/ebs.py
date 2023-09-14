import boto3

def handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Step 1: List all AMIs
    amis = ec2.describe_images(Owners=['self'])['Images']
    
    # Step 2: Extract snapshot IDs from AMIs
    associated_snapshots = set()
    for ami in amis:
        for block_device in ami['BlockDeviceMappings']:
            if 'Ebs' in block_device and 'SnapshotId' in block_device['Ebs']:
                associated_snapshots.add(block_device['Ebs']['SnapshotId'])
    
    # Step 3: List all EBS snapshots
    paginator = ec2.get_paginator('describe_snapshots')
    for page in paginator.paginate(OwnerIds=['self']):
        for snapshot in page['Snapshots']:
            # Step 4: Compare and delete if not associated with an AMI
            if snapshot['SnapshotId'] not in associated_snapshots:
                print(f"Deleting snapshot {snapshot['SnapshotId']}...")
                ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])

    return {
        'statusCode': 200,
        'body': 'Snapshots cleaned up'
    }
