"""
Lab 4: Q1F: Create a new key pair: Hunter Allen Edition
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName='hqa001Lab41fKey')
print('Success', response)