import boto3

def handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get the list of all Elastic IPs
    addresses_dict = ec2.describe_addresses()
    
    for eip_dict in addresses_dict['Addresses']:
        # Check if 'InstanceId' or 'NetworkInterfaceId' is missing, which indicates it's unassociated
        if 'InstanceId' not in eip_dict and 'NetworkInterfaceId' not in eip_dict:
            print(f"Releasing EIP {eip_dict['PublicIp']}")
            ec2.release_address(AllocationId=eip_dict['AllocationId'])

    return "Done!"
