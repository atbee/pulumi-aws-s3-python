import pulumi
from pulumi_aws import s3

# Create AWS resources
bucket = s3.Bucket("my-bucket")

# Output
pulumi.export("bucket-name", bucket.id)
