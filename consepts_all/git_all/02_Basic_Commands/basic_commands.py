# Git Basic Commands - Daily workflow commands

print("=== Setup ===")
print("""
git config --global user.name  "Jayaram"
git config --global user.email "jayaram@email.com"
git config --global core.editor "code --wait"   # use VS Code as editor
git config --list                                # view all config
""")

print("=== Start a Repository ===")
print("""
git init                        # create new repo in current folder
git clone <url>                 # download existing repo
git clone <url> my-folder       # clone into specific folder
""")

print("=== Daily Workflow ===")
print("""
git status                      # see what changed
git diff                        # see exact changes (unstaged)
git diff --staged               # see staged changes

git add file.py                 # stage one file
git add .                       # stage all changes
git add src/                    # stage a folder

git commit -m "Add user login"  # commit with message
git commit -am "Fix bug"        # add + commit tracked files

git log                         # view commit history
git log --oneline               # compact history
git log --oneline --graph       # visual branch graph
""")

print("=== Undo Changes ===")
print("""
git restore file.py             # discard unstaged changes
git restore --staged file.py    # unstage a file
git reset HEAD~1                # undo last commit (keep changes)
git reset --hard HEAD~1         # undo last commit (discard changes)
git revert <commit-hash>        # create new commit that undoes a commit (safe)
""")

print("=== Remote ===")
print("""
git remote add origin <url>     # connect local repo to remote
git remote -v                   # view remotes
git push origin main            # push to main branch
git push -u origin main         # push and set upstream (first time)
git pull origin main            # pull latest changes
git fetch origin                # download changes without merging
""")

print("=== Stash (save work temporarily) ===")
print("""
git stash                       # save uncommitted changes temporarily
git stash pop                   # restore stashed changes
git stash list                  # view all stashes
git stash drop                  # delete latest stash
""")
