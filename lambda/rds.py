import boto3
import os

def handler(event, context):
    region = os.environ.get('AWS_REGION', 'us-east-1')
    rds = boto3.client('rds', region_name=region)

    instances = rds.describe_db_instances()
    for instance in instances['DBInstances']:
        if instance['DBInstanceStatus'] == 'available':
            instance_id = instance['DBInstanceIdentifier']
            print(f"Stopping RDS instance: {instance_id}")
            rds.stop_db_instance(DBInstanceIdentifier=instance_id)

    return {
        'statusCode': 200,
        'body': 'RDS instances stopped'
    }
