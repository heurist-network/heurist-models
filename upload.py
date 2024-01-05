import boto3
import os
import argparse
from dotenv import load_dotenv

# Example usage for uploading a directory of files to a bucket:
# python3 upload.py --dir ~/Downloads/civitai --bucket heurist-models

# Load .env file
load_dotenv()

# Configure the S3 client to use Cloudflare's endpoint
s3_client = boto3.client(
    's3',
    region_name='enam',
    endpoint_url=os.getenv('S3_ENDPOINT'),
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY')
)

# Create the parser and add command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--dir', help='The directory containing the files you want to upload')
parser.add_argument('--bucket', help='The name of your Cloudflare R2 bucket')
args = parser.parse_args()

# Iterate over the files in the directory and upload them
for filename in os.listdir(args.dir):
    file_path = os.path.join(args.dir, filename)
    if os.path.isfile(file_path):
        s3_client.upload_file(file_path, args.bucket, filename)
        print(f'Uploaded {file_path} to {args.bucket}/{filename}')