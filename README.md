# AWS Serverless Image Processing

## Project Overview
This project demonstrates a serverless image processing application built on AWS.
When a user uploads an image to an S3 bucket, an AWS Lambda function is triggered automatically to process the image (resize/watermark) and store the output in another S3 bucket.

## Solution Architecture
Architecture/Architecture.png

## AWS Services Used
- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch
- (Optional) Amazon DynamoDB
- (Optional) Amazon API Gateway

## Workflow
1. User uploads an image to the source S3 bucket
2. S3 event notification triggers Lambda
3. Lambda processes the image
4. Processed image is stored in destination S3 bucket
5. Logs are stored in CloudWatch

## Security
- IAM role with least privilege
- S3 buckets with Block Public Access
- Encrypted S3 objects
- No hardcoded credentials

## Scalability
- Fully serverless and auto-scaling
- Handles high volume of uploads without manual scaling

## Cost Optimization
- Pay only per Lambda execution
- S3 lifecycle rules reduce storage costs

## Testing
- Upload image to S3
- Verify processed image
- Check CloudWatch logs

## Author
**AbdElrahman Fawaz**  
