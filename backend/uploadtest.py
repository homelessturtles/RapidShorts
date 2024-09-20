import boto3
import os

s3_key = os.getenv('S3_KEY')
s3_secret_key = os.getenv('S3_SECRET_KEY')
client = boto3.client('s3', aws_access_key_id=s3_key,
                      aws_secret_access_key=s3_secret_key)

upload_file_bucket = 'rapidshorts'


def upload_video(file, fname):
    client.upload_file(file, upload_file_bucket, fname)


def get_url(fname):
    return client.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': upload_file_bucket,
                'Key': fname},
        ExpiresIn=1800)


#upload_video('backend/lions_1.mp4', 'lions.mp4')
#print(get_url('lions.mp4'))
