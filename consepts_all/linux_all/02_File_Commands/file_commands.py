# Linux File Commands - Most used daily

print("=== Create / Copy / Move / Delete ===")
file_cmds = {
    "touch file.txt":           "Create empty file",
    "mkdir myfolder":           "Create directory",
    "mkdir -p a/b/c":           "Create nested directories",
    "cp file.txt backup.txt":   "Copy file",
    "cp -r folder/ backup/":    "Copy directory recursively",
    "mv file.txt /tmp/":        "Move file",
    "mv old.txt new.txt":       "Rename file",
    "rm file.txt":              "Delete file",
    "rm -rf folder/":           "Delete directory (careful!)",
}
for cmd, desc in file_cmds.items():
    print(f"  {cmd:35}: {desc}")

print("\n=== Read / View Files ===")
view_cmds = {
    "cat file.txt":             "Print entire file",
    "less file.txt":            "View file page by page (q to quit)",
    "head -n 20 file.txt":      "First 20 lines",
    "tail -n 20 file.txt":      "Last 20 lines",
    "tail -f app.log":          "Follow log file in real time",
    "grep 'error' app.log":     "Search for 'error' in file",
    "grep -r 'TODO' ./src":     "Search recursively in folder",
    "wc -l file.txt":           "Count lines in file",
}
for cmd, desc in view_cmds.items():
    print(f"  {cmd:35}: {desc}")

print("\n=== Find Files ===")
find_cmds = {
    "find . -name '*.py'":              "Find all .py files",
    "find . -name 'main.py'":           "Find specific file",
    "find /var/log -mtime -1":          "Files modified in last 1 day",
    "find . -size +10M":                "Files larger than 10MB",
    "locate filename":                  "Fast file search (uses index)",
    "which python":                     "Find where command is installed",
}
for cmd, desc in find_cmds.items():
    print(f"  {cmd:40}: {desc}")

print("\n=== Disk Usage ===")
disk_cmds = {
    "df -h":            "Disk space of all partitions",
    "du -sh folder/":   "Size of a folder",
    "du -sh *":         "Size of all items in current dir",
}
for cmd, desc in disk_cmds.items():
    print(f"  {cmd:25}: {desc}")
