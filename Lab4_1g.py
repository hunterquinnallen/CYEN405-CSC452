"""
Lab 4: Q1G: Delete a new key pair: Hunter Allen Edition
"""
import boto3
ec2 = boto3.client('ec2')
response = ec2.delete_key_pair(KeyName='hqa001Lab41fKey')
print('Success', response)