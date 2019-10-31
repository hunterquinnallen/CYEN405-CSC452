"""
Lab 4: FIrst Python Boto3 activity: Hunter Allen Edition
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)