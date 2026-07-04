# CI/CD - Continuous Integration / Continuous Deployment
# Automatically test and deploy your code on every push

print("=== What is CI/CD? ===")
concepts = {
    "CI (Continuous Integration)": "Auto run tests on every code push",
    "CD (Continuous Delivery)":    "Auto build and prepare for deployment",
    "CD (Continuous Deployment)":  "Auto deploy to production after tests pass",
    "Pipeline":                    "Series of automated steps: test → build → deploy",
    "Trigger":                     "Event that starts pipeline (push, PR, tag)",
    "Runner":                      "Machine that executes pipeline steps",
    "Artifact":                    "Output of build step (Docker image, zip file)",
}
for k, v in concepts.items():
    print(f"  {k:35}: {v}")

print("\n=== CI/CD Flow ===")
flow = [
    "1. Developer pushes code to GitHub/GitLab",
    "2. CI pipeline triggers automatically",
    "3. Install dependencies",
    "4. Run linting (code style check)",
    "5. Run tests (pytest)",
    "6. Build Docker image",
    "7. Push image to registry (Docker Hub / ECR)",
    "8. Deploy to server (EC2, ECS, Kubernetes)",
    "9. Notify team (Slack, email)",
]
for step in flow:
    print(f"  {step}")

print("\n=== Tools ===")
tools = {
    "GitHub Actions": "Built into GitHub, free for public repos, easy YAML config",
    "GitLab CI/CD":   "Built into GitLab, powerful, self-hosted option",
    "Jenkins":        "Open source, highly customizable, needs server",
    "CircleCI":       "Cloud-based, fast, good Docker support",
    "AWS CodePipeline":"AWS native CI/CD, integrates with ECR/ECS/Lambda",
}
for tool, desc in tools.items():
    print(f"  {tool:18}: {desc}")

print("\n=== Why CI/CD Matters for Jobs ===")
print("  - Every company uses CI/CD in production")
print("  - Prevents 'works on my machine' problems")
print("  - Faster releases, fewer bugs in production")
print("  - Asked in almost every backend/DevOps interview")
