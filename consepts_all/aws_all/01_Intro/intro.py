# AWS - Amazon Web Services Introduction
# Most used cloud platform in the world

print("=== What is AWS? ===")
print("  Cloud platform by Amazon — 200+ services")
print("  Pay only for what you use (no upfront cost)\n")

print("=== Core AWS Services ===")
services = {
    "EC2":          "Virtual servers (like your own Linux machine in cloud)",
    "S3":           "Object storage — store files, images, backups",
    "RDS":          "Managed relational DB (PostgreSQL, MySQL)",
    "DynamoDB":     "Managed NoSQL key-value database",
    "Lambda":       "Serverless functions — run code without managing servers",
    "ECS/EKS":      "Run Docker containers (ECS=managed, EKS=Kubernetes)",
    "API Gateway":  "Manage and expose APIs, connect to Lambda",
    "SQS":          "Managed message queue",
    "SNS":          "Pub/Sub notifications",
    "ElastiCache":  "Managed Redis/Memcached",
    "CloudFront":   "CDN — deliver content fast globally",
    "Route 53":     "DNS service — manage domain names",
    "IAM":          "Identity — manage users, roles, permissions",
    "CloudWatch":   "Monitoring, logs, alerts",
    "ECR":          "Docker image registry",
    "Secrets Manager":"Store API keys, passwords securely",
}
for k, v in services.items():
    print(f"  {k:16}: {v}")

print("\n=== AWS Regions and AZs ===")
print("  Region:            Geographic area (ap-south-1 = Mumbai)")
print("  Availability Zone: Data center within a region (ap-south-1a, 1b, 1c)")
print("  Deploy across AZs for high availability\n")

print("=== Install AWS CLI ===")
print("  pip install awscli")
print("  aws configure  →  enter Access Key, Secret Key, Region")
print("  aws s3 ls      →  test connection")

print("\n=== Common Regions ===")
regions = {
    "ap-south-1":    "Mumbai (India) — use this for Indian projects",
    "us-east-1":     "N. Virginia (USA) — most services available here",
    "eu-west-1":     "Ireland (Europe)",
    "ap-southeast-1":"Singapore (SE Asia)",
}
for k, v in regions.items():
    print(f"  {k:18}: {v}")
