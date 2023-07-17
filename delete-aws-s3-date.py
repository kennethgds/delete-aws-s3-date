import boto3
from datetime import datetime, timezone

s3 = boto3.client('s3', region_name='us-east-1')
bucket = 'XXX' # bucket-name
prefix = 'XXX' # bucket-prefix
paginator = s3.get_paginator("list_objects_v2")
pages = paginator.paginate(Bucket=bucket, Prefix=prefix)
date_check = datetime(YYYY, MM, DD) # date after which you want to delete

keys_to_delete = []
for page in pages:
    for obj in page["Contents"]:
        if obj["LastModified"] > date_check.replace(tzinfo=timezone.utc):
            keys_to_delete.append({"Key": obj["Key"]})
    
for chunk in [keys_to_delete[i:i+1000] for i in range(0, len(keys_to_delete), 1000)]:
    print(chunk)
    s3.delete_objects(Bucket=bucket, Delete={'Objects': chunk})
