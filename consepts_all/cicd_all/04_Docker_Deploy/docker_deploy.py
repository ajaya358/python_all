# Docker Deploy - Full deployment pipeline with Docker
# Build image → push to registry → pull on server → run

print("=== Full Docker Deploy Flow ===")
flow = [
    "1. Code pushed to GitHub/GitLab",
    "2. CI pipeline builds Docker image",
    "3. Image pushed to Docker Hub / AWS ECR / GitLab Registry",
    "4. Deploy step SSHs into server",
    "5. Server pulls latest image",
    "6. Old container stopped, new container started",
    "7. App is live with zero downtime (with proper setup)",
]
for step in flow:
    print(f"  {step}")

print("\n=== Docker Hub Push (manual) ===")
print("""
# Build and tag
docker build -t myusername/myapp:latest .
docker build -t myusername/myapp:v1.0.0 .

# Login and push
docker login
docker push myusername/myapp:latest
docker push myusername/myapp:v1.0.0

# On server: pull and run
docker pull myusername/myapp:latest
docker stop myapp && docker rm myapp
docker run -d --name myapp -p 8000:8000 --restart always myusername/myapp:latest
""")

print("=== AWS ECR Push ===")
print("""
# Authenticate
aws ecr get-login-password --region ap-south-1 | \\
  docker login --username AWS --password-stdin <account_id>.dkr.ecr.ap-south-1.amazonaws.com

# Tag and push
docker tag myapp:latest <account_id>.dkr.ecr.ap-south-1.amazonaws.com/myapp:latest
docker push <account_id>.dkr.ecr.ap-south-1.amazonaws.com/myapp:latest
""")

print("=== Zero Downtime Deploy with Docker Compose ===")
print("""
# docker-compose.prod.yml
version: '3.8'
services:
  web:
    image: myusername/myapp:latest
    ports:
      - "8000:8000"
    restart: always
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - SECRET_KEY=${SECRET_KEY}

# Deploy command on server
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d --no-deps web
""")

print("=== Health Check in Dockerfile ===")
print("""
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \\
  CMD curl -f http://localhost:8000/health || exit 1
""")
