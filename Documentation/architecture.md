## Overview
This project implements an event-driven serverless architecture for image processing using AWS managed services.
The system automatically processes images upon upload without managing servers.

## Architecture Components

### Amazon S3
- Source bucket for original images
- Destination bucket for processed images
- Event notifications enabled

### AWS Lambda
- Triggered by S3 upload events
- Performs image resizing or watermarking
- Stores processed images in destination bucket

### CloudWatch
- Captures Lambda logs
- Monitors execution metrics

### Optional Services
- DynamoDB for image metadata
- API Gateway for upload endpoints
