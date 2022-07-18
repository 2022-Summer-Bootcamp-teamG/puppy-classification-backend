import boto3
from botocore.client import Config

from .s3Config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

def s3_connection():
    s3 =  boto3.resource(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        config=Config(signature_version='s3v4'))
    return s3