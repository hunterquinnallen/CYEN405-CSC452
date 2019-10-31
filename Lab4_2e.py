"""
Lab 4: Q2E: Create Presigned URLs: Hunter Allen Edition
"""
import boto3
import logging


filename = 'README2.md'
bucket_name = 'huntersbucket2'
key = 'README.md'

# Create an S3 client
s3 = boto3.client('s3')
response = s3.generate_presigned_url(ClientMethod='get_object', Params = {'Bucket': bucket_name,'Key': key})

print(response)