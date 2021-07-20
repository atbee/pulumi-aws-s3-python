# Pulumi AWS S3 with Python

Create and configure a new stack

```sh
pulumi stack init s3
pulumi config set aws:region ap-southeast-1
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
