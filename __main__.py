import pulumi
from pulumi_aws import s3


config = pulumi.Config()
bucket_name = config.require("bucket-name")
environment = config.require("environment")

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
    tags={
        "Environment": environment,
        "ProductArea": "Storage",
        "Team": "Atbee",
    },
    versioning=s3.BucketVersioningArgs(
        enabled=True,
    ),
)

bucket_public_access_block = s3.BucketPublicAccessBlock("bucket-public-access-block",
    bucket=bucket.id,
    block_public_acls=True,
    block_public_policy=True,
    ignore_public_acls=True,
    restrict_public_buckets=True,
)

# Output
pulumi.export("bucket-name", bucket.id)
