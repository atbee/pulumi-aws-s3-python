import pulumi
from pulumi_aws import s3


config = pulumi.Config()
bucket_name = config.require("bucket-name")

# Create AWS S3 bucket resource
bucket = s3.Bucket(
    bucket_name,
    acl="private",
    bucket=bucket_name,
    server_side_encryption_configuration=s3.BucketServerSideEncryptionConfigurationArgs(
        rule=s3.BucketServerSideEncryptionConfigurationRuleArgs(
            bucket_key_enabled=False,
            apply_server_side_encryption_by_default=s3.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs(
                sse_algorithm="AES256",
            ),
        ),
    ),
    versioning=s3.BucketVersioningArgs(
        enabled=True,
    ),
)

# Output
pulumi.export("bucket-name", bucket.id)
