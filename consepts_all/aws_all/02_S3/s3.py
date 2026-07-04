# AWS S3 - Simple Storage Service
# Store files, images, videos, backups, static websites
# pip install boto3

import boto3
from botocore.exceptions import ClientError

# --- Connect to S3 ---
s3 = boto3.client(
    's3',
    region_name='ap-south-1',
    aws_access_key_id='YOUR_ACCESS_KEY',         # use env vars in production
    aws_secret_access_key='YOUR_SECRET_KEY'
)

# Better: use environment variables or IAM role
# s3 = boto3.client('s3')  # reads from ~/.aws/credentials or env vars

print("=== S3 Bucket Operations ===")
print("""
import boto3
s3 = boto3.client('s3', region_name='ap-south-1')

# Create bucket
s3.create_bucket(
    Bucket='my-app-bucket',
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
)

# List buckets
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

# Delete bucket (must be empty)
s3.delete_bucket(Bucket='my-app-bucket')
""")

print("=== File Operations ===")
print("""
# Upload file
s3.upload_file('local_file.txt', 'my-bucket', 'folder/remote_file.txt')

# Upload from memory (BytesIO)
import io
data = b"Hello from Python!"
s3.put_object(Bucket='my-bucket', Key='hello.txt', Body=data)

# Download file
s3.download_file('my-bucket', 'folder/remote_file.txt', 'downloaded.txt')

# List files in bucket
response = s3.list_objects_v2(Bucket='my-bucket', Prefix='folder/')
for obj in response.get('Contents', []):
    print(obj['Key'], obj['Size'])

# Delete file
s3.delete_object(Bucket='my-bucket', Key='folder/remote_file.txt')

# Check if file exists
try:
    s3.head_object(Bucket='my-bucket', Key='file.txt')
    print("File exists")
except ClientError as e:
    if e.response['Error']['Code'] == '404':
        print("File not found")
""")

print("=== Generate Pre-signed URL (temporary access) ===")
print("""
# Generate URL valid for 1 hour — share with users to download
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': 'my-bucket', 'Key': 'file.txt'},
    ExpiresIn=3600
)
print(url)  # https://my-bucket.s3.amazonaws.com/file.txt?X-Amz-...

# Generate URL for upload
url = s3.generate_presigned_url(
    'put_object',
    Params={'Bucket': 'my-bucket', 'Key': 'upload.txt'},
    ExpiresIn=300
)
""")

print("=== FastAPI File Upload to S3 ===")
print("""
from fastapi import FastAPI, UploadFile
import boto3, uuid

app = FastAPI()
s3 = boto3.client('s3')

@app.post("/upload")
async def upload_file(file: UploadFile):
    key = f"uploads/{uuid.uuid4()}/{file.filename}"
    s3.upload_fileobj(file.file, 'my-bucket', key)
    url = f"https://my-bucket.s3.ap-south-1.amazonaws.com/{key}"
    return {"url": url, "key": key}
""")
