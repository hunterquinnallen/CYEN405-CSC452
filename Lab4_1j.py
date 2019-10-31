"""
Lab 4: Q1J: Delete a security group: Hunter Allen Edition
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.delete_security_group(GroupId='sg-055f411301dfbf632')
    print('Success', response)
except ClientError as e:
    print(e)