"""
Lab 4: Q1D: Reboot Amazon BC2 instance: Hunter Allen Edition
"""
import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try: 
    ec2.reboot_instances(InstanceIds=['i-016b5621ca7cfdcf9'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot intances")
        raise
# Dry run succeeded, run reboot_instances again without dryrun
try: 
    response = ec2.reboot_instances(InstanceIds=['i-016b5621ca7cfdcf9'], DryRun=False)
    print('Success', response)
except ClientError as e:
    print(e)