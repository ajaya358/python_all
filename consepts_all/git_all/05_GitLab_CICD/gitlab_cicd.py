# GitLab - Git hosting + built-in CI/CD

print("=== GitLab vs GitHub ===")
comparison = {
    "CI/CD":        "GitLab: built-in powerful pipelines | GitHub: Actions (marketplace)",
    "Registry":     "GitLab: built-in Docker/package registry | GitHub: GitHub Packages",
    "Self-hosted":  "GitLab: free self-hosted option | GitHub: paid Enterprise",
    "Issues":       "Both have issues, boards, milestones",
    "Merge Request":"GitLab calls PR a 'Merge Request' (MR)",
}
for k, v in comparison.items():
    print(f"  {k:14}: {v}")

print("\n=== GitLab Workflow ===")
print("""
  1. Create branch from main/develop
  2. Push code: git push origin feature/my-feature
  3. Open Merge Request (MR) on GitLab
  4. CI pipeline runs automatically (tests, lint, build)
  5. Team reviews code
  6. MR approved + pipeline green → Merge
  7. CD pipeline deploys to staging/production
""")

print("\n=== .gitlab-ci.yml - Full Pipeline ===")
print("""
stages:
  - lint
  - test
  - build
  - deploy

variables:
  IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA

lint:
  stage: lint
  image: python:3.11-slim
  script:
    - pip install flake8
    - flake8 . --max-line-length=100

test:
  stage: test
  image: python:3.11-slim
  services:
    - postgres:15
  variables:
    POSTGRES_DB: testdb
    POSTGRES_USER: user
    POSTGRES_PASSWORD: pass
    DATABASE_URL: postgresql://user:pass@postgres/testdb
  script:
    - pip install -r requirements.txt pytest
    - pytest tests/ -v --cov=. --cov-report=xml
  coverage: '/TOTAL.*\\s+(\\d+%)$/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE .
    - docker push $IMAGE
  only:
    - main

deploy_staging:
  stage: deploy
  script:
    - echo "Deploy to staging server"
  environment:
    name: staging
    url: https://staging.myapp.com
  only:
    - main

deploy_production:
  stage: deploy
  script:
    - echo "Deploy to production"
  environment:
    name: production
    url: https://myapp.com
  only:
    - main
  when: manual
""")

print("=== GitLab Predefined Variables ===")
variables = {
    "$CI_COMMIT_BRANCH":    "Current branch name",
    "$CI_COMMIT_SHORT_SHA": "Short commit hash (abc1234)",
    "$CI_REGISTRY":         "GitLab container registry URL",
    "$CI_REGISTRY_USER":    "Registry username",
    "$CI_REGISTRY_PASSWORD":"Registry password",
    "$CI_PROJECT_NAME":     "Project name",
    "$CI_ENVIRONMENT_NAME": "Deployment environment name",
}
for k, v in variables.items():
    print(f"  {k:30}: {v}")
