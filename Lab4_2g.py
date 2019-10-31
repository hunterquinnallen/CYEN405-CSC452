"""
Lab 4: Q2G: Retrieve a bucket policy: Hunter Allen Edition
"""
import boto3
bucket_name = 'huntersbucket2'
s3 = boto3.client('s3')
response = s3.get_bucket_ac1(Bucket=bucket_name)
print(response)