# GitHub Actions - CI/CD built into GitHub
# File location: .github/workflows/main.yml

print("=== GitHub Actions Key Terms ===")
terms = {
    "Workflow":  "Automated process defined in YAML file",
    "Job":       "Group of steps that run on same machine",
    "Step":      "Single task (run command or use action)",
    "Action":    "Reusable step from GitHub Marketplace",
    "Runner":    "Machine that runs the job (ubuntu-latest, windows, mac)",
    "Trigger":   "When to run: push, pull_request, schedule, manual",
    "Secret":    "Encrypted variable stored in GitHub settings",
    "Artifact":  "Files saved from workflow (test reports, builds)",
    "Matrix":    "Run same job with different configs (Python 3.10, 3.11)",
}
for k, v in terms.items():
    print(f"  {k:12}: {v}")

print("\n=== Workflow 1: Run Tests on Every Push ===")
print("""
# .github/workflows/test.yml
name: Run Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest

      - name: Run tests
        run: pytest tests/ -v
""")

print("=== Workflow 2: Build and Push Docker Image ===")
print("""
# .github/workflows/docker.yml
name: Build and Deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push image
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: myusername/myapp:latest

      - name: Deploy to server
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ubuntu
          key: ${{ secrets.SSH_KEY }}
          script: |
            docker pull myusername/myapp:latest
            docker stop myapp || true
            docker run -d --name myapp -p 8000:8000 myusername/myapp:latest
""")
