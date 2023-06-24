import boto3
from datetime import datetime



date_format = "%Y-%m-%d|%H:%M:%S"
current_date = datetime.now().strftime(date_format)
file_name = f"{current_date}.txt"

file_content = "This file is uploaded to S3."
bucket_name_1 = "qa-ibrahim-ulker-platform-challenge"
bucket_name_2 = "staging-ibrahim-ulker-platform-challenge"

session = boto3.Session(profile_name='default')

default_s3_client = session.client('s3')

s3_client = boto3.client('s3',
     region_name = "us-east-1")
s3_client.put_object(Body=file_content, Bucket=bucket_name_1, Key=file_name)
s3_client.put_object(Body=file_content, Bucket=bucket_name_2, Key=file_name)




