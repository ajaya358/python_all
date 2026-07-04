# GitHub - Collaborate, review code, automate workflows

print("=== GitHub Key Features ===")
features = {
    "Repository":       "Host your code online, public or private",
    "Pull Request (PR)":"Propose changes, get code review before merging",
    "Issues":           "Track bugs, features, tasks",
    "Actions":          "CI/CD — automate test, build, deploy",
    "Releases":         "Tag versions, attach binaries",
    "Wiki":             "Documentation for your project",
    "Projects":         "Kanban board for task management",
    "Secrets":          "Store API keys, passwords securely for Actions",
    "Branch Protection":"Require PR review before merging to main",
}
for k, v in features.items():
    print(f"  {k:22}: {v}")

print("\n=== GitHub Workflow (Team) ===")
print("""
  1. Fork or clone the repository
  2. Create feature branch: git checkout -b feature/login
  3. Make changes and commit
  4. Push branch: git push origin feature/login
  5. Open Pull Request on GitHub
  6. Team reviews code, leaves comments
  7. Fix review comments, push again
  8. PR approved → Merge to main
  9. CI/CD pipeline deploys automatically
""")

print("=== .gitignore - Files to never commit ===")
print("""
# .gitignore
__pycache__/
*.pyc
*.pyo
.env                    # secrets!
.venv/
venv/
*.db
*.sqlite3
.DS_Store
node_modules/
dist/
build/
*.log
.idea/
.vscode/
""")

print("=== README.md - Project documentation ===")
print("""
# My Project

## Description
Brief description of what the project does.

## Installation
pip install -r requirements.txt

## Usage
uvicorn main:app --reload

## API Endpoints
- GET  /users       - List all users
- POST /users       - Create user
- GET  /users/{id}  - Get user by ID

## Environment Variables
DATABASE_URL=postgresql://...
SECRET_KEY=...

## Contributing
1. Fork the repo
2. Create feature branch
3. Submit Pull Request
""")

print("=== Useful GitHub URLs ===")
print("  github.com/username/repo/issues          → Issues")
print("  github.com/username/repo/pulls           → Pull Requests")
print("  github.com/username/repo/actions         → CI/CD Workflows")
print("  github.com/username/repo/settings/secrets → Secrets")
