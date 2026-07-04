# AWS IAM - Identity and Access Management
# Control who can access what in AWS

print("=== IAM Key Concepts ===")
concepts = {
    "User":         "Individual person or app with AWS credentials",
    "Group":        "Collection of users with same permissions",
    "Role":         "Temporary permissions for AWS services (EC2, Lambda)",
    "Policy":       "JSON document defining allowed/denied actions",
    "Permission":   "Allow or Deny specific actions on specific resources",
    "ARN":          "Amazon Resource Name — unique ID for any AWS resource",
    "Access Key":   "Programmatic access (key ID + secret key)",
    "MFA":          "Multi-Factor Authentication — extra security layer",
}
for k, v in concepts.items():
    print(f"  {k:14}: {v}")

print("\n=== IAM Policy Example ===")
print("""
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::my-app-bucket/*"
    },
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::my-app-bucket"
    },
    {
      "Effect": "Deny",
      "Action": "s3:DeleteBucket",
      "Resource": "*"
    }
  ]
}
""")

print("=== IAM Best Practices ===")
practices = [
    "Never use root account for daily work — create IAM users",
    "Enable MFA on root and all admin accounts",
    "Principle of least privilege — give minimum permissions needed",
    "Use IAM Roles for EC2/Lambda — never hardcode credentials",
    "Rotate access keys regularly",
    "Never commit AWS keys to Git — use environment variables",
    "Use AWS Secrets Manager for storing credentials",
    "Enable CloudTrail to log all API calls",
]
for p in practices:
    print(f"  - {p}")

print("\n=== IAM Role for EC2 (no hardcoded keys) ===")
print("""
# 1. Create IAM Role with S3 permissions
# 2. Attach role to EC2 instance
# 3. boto3 automatically uses the role — no keys needed!

import boto3
s3 = boto3.client('s3')  # uses EC2 instance role automatically
s3.list_buckets()
""")

print("\n=== AWS CLI IAM Commands ===")
print("""
aws iam create-user --user-name myuser
aws iam create-group --group-name developers
aws iam add-user-to-group --user-name myuser --group-name developers
aws iam attach-group-policy --group-name developers --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
aws iam list-users
aws iam get-user --user-name myuser
""")
