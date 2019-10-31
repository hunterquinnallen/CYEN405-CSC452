"""
Lab 4: Q1H: Get info about security groups: Hunter Allen Edition
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.describe_security_groups(GroupIds=['sg-024ba7b0d49cf4b1b'])
    print('Success', response)
except ClientError as e:
    print(e)