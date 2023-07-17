# delete-aws-s3-date.py

## This python script helps delete multiple Objects in a S3 bucket post on a cutoff date

- Download this file
- Chmod it to 755
- Make sure boto3 is installed (pip3 install boto3)
- Change the values in the file (Bucket name, Prefix, Date)
- Run this python script after authenticating with https://github.com/mmmorris1975/aws-runas (aws-runas -E <profile-name> python3 delete-aws-s3-date.py)
