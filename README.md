# Pulumi AWS S3 with Python

Create and configure a new stack

```sh
pulumi stack init s3
pulumi config set aws:region ap-southeast-1
pulumi config set pulumi-aws-s3-python:bucket-name <value>
pulumi config set pulumi-aws-s3-python:environment <value>
```

Preview and run the deployment

```sh
pulumi up
```

---

Remove the app and its stack

```sh
pulumi destroy && pulumi stack rm -y
```
