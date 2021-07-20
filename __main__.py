import pulumi
from pulumi_aws import s3


config = pulumi.Config()
bucket_name = config.require("bucket-name")

# Create AWS resources
bucket = s3.Bucket(
    bucket_name,
    bucket=bucket_name,
)

# Output
pulumi.export("bucket-name", bucket.id)
