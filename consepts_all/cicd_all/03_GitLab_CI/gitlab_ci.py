# GitLab CI/CD - Built into GitLab
# File location: .gitlab-ci.yml (root of project)

print("=== GitLab CI/CD Key Terms ===")
terms = {
    "Pipeline":   "Full CI/CD process triggered by git push",
    "Stage":      "Group of jobs (test, build, deploy)",
    "Job":        "Single task inside a stage",
    "Runner":     "Machine that runs jobs (shared or self-hosted)",
    "Artifact":   "Files passed between jobs",
    "Environment":"Target deployment (staging, production)",
    "Variable":   "Stored in GitLab Settings → CI/CD → Variables",
}
for k, v in terms.items():
    print(f"  {k:14}: {v}")

print("\n=== .gitlab-ci.yml Example ===")
print("""
# .gitlab-ci.yml
stages:
  - test
  - build
  - deploy

variables:
  IMAGE_NAME: registry.gitlab.com/mygroup/myapp

# ── Test Stage ──────────────────────────────────────────────────
run_tests:
  stage: test
  image: python:3.11-slim
  script:
    - pip install -r requirements.txt pytest
    - pytest tests/ -v
  only:
    - main
    - merge_requests

# ── Build Stage ─────────────────────────────────────────────────
build_image:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE_NAME:latest .
    - docker push $IMAGE_NAME:latest
  only:
    - main

# ── Deploy Stage ────────────────────────────────────────────────
deploy_production:
  stage: deploy
  image: alpine
  script:
    - apk add openssh-client
    - ssh -i $SSH_KEY ubuntu@$SERVER_IP "
        docker pull $IMAGE_NAME:latest &&
        docker stop myapp || true &&
        docker run -d --name myapp -p 8000:8000 $IMAGE_NAME:latest
      "
  environment:
    name: production
    url: http://$SERVER_IP:8000
  only:
    - main
  when: manual   # require manual approval before deploy
""")

print("=== GitLab vs GitHub Actions ===")
comparison = {
    "GitLab CI":       "Built-in registry, environments, self-hosted runners, better for enterprise",
    "GitHub Actions":  "Huge marketplace, easier syntax, better for open source",
}
for k, v in comparison.items():
    print(f"  {k:18}: {v}")
