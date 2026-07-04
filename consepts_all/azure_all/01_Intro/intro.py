# Azure - Microsoft Azure Cloud Platform
# Second largest cloud platform after AWS

print("=== What is Azure? ===")
print("  Microsoft's cloud platform — 200+ services")
print("  Strong in enterprise, .NET, Windows, AI/ML services\n")

print("=== Azure Core Services ===")
services = {
    "Virtual Machines":     "Like AWS EC2 — Linux/Windows VMs",
    "Blob Storage":         "Like AWS S3 — store files, images, backups",
    "Azure SQL":            "Managed SQL Server / PostgreSQL / MySQL",
    "Cosmos DB":            "Like AWS DynamoDB — globally distributed NoSQL",
    "Azure Functions":      "Like AWS Lambda — serverless functions",
    "AKS":                  "Azure Kubernetes Service — managed K8s",
    "ACI":                  "Azure Container Instances — run Docker containers",
    "API Management":       "Like AWS API Gateway — manage APIs",
    "Service Bus":          "Like AWS SQS/SNS — message queue",
    "Azure Cache (Redis)":  "Managed Redis",
    "Azure CDN":            "Content Delivery Network",
    "Azure AD":             "Identity and access management",
    "Key Vault":            "Like AWS Secrets Manager — store secrets",
    "Azure Monitor":        "Like AWS CloudWatch — logs and metrics",
    "Azure OpenAI":         "GPT-4, DALL-E, Whisper via Azure",
}
for k, v in services.items():
    print(f"  {k:24}: {v}")

print("\n=== AWS vs Azure Comparison ===")
comparison = {
    "EC2":          "Virtual Machines",
    "S3":           "Blob Storage",
    "Lambda":       "Azure Functions",
    "RDS":          "Azure SQL Database",
    "DynamoDB":     "Cosmos DB",
    "SQS":          "Service Bus Queue",
    "CloudWatch":   "Azure Monitor",
    "IAM":          "Azure Active Directory",
    "ECR":          "Azure Container Registry",
    "EKS":          "AKS (Azure Kubernetes Service)",
}
print("  AWS Service       → Azure Equivalent")
for aws, azure in comparison.items():
    print(f"  {aws:16}→ {azure}")

print("\n=== Install Azure SDK ===")
print("  pip install azure-storage-blob azure-identity azure-cosmos")
print("  az login  (Azure CLI)")
