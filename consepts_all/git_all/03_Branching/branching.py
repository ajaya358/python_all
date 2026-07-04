# Git Branching - Work on features without affecting main code

print("=== Branch Commands ===")
print("""
git branch                      # list all local branches
git branch -a                   # list local + remote branches
git branch feature-login        # create new branch
git checkout feature-login      # switch to branch
git checkout -b feature-login   # create AND switch (shortcut)
git switch feature-login        # modern way to switch
git switch -c feature-login     # modern way to create + switch

git branch -d feature-login     # delete branch (safe)
git branch -D feature-login     # force delete branch
git push origin --delete feature-login  # delete remote branch
""")

print("=== Merging ===")
print("""
# Merge feature branch into main
git checkout main
git merge feature-login         # merge (creates merge commit)
git merge --squash feature-login # squash all commits into one
git merge --no-ff feature-login  # always create merge commit

# Fast-forward merge (no merge commit if no divergence)
git merge --ff-only feature-login
""")

print("=== Rebase (cleaner history) ===")
print("""
# Instead of merge commit, replay commits on top of main
git checkout feature-login
git rebase main                 # rebase onto main

# Interactive rebase (edit, squash, reorder commits)
git rebase -i HEAD~3            # edit last 3 commits
""")

print("=== Resolve Merge Conflicts ===")
print("""
# When conflict happens:
# Git marks conflicting files like this:
<<<<<<< HEAD
  your changes
=======
  incoming changes
>>>>>>> feature-login

# Steps to resolve:
1. Open conflicting file
2. Edit to keep correct code (remove <<<, ===, >>> markers)
3. git add file.py
4. git commit
""")

print("=== Git Flow (professional branching strategy) ===")
print("""
  main        → production code only, always deployable
  develop     → integration branch, latest development
  feature/*   → new features (branch from develop)
  release/*   → prepare release (branch from develop)
  hotfix/*    → urgent production fixes (branch from main)
  
  Workflow:
  1. git checkout -b feature/user-auth develop
  2. Work on feature, commit
  3. git checkout develop && git merge feature/user-auth
  4. git checkout -b release/1.0.0 develop
  5. Test, fix bugs
  6. git checkout main && git merge release/1.0.0
  7. git tag v1.0.0
""")
