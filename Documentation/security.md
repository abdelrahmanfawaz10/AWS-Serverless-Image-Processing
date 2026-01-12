## IAM
- Lambda execution role with access to:
  - Read objects from source bucket
  - Write objects to destination bucket
  - Write logs to CloudWatch

## S3 Security
- Block all public access
- Server-side encryption enabled
- Bucket policies restrict access

## Best Practices
- Least privilege IAM roles
- No exposed credentials
- AWS-managed services used
