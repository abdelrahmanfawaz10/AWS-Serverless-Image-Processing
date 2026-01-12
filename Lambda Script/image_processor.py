import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    dest_bucket = "processed-images-bucket"

    response = s3.get_object(Bucket=source_bucket, Key=object_key)
    image = Image.open(response['Body'])

    image = image.resize((300, 300))
    buffer = io.BytesIO()
    image.save(buffer, 'JPEG')
    buffer.seek(0)

    s3.put_object(Bucket=dest_bucket, Key=object_key, Body=buffer)
