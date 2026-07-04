# Git - Version Control System
# Track changes, collaborate with team, manage code history

print("=== What is Git? ===")
concepts = {
    "Repository (repo)": "Folder tracked by Git — contains all code + history",
    "Commit":            "Snapshot of your code at a point in time",
    "Branch":            "Independent line of development",
    "Merge":             "Combine changes from one branch into another",
    "Remote":            "Repository hosted online (GitHub, GitLab)",
    "Clone":             "Download a remote repo to your machine",
    "Push":              "Upload local commits to remote",
    "Pull":              "Download remote changes to local",
    "Staging Area":      "Area where you prepare files before committing",
    "HEAD":              "Pointer to current commit/branch",
    "Tag":               "Label for a specific commit (v1.0.0)",
}
for k, v in concepts.items():
    print(f"  {k:22}: {v}")

print("\n=== Git Workflow ===")
print("""
  Working Directory → git add → Staging Area → git commit → Local Repo → git push → Remote Repo
  
  1. Edit files in working directory
  2. git add file.py          (stage changes)
  3. git commit -m "message"  (save snapshot locally)
  4. git push origin main     (upload to GitHub/GitLab)
""")

print("=== Git vs GitHub vs GitLab ===")
print("  Git:    Tool installed on your computer — tracks changes locally")
print("  GitHub: Website to host Git repos — collaboration, PRs, Actions")
print("  GitLab: Similar to GitHub — also has built-in CI/CD pipelines")

print("\n=== Install & Setup ===")
print("  Download: https://git-scm.com")
print("  git config --global user.name  'Your Name'")
print("  git config --global user.email 'you@email.com'")
