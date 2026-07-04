# Linux - Essential for every developer
# All servers run Linux. You must know basic commands.

print("=== Why Linux? ===")
print("  - All cloud servers (AWS EC2, Azure VM) run Linux")
print("  - Docker containers use Linux")
print("  - Most backend deployments are on Linux")
print("  - SSH into servers, run scripts, manage processes\n")

print("=== Linux File System Structure ===")
structure = {
    "/":        "Root directory — top of everything",
    "/home":    "User home directories (/home/ubuntu)",
    "/etc":     "Config files (nginx.conf, hosts, environment)",
    "/var":     "Variable data — logs (/var/log), databases",
    "/tmp":     "Temporary files — cleared on reboot",
    "/usr":     "User programs and libraries",
    "/bin":     "Essential commands (ls, cp, mv, cat)",
    "/opt":     "Optional/third-party software",
    "/proc":    "Virtual filesystem — running processes info",
}
for path, desc in structure.items():
    print(f"  {path:10}: {desc}")

print("\n=== Navigation Commands ===")
nav = {
    "pwd":              "Print current directory",
    "ls":               "List files",
    "ls -la":           "List all files with details and hidden files",
    "cd /path":         "Change directory",
    "cd ..":            "Go up one level",
    "cd ~":             "Go to home directory",
    "tree":             "Show directory tree",
}
for cmd, desc in nav.items():
    print(f"  {cmd:20}: {desc}")

print("\n=== File Permissions ===")
print("  -rwxrwxrwx  →  - (file) rwx (owner) rwx (group) rwx (others)")
print("  r=read(4)  w=write(2)  x=execute(1)")
print("  chmod 755 file   → owner:rwx group:r-x others:r-x")
print("  chmod +x file    → add execute permission")
print("  chown user:group file → change owner")
