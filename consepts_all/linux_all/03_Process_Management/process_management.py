# Linux Process Management - Run, monitor, kill processes

print("=== View Processes ===")
process_cmds = {
    "ps aux":                   "List all running processes",
    "ps aux | grep python":     "Find python processes",
    "top":                      "Live process monitor (q to quit)",
    "htop":                     "Better live monitor (needs install)",
    "pgrep uvicorn":            "Get PID of uvicorn process",
    "pidof python":             "Get PID by name",
}
for cmd, desc in process_cmds.items():
    print(f"  {cmd:35}: {desc}")

print("\n=== Kill Processes ===")
kill_cmds = {
    "kill 1234":            "Send SIGTERM to PID 1234 (graceful stop)",
    "kill -9 1234":         "Force kill PID 1234 (SIGKILL)",
    "pkill uvicorn":        "Kill by process name",
    "killall python":       "Kill all python processes",
}
for cmd, desc in kill_cmds.items():
    print(f"  {cmd:30}: {desc}")

print("\n=== Run in Background ===")
bg_cmds = {
    "python app.py &":              "Run in background",
    "nohup python app.py &":        "Run even after terminal closes",
    "jobs":                         "List background jobs",
    "fg %1":                        "Bring job 1 to foreground",
    "bg %1":                        "Send job 1 to background",
    "Ctrl+C":                       "Stop running process",
    "Ctrl+Z":                       "Pause process (send to background)",
}
for cmd, desc in bg_cmds.items():
    print(f"  {cmd:35}: {desc}")

print("\n=== systemd - Manage Services ===")
systemd_cmds = {
    "sudo systemctl start nginx":       "Start nginx service",
    "sudo systemctl stop nginx":        "Stop nginx service",
    "sudo systemctl restart nginx":     "Restart nginx",
    "sudo systemctl status nginx":      "Check service status",
    "sudo systemctl enable nginx":      "Auto-start on boot",
    "sudo systemctl disable nginx":     "Disable auto-start",
    "journalctl -u nginx -f":           "View service logs live",
}
for cmd, desc in systemd_cmds.items():
    print(f"  {cmd:45}: {desc}")

print("\n=== Environment Variables ===")
env_cmds = {
    "export MY_VAR=hello":          "Set variable for current session",
    "echo $MY_VAR":                 "Print variable value",
    "env":                          "List all environment variables",
    "printenv PATH":                "Print specific variable",
    "source .env":                  "Load variables from .env file",
}
for cmd, desc in env_cmds.items():
    print(f"  {cmd:35}: {desc}")
