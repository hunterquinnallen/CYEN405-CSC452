"""
Lab 4: Q1C: Start and Stop an Amazon EC2 instance: Hunter Allen Edition
"""
import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
action = sys.argv[1].upper()
if action == 'ON':
    #Do a dryrun first to verify pernmissions
    try: 
        ec2.start_instances(InstanceIds=['i-016b5621ca7cfdcf9'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry run succeeded, run start_instances again without dryrun
    try: 
        response = ec2.start_instances(InstanceIds=['i-016b5621ca7cfdcf9'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    #Do a dryrun first to verify pernmissions
    try: 
        ec2.stop_instances(InstanceIds=['i-016b5621ca7cfdcf9'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry run succeeded, run start_instances again without dryrun
    try: 
        response = ec2.stop_instances(InstanceIds=['i-016b5621ca7cfdcf9'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)