import pulumi
from pulumi_aws import s3

# Create AWS resources
bucket = s3.Bucket(
    "atbee-name",
    bucket="atbee-name",
)

# Output
pulumi.export("bucket-name", bucket.id)
